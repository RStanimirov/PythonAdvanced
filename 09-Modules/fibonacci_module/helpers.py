def create_sequence(n):
    fibonacci_sequence = [0, 1]
    for _ in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


def locate(seq, num):
    if num in seq:
        print(f"The number - {num} is at index {seq.index(num)}")
    else:
        print(f"The number {num} is not in the sequence")

