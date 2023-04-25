while True:
    with open("../files/sides.txt", "r") as file:
        sides = file.readlines()

    side_of_coin = input("Throw the coin and enter head or tail here: ? ") + "\n"

    sides.append(side_of_coin)

    with open("../files/sides.txt", "w") as file:
        file.writelines(sides)

    total_heads = sides.count("head\n")
    percentage = total_heads / len(sides) * 100

    print(f"Heads: {percentage}%")



