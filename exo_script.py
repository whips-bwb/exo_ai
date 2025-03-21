# import os, sys

def process_data(data):
    if isinstance(data, list) == True:
        process_list(data)
    elif isinstance(data, dict):
        process_dict(data)
    else:
        print("Unsupported data type")

def process_list(list_data):
    for i in range(len(list_data)):
        print(list_data[i])

def process_dict(dict_data):
    for key in dict_data:
        print(key, dict_data[key])

data = [1, 2, 3]
process_data(data)

# Some complex if-else logic with redundant conditions
def is_number_positive(numb):
    if numb > 0:
        result = "positive"
    elif numb == 0:
        result = "zero"
    elif numb < 0:
    result = "negative"  # Incorrect indentation
    return result

print(is_number_positive(-5))  # Check with negative number

def example_function():
    # This function has bad indentation
    print("Hello world!")


def another_function():
    a = 10  # Missing spaces around the assignment operator
    print(a)


if __name__ == "__main__":
    example_function()
    another_function()
