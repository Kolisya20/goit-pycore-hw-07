from models.address_book import AddressBook
from models.record import Record

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("25.11.1990")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("01.11.1988")
    book.add_record(jane_record)

    for name, record in book.items():
        print(record)

    print("\nContacts with birthdays in the upcoming week:")
    for record in book.get_upcoming_birthdays():
        print(record)
