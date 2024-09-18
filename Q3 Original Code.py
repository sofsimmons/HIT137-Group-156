global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Colon was added after defining process_numbers and update_global

def process_numbers():
    global global_variable
    global_variable = 5
    numbers = [1, 2, 3, 4, 5]
    local_variable = len(numbers)  # Define local_variable based on the numbers list

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable) # Use numbers instead of number
        local_variable -= 1

    return numbers

my_set = {1,2,3,4,5,5,4,3,2,1}
result = process_numbers() # Removed argument 'numbers'

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict() # No argument needed

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i) #This prints 0 to 4 without needing to increment i

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionaryy")

print(global_variable)
print(my_dict)
print(my_set)