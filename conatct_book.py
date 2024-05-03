class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_all_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                found = True
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self, name):
        deleted = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted.")
                deleted = True
                break
        if not deleted:
            print(f"Contact '{name}' not found.")

def main():
    address_book = AddressBook()

    while True:
        print("\nWhat do you plan to do: ")
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone, email)
            address_book.add_contact(contact)
        elif choice == '2':
            address_book.view_all_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            address_book.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n\n")

if __name__ == "__main__":
    main()
