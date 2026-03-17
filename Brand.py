brand = str(input("What's the model of the car: "))

match brand:
    case "Verna" | "Creta" | "i20" | "Venue":
        print("The brand of the Car is Hyndai")
    
    case "Punch" | "Safari" | "Harrier":
        print("The brand of the car is TATA")

    case _:
        print("Maybe an Japanese Manufacturer")


