names = []
ages = []
emails = []

name = input("Name: ")
age = input("Age: ")
email = input("Email: ")

names.append(name)
ages.append(age)
emails.append(email)

print(names, ages, emails)  # Output ['asad'] ['25'] ['asad123@gmail.com']
#######################################################################################
names = []
ages = []
emails = []

for i in range(3):
    print(i + 1, "Input")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    names.append(name)
    ages.append(age)
    emails.append(email)

print(
    names, ages, emails
)  # Output ['das', 'util', 'horn'] ['45', '54', '51'] ['das@hotmail.com', 'utl@gmail.com', 'horn@gmail.com']
################################################################################################################
## Dictionary
people = []

for i in range(3):
    print(i + 1, "Input")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    people.append(person)

print(
    people
)  # Output Dictionaries inside lists>> [{'name': 'hit', 'age': '50', 'email': 'hit@hotmail.com'}, {'name': 'get', 'age': '25', 'email': 'get@newmail.com'}, {'name': 'said', 'age': '45', 'email': 'said@oldmail.com'}]


#######################################################################################
## Adding Functionality to the System (Add, Del, Search)
###Complete project below

import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number")

    people.pop(number - 1)  # Feature mutable/immutable here can be used
    print("Person deleted.")


## Search function works this way
def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)


print("Hi, welcome to the Contact Management System")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit:").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)
        pass
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)

# print(people)  # Output add=[{'name': 'dare', 'age': '24', 'email': 'dare@gmail.com'}]
