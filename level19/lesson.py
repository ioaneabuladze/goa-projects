numbers = [1, 2, 3, 4, 5]


numbers.extend([numbers[0]] * 3)  
numbers.extend([numbers[3]] * 3) 

strings = ["apple", "banana", "date", "griope", "grape", "kiwi"]


middle_index = len(strings) // 2
print(strings[middle_index]) 


my_string = "Hello"


print(my_string[1:3])