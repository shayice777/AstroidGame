def save_number():
    number = input("Please enter a number: ")
    with open("number_store.txt", "w") as file:
        file.write(number)
    print("Number saved!")


def load_number():
    try:
        with open("number_store.txt", "r") as file:
            number = file.read()
            print(f"The last number you entered was: {number}")
    except FileNotFoundError:
        print("No number was saved previously.")


def main():
    while True:
        print("1. Enter a new number")
        print("2. Load last number")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            save_number()
        elif choice == "2":
            load_number()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")



main()
