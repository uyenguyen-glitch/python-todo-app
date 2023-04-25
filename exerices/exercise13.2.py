names = input("Enter names separated by commas (no spaces): ")
def number_of_names(list_name):
    name = list_name.split(',')
    total = len(name)
    return total


numbers = number_of_names(names)
print(numbers)
