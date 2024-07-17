#!/bin/bash
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            a= input("Enter an item to be added: ")
            shopping_list.append(a)
        elif choice == '2':
            # Prompt for and remove an item
            b = input("Enter an item to be removed: ")
            if b in shopping_list:
                shopping_list.remove(b)
            else:
                print("The item does not exist")
        elif choice == '3':
            # Display the shopping list
            my_string = list(shopping_list)
            print(my_string)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
