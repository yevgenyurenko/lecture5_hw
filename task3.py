import random
s = input('Input a string: ')
string_length = len(s)

for _ in range(string_length):
    random_string = ''.join(random.sample(s,5))
    print(random_string)