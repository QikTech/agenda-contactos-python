# the csv module (Comma Separated Values) let read and write tabular data in csv format
import csv


# Class with the data of each contact
class Contact:

    # construct method
    def __init__(self, Pname, Pphone, Pemail):
        """
        : param Pname: Name of the new record
        : param Pphone: Phone of the new record
        : param Pemail: Email of the new record
        """
        self.name = Pname
        self.phone = Pphone
        self.email = Pemail


# Class containing objects of type Contact
class ContactBook:

    # construct method
    # initialize the contact book with an empty list
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        """
        Adds an object of type Contact to the list and saves it
        : param name: Name of the new record
        : param phone: Phone of the new record
        : param email: Email of the new record
        : return: none
        """
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        print("**Successful registration.")

    def delete(self, name):
        """
        search for a contact by name and delete it, then save the csv
        : param name: name of the record to delete
        :return: none
        """
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                print("Contact {} was successfully removed.".format(contact.name))
                break
        else:
            self._not_found()

    def _save(self):
        """
        uses or creates a contact.csv file (w = write) and writes the lines of
        header, and then a for loop to write all contact data
        :return:
        """
        with open('contact.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        """
        method that prints a contact
        : param contact: contact to print
        :return: none
        """
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Phone No: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def show_all(self):
        """
        Print all the contacts using the _print_contact method
        :return: none
        """
        for contact in self._contacts:
            self._print_contact(contact)

    def search(self, name):
        """
        Search for a name in the contact list
        when you find it break
        : param name: name to search
        :return: none
        """
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        """
        update contact details
        : param name: contact name to update
        :return: none
        """
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.phone = str(input("New phone: "))
                contact.email = str(input("New email: "))
                self._save()
                print("**Updated registration.")

    def _not_found(self):
        print('*******')
        print('Not found!')
        print('*******')


def run():
    # Creating an instance of the ContactBook class
    contact_book = ContactBook()

    # Open a file called "contact.csv" (r = read) and extract the content for
    # use it in the terminal app, if it takes the header or empty line: continue
    with open('contact.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            if row == []:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input("""
            What would you like to do?
            
            [a]add contact
            [ac]update contact
            [b]search contact
            [e]preliminary contact
            [l]List contacts
            [s]exit
        """))

        if command == 'a':
            name = str(input("Write the name of the contact: "))
            phone = str(input("Write the phone number of the contact: "))
            email = str(input("Write the contact email: "))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input("Write the name of the contact: "))
            contact_book.update(name)

        elif command == 'b':
            name = str(input("Write the name of the contact: "))
            contact_book.search(name)

        elif command == 'e':
            name = str(input("Write the name of the contact to delete: "))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break

        else:
            print('Command not found!')


# these lines are used to execute only this file
# in case there are other imported python modules
if __name__ == '__main__':
    print('W E L C O M E')
    run()