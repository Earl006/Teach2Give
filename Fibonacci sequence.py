fibonacci_sequence = [0, 1]
while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= 100:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print(fibonacci_sequence)