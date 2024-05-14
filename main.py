from q import QuantumSimulator

def main():
    simulator = QuantumSimulator(num_qubits=1)

    result = simulator.flip_coin()
    print("Jane and John, you said:", result)

if __name__ == "__main__":
    main()
