# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.

sentence = input("Enter a sentence: ")
vowels = "aeiou"
count = 0
vowels_seen = []
for i in sentence:
    if i in vowels and not i in vowels_seen:
        vowels_seen.append(i)
        count += 1
print(count)