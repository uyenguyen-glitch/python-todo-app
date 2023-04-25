birth = int(input("Enter your age: "))


def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


age = get_age(birth)

# Print age if equal or less than 120
if age <= 120:
    print(age)
else:
    print("Hold on there, grandpa! That's a bit overhead")
