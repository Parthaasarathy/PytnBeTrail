name = input("Whats your favourite car?")

with open ("cars.txt", "a") as file:
    file.write(f"{name}\n")
