import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users
                      if name.lower in user["name"].lower()]

    print(filtered_users if filtered_users else "name not found")


def filter_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users
                      if user["age"] == age]

    print(filtered_users if filtered_users else "no user with that age")


def filter_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users
                      if email.lower() in user["email"].lower()
    ]

    print(filtered_users if filtered_users else "email not found")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter a age to filter users: ").strip())
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
