import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Current phone: {contacts[name]['phone']}, Current email: {contacts[name]['email']}")
        phone = input("Enter new phone (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
