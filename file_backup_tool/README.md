# File Backup Tool

A Python utility that creates timestamped backups of files while preserving metadata and maintaining a backup history log.

---

## Features

- Validates file paths
- Automatically creates a `backups` directory
- Creates timestamped backup copies
- Preserves original file metadata
- Logs every backup operation
- Displays the backup location after completion

---

## Technologies Used

- Python
- `os`
- `shutil`
- `datetime`

---

## Project Structure

```
file-backup-tool/
│
├── file_backup_tool.py
├── backup.log
├── backups/
└── README.md
```

---

## Example

### Input

```
Enter the file path:
/home/user/Documents/report.pdf
```

### Output

```
Backup created successfully:
backups/report_20260704_183512.pdf
```

---

## Backup Log

Each successful backup is recorded in `backup.log`.

Example:

```
2026-07-04 18:35:12
Original: /home/user/Documents/report.pdf
Backup: backups/report_20260704_183512.pdf
----------------------------------------
```

---

## How It Works

1. Validates the provided file path.
2. Creates a `backups` folder if it does not already exist.
3. Generates a timestamped filename to prevent overwriting previous backups.
4. Copies the file while preserving metadata using `shutil.copy2()`.
5. Records the backup details in `backup.log`.

---

## Future Improvements

- Restore files from backups
- Compress backups into ZIP archives
- Schedule automatic backups
- Support backing up entire directories
- Allow users to choose a custom backup destination
