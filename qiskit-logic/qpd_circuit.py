

# Importing the essentials

import numpy as np
from qiskit import *
from qiskit import Aer

# Creating a two-qubit Quantum circuit

qreg = QuantumRegister(2)
creg = ClassicalRegister(1)
circuit = QuantumCircuit(qreg, creg)

# Assigning the value of gamma from user input.
gamma = np.pi


#Adding J gate or entanglement gate in the circuit

circuit.ry(gamma/2,0)
circuit.cnot(0, 1)
circuit.s(1)

# Adding the individual unitaries as per the input from interface

gamma_A = gamma/2
phi_A = gamma/4

gamma_B = gamma/2
phi_B = gamma/4

circuit.rz(-phi_A, 0)
circuit.ry(gamma_A, 0)
circuit.rz(-phi_A, 0)

circuit.rz(-phi_B, 0)
circuit.ry(gamma_B, 0)
circuit.rz(-phi_B, 0)

# Adding J diagger at last into the circuit model


circuit.sdg(1)
circuit.cnot(0, 1)
circuit.ry(gamma/2,0)

# Summoning the simulator to evaluate our statevector at the end

backend = Aer.get_backend('statevector_simulator') 

job = backend.run(circuit)
results = job.result()
outputstate = results.get_statevector(circuit, decimals=3)
print(outputstate)