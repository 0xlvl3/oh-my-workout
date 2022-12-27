import json

# If user has been created locally, maybe through JSON?
# Check for directory as well


def welcome_back():
    with open("user_details/username.json") as file:
        data = file.read()

    data = json.loads(data)
    GLOBAL_USER = data["username"]
    return GLOBAL_USER
