from fibonacci_module.helpers import create_sequence, locate


def run_fibonacci():
    data = input()
    result = []

    while data != "Stop":
        split_data = data.split()
        if split_data[0] == "Create":
            number = int(split_data[-1])
            result = create_sequence(number)
            print(*result)
        elif split_data[0] == "Locate":
            number = int(split_data[-1])
            locate(result, number)
        data = input()
