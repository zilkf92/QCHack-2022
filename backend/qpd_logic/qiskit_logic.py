import numpy as np
import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

# from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector
from qiskit.providers.aer import QasmSimulator

from qpd_logic.gates import Jgate, Jdggate, Ustrategy


def play_game(gamma, theta, phi, qpu):

    # Protocol uses 2 qubits and 2 classical bits in 2 different registers

    qr = QuantumRegister(2)  # Protocol uses 2 qubits
    cr = ClassicalRegister(2)  # and 2 classical bits
    qc = QuantumCircuit(qr, cr)
    # qc.draw()

    # J gate is entangling gate acting on |00>
    Jgate(qc, qr, gamma)
    qc.barrier()
    # qc.draw()

    # Human player strategy U acting on respective qubit
    Ustrategy(qc, qr, 0, theta * np.pi, phi * np.pi / 2)

    # Choose random strategy for computer player
    theta_b = random.uniform(0, 1)
    phi_b = random.uniform(0, 1)
    Ustrategy(qc, qr, 1, theta_b * np.pi, phi_b * np.pi / 2)
    qc.barrier()
    # qc.draw()

    # Apply J dagger
    Jdggate(qc, qr, gamma)
    qc.barrier()

    # Measure qubits
    qc.measure(0, 0)
    qc.measure(1, 1)

    # Logic is currently only implemented for simulator backend
    # Token needs to be retrieved from FE for QPU access
    if qpu == "true":

        # Load IBM Q account and get the least busy backend device
        provider = IBMQ.load_account()
        provider = IBMQ.get_provider("ibm-q")
        device = least_busy(
            provider.backends(
                filters=lambda x: x.configuration().n_qubits >= 3
                and not x.configuration().simulator
                and x.status().operational == True
            )
        )
        print("Running on current least busy device: ", device)
        # Run our circuit on the least busy backend. Monitor the execution of the job in the queue
        transpiled_circuit = transpile(qc, device, optimization_level=3)
        job = device.run(transpiled_circuit)
        job_monitor(job, interval=2)
        # Get the results from the computation
        results = job.result()
        answer = results.get_counts(qc)
        # plot_histogram(answer)
        return answer

    else:

        # Choose noisy quantum circuit simulator as backend
        backend = QasmSimulator()

        qc_compiled = transpile(qc, backend)
        job_sim = backend.run(qc_compiled, shots=1024)

        result_sim = job_sim.result()

        counts = result_sim.get_counts(qc_compiled)

        return counts
