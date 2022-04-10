import numpy as np
import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize

# from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector
from qiskit.providers.aer import QasmSimulator

from qpd_logic.gates import Jgate, Jdggate, Ustrategy


def play_game(gamma, theta, phi):
    ## SETUP
    # Protocol uses 2 qubits and 2 classical bits in 2 different registers

    qr = QuantumRegister(2)  # Protocol uses 2 qubits
    cr = ClassicalRegister(2)  # and 2 classical bits
    qc = QuantumCircuit(qr, cr)
    # qc.draw()

    Jgate(qc, qr, gamma)
    qc.barrier()
    # qc.draw()

    Ustrategy(qc, qr, 0, theta * np.pi, phi * np.pi / 2)

    # choose strategy for computer
    theta_b = random.uniform(0, 1)
    phi_b = random.uniform(0, 1)
    Ustrategy(qc, qr, 1, theta_b * np.pi, phi_b * np.pi / 2)
    qc.barrier()
    # qc.draw()

    Jdggate(qc, qr, gamma)
    qc.barrier()

    # measure qubits
    qc.measure(0, 0)
    qc.measure(1, 1)

    backend = QasmSimulator()

    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=1024)

    result_sim = job_sim.result()

    counts = result_sim.get_counts(qc_compiled)
    print(counts)
    print(type(counts))
    # plot_histogram(counts)
    return counts
