def get_integer_input():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            number = int(user_input)
            return number  
        except ValueError:
            print("Error: That's not an integer. Please try again.")
print("This program will keep asking until you enter a valid integer.")
result = get_integer_input()
print(f"You entered the integer: {result}")
