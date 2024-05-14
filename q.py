import numpy as np

class QuantumSimulator:
    def __init__(self, num_qubits=1):
        self.num_qubits = num_qubits

#State initialization
    def flip_coin(self):
        state = np.array([1, 0])

#Hadamard gate
        hadamard = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
                             [1/np.sqrt(2), -1/np.sqrt(2)]])
        for _ in range(self.num_qubits):
            state = np.dot(hadamard, state)

 # Measurement
        measured_state = np.random.choice([0, 1], size=self.num_qubits, p=[abs(state[0])**2, abs(state[1])**2])

        return measured_state

