import json


def filter_users_by_name(name):
    """
    Filter users by name.

    Args:
        name (str): Name or partial name to search for.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [
        user
        for user in users
        if name.lower() in user["name"].lower()
    ]

    print(filtered_users if filtered_users else "Name not found.")


def filter_users_by_age(age):
    """
    Filter users by age.

    Args:
        age (int): Age to search for.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [
        user
        for user in users
        if user["age"] == age
    ]

    print(filtered_users if filtered_users else "No user with that age.")


def filter_users_by_email(email):
    """
    Filter users by email.

    Args:
        email (str): Email or partial email to search for.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [
        user
        for user in users
        if email.lower() in user["email"].lower()
    ]

    print(filtered_users if filtered_users else "Email not found.")


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? "
        "(Currently supported: 'name', 'age', 'email'): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input(
            "Enter a name to filter users: "
        ).strip()

        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(
            input("Enter an age to filter users: ").strip()
        )

        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input(
            "Enter an email to filter users: "
        ).strip()

        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")