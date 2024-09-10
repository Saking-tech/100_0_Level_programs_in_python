# Program for a simple contact book

# Initialize the contact book
contacts = {}

# Function to add a contact
def add_contact(name, number):
    contacts[name] = number

# Function to display all contacts
def show_contacts():
    if contacts:
        print("Contact Book:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts available")

# Main menu
while True:
    print("\n1. Add Contact\n2. Show Contacts\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid option")
