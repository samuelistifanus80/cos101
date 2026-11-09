while True:
    user_input = int(input("Input any number greater than 1 or press e to exit: "))

    if user_input.lower() == "e":
        print("Program terminated.")
        break
    elif not user_input.isdigit():
          number = int(user_input)
            

    elif number <= 1:
        print("Invalid input! The number must be greater than 1.")

    elif number > 12:
        print("Invalid input! Enter a number between 2 and 12.")

    else:
        print(f"\nMultiplication table of {number}")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

        print("--------------------------")



