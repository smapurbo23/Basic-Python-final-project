# User Choosing Options
print("What do you want to do? \n 1.Add new contact\n 2.Update contact\n 3.Delete contact\n 4.Search contact\n")
user = int(input("Enter your option: "))

names = []
phoneNumbers = []
emails = []

if user == 1:

    name = input("Name: ")
    phone_number = input("Phone Number: ")  # for convert to int => int(input("Phone Number: "))
    email = input("Email: ")

    names.append(name)
    phoneNumbers.append(phone_number)
    emails.append(email)
    print("Contact added successfully")

if user == 2:
    update = int(input("Which contact do you want to update? \n"))

    if update in names:
        name = input("Name: ")
        phone_number = input("Phone Number: ")  # for convert to int => int(input("Phone Number: "))
        email = input("Email: ")

        names.append(name)
        phoneNumbers.append(phone_number)
        emails.append(email)

        print("Contact updated successfully")
    else:
        print("Invalid Input!")

# if user = 3:
#     update = int(input("Which contact do you want to update? \n"))
#
#     if update in names:

# if user == 4:
#      search = input("Enter the contact to search: ")
#
#      if search in names:
#             print(names.)

