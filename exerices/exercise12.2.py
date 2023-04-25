def check_password(password):
    results = {}

    # Check length of password
    if len(password) >= 8:
        results["length:"] = True
    else:
        results["length"] = False

    # Check digit in password
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    results["digit"] = digit

    # Check capitalize letter in password
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    results["uppercase"] = uppercase


    # Check final result
    if all(results.values()):
        return print("Strong password")
    else:
        return print("Weak password")


# Main
password = input("Enter your password: ")

check_password(password)
