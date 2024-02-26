# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

fibonacci_sequence = [0, 1]
while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= 100:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print(fibonacci_sequence)