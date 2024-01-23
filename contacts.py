import json

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            print("No existing contact file found. Starting with an empty contact book.")

    def save_contacts_to_file(self, filename):
        data = [{'name': contact.name, 'phone_number': contact.phone_number,
                 'email': contact.email, 'address': contact.address} for contact in self.contacts]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print("Contact book saved successfully.")

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts
                          if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if not found_contacts:
            print(f"No contacts found with '{search_term}'.")
        else:
            print("\nFound Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, contact_name):
        for contact in self.contacts:
            if contact_name.lower() == contact.name.lower():
                print(f"Updating contact: {contact.name}")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {contact.name} updated successfully!")
                return
        print(f"No contact found with the name '{contact_name}'.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact_name.lower() == contact.name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully!")
                return
        print(f"No contact found with the name '{contact_name}'.")

def print_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts to File")
    print("7. Load Contacts from File")
    print("8. Exit")

def main():
    contact_book = ContactBook()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            contact_name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(contact_name)

        elif choice == '5':
            contact_name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(contact_name)

        elif choice == '6':
            contact_book.save_contacts_to_file("contacts.json")

        elif choice == '7':
            contact_book.load_contacts_from_file("contacts.json")

        elif choice == '8':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
