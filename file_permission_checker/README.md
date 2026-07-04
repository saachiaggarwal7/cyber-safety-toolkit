# File Permission Checker

A Python utility that analyzes Linux file and directory permissions, displays access rights, and warns about insecure world-writable permissions.

---

## Features

- Validates file and directory paths
- Detects whether the path is a file or directory
- Checks read, write, and execute permissions
- Displays octal permissions (e.g., `755`)
- Displays symbolic permissions (e.g., `-rwxr-xr-x`)
- Detects insecure world-writable permissions
- Warns about potential security risks

---

## Technologies Used

- Python
- `os`
- `stat`

---

## Project Structure

```
file-permission-checker/
│
├── file_permission_checker.py
└── README.md
```

---

## Example

### Input

```
Enter path:
/home/user/test.txt
```

### Output

```
Type:         File
Read:         True
Write:        True
Execute:      False
Permissions:  644
Symbolic:     -rw-r--r--
```

### Example Warning

```
Permissions: 777
Symbolic: -rwxrwxrwx

[WARNING] File is world-writable and may pose a security risk
```

---

## How It Works

1. Validates the provided path.
2. Determines whether the path is a file or directory.
3. Checks the current user's read, write, and execute permissions.
4. Retrieves the file's octal and symbolic permission formats.
5. Detects common insecure permissions (`777`, `767`, `666`) and displays a warning.

---

## Why It Matters

Files with world-writable permissions can be modified by any user on the system, increasing the risk of:

- Unauthorized file modification
- Privilege escalation
- Malware or script tampering
- Accidental deletion or corruption

Checking file permissions is an essential part of Linux system administration and security auditing.

---

## Future Improvements

- Scan an entire directory recursively
- Detect additional insecure permission patterns
- Export scan results to a report file
- Check file ownership and group information
- Suggest secure permission values (e.g., `644`, `755`)
