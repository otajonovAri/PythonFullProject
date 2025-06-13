# Predefined user credentials (for a simple example)
users = {
    "asad": "12345",
    "ali": "password123",
    "dilshod": "qwerty"
}

# Ask the user to enter username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Authentication check
if username in users:
    if users[username] == password:
        print("Successfully logged in!")
    else:
        print("Incorrect password!")
else:
    print("Username not found!")
