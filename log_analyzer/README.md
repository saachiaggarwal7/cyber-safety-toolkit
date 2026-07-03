# Log Analyzer

A Python-based security log analyzer that summarizes log files, searches for keywords, detects failed login attempts, and generates a security report.

---

## Features

- Validates log file paths
- Counts total log entries
- Counts `ERROR`, `WARNING`, and `INFO` messages
- Performs case-insensitive keyword searches
- Detects failed login attempts
- Counts failed login attempts by source IP
- Generates a security report (`report.txt`)

---

## Technologies Used

- Python
- `os`
- `collections.defaultdict`

---

## Project Structure

```
log-analyzer/
│
├── log_analyzer.py
├── sample.txt
├── report.txt
└── README.md
```

---

## Example

### Input

```
Enter file path: sample.txt
Enter keyword to search: failed
```

### Output

```
Total Lines: 150
Total ERROR messages: 8
Total WARNING messages: 15
Total INFO messages: 127

Found 6 matching lines.

Failed Login Attempts by IP:
192.168.1.20 : 4
10.0.0.5 : 2

Security report saved as report.txt
```

---

## Security Report

The generated `report.txt` includes:

- Log summary
- Keyword search results
- Failed login attempts grouped by IP address

---

## Future Improvements

- Export reports in JSON format
- Display top source IPs
- Detect brute-force attacks
- Support Apache and Nginx logs
- Filter logs by severity
