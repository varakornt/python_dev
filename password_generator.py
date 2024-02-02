import random
import string

lower_chars = list(string.ascii_lowercase)
upper_chars = list(string.ascii_uppercase)
numbers_range = list(range(10))
numbers_list = list(map(str, numbers_range))
special_characters = list(string.punctuation)
#print(special_characters)
#print(lower_chars)
#print(numbers_list)
print("----Password Generator----")

upper_num_chars = int(input("Enter the # of uppercase characters you want: "))
lower_num_chars = int(input("Enter the # of lowercase characters you want: "))
num_nums = int(input("Enter the # of numbers you want: "))
spec_chars = int(input("Enter the # of special chararacters you want: "))

total_password = upper_num_chars + lower_num_chars + num_nums + spec_chars

password = []

for i in range(upper_num_chars):
    password += random.choice(upper_chars)
for i in range(lower_num_chars):
    password += random.choice(lower_chars)
for i in range(num_nums):
    password += random.choice(numbers_list)
for i in range(spec_chars):
    password += random.choice(special_characters)

random.shuffle(password)

password = ''.join(password)
print("\nGenerated password:",password)
total_length = upper_num_chars + lower_num_chars + num_nums + spec_chars
print("\nTotal Length:",total_length)
