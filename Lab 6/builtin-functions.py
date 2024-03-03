#task 1

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply((8, 2, 3, -1, 7)))

#task 2

def count_upper_lower_letters(input_string):
    upper_count = sum(1 for c in input_string if c.isupper())
    lower_count = sum(1 for c in input_string if c.islower())
    return upper_count, lower_count

input_str = "Hello World"
upper, lower = count_upper_lower_letters(input_str)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)


#task 3
def is_palindrome(input_string):
    reversed_string = ''.join(reversed(input_string))
    return input_string == reversed_string

input_str = "123321"
print(is_palindrome(input_str))

ins = int(input())
ml = int(input())

#task 4

def systemSleep(s):
        i = 0
        for i in range(0, int((s*45100000)*2.3)):
            3 * 3
            3 * 3
            3 * 3
systemSleep(int((ml/1000)))
print(ins ** 0.5)

#task 5

def all_elements_true(tuple_data):
    return all(tuple_data)

tuple_data = (1, 2, 3, 4)
if all_elements_true(tuple_data):
    print("All elements of the tuple are true.")
else:
    print("Not all elements of the tuple are true")