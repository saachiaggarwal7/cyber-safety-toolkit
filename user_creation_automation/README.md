# User Creation Automation

A Python utility that automates Linux user management by creating users, setting passwords securely, and assigning users to groups.

---

## Features

- Checks if a user already exists
- Creates new Linux users
- Automatically creates a home directory (`useradd -m`)
- Secure password input using `getpass`
- Sets user passwords automatically
- Adds users to Linux groups
- Handles invalid user input and common errors

---

## Technologies Used

- Python
- `subprocess`
- `getpass`

---

## Project Structure

```
user-creation-automation/
│
├── user_creation.py
└── README.md
```

---

## Example

### Input

```
Enter username:
alice

Enter password:
********

Add user to a group?

1. sudo
2. developers
3. users
4. Skip

Enter your choice:
1
```

### Output

```
User created successfully.
Password set successfully.
User added to sudo group successfully.
```

---

## How It Works

1. Checks whether the specified user already exists.
2. Creates a new Linux user with a home directory.
3. Securely accepts a password without displaying it on the screen.
4. Sets the user's password using `chpasswd`.
5. Optionally adds the user to a Linux group (`sudo`, `developers`, or `users`).
6. Displays success or error messages based on the operation.

---

## Linux Commands Used

- `id` – Check if a user exists
- `useradd -m` – Create a new user with a home directory
- `chpasswd` – Set the user's password
- `usermod -aG` – Add a user to a supplementary group

---

## Requirements

- Linux operating system
- Python 3.x
- Administrator (`sudo`) privileges

---

## Future Improvements

- Delete existing users
- Modify user information
- Create custom groups automatically
- Validate whether a selected group exists
- Log user creation activities
- Support batch user creation from a CSV file
