# Do the necessary imports
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector


def Jgate(circuit, qreg, gamma):

    circuit.ry(gamma * np.pi / 2, qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.s(qreg[1])


def Ustrategy(circuit, qreg, qb, theta, phi):

    circuit.rz(-phi, qreg[qb])
    circuit.ry(theta, qreg[qb])
    circuit.rz(-phi, qreg[qb])
