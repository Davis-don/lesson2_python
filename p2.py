students = [
    {
        "first_name": "",
        "last_name": "",
        "username": "samorai",
        "password": "",
        "age": 0
    }
]

# Check if username already exists
def isUsernameSimilar(username):
    for student in students:
        if student["username"] == username:
            return True
    return False


def create_Account():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # LOOP until unique username is given
    while True:
        username = input("Enter your username: ")

        if isUsernameSimilar(username):
            print("❌ Username exists! Try another.")
        else:
            print("✔ Username available.")
            break

    age = int(input("Enter your age: "))

    # Confirm password
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            break
        else:
            print("❌ Passwords do not match. Try again.")

    # Save account
    students.append({
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "age": age
    })

    print("🎉 Account created successfully!")


def run_until_exit(run_func):
    while True:
        run_func()  # call the function properly

        choice = int(input("""
Do you want to continue?
1) Yes
2) No
Choice: """))

        if choice == 2:
            break

    print("All students:", students)


run_until_exit(create_Account)
