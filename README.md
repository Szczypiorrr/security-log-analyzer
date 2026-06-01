# security-log-analyzer
A simple Python project for parsing, validating, and generating reports from raw log data.

The goal of this project is to demonstrate basic data/backend processing skills in Python, including file handling, data validation and modular project structure.

## ⚙️ How to run

### 1. Clone repository
```bash
git clone https://github.com/Szczypiorrr/security-log-analyzer.git
cd security-log-analyzer
```
### 2. Run project
```bash
python main.py
```

## 📌 Features

- Parses raw log entries from a text file
- Validates log structure (timestamp, status, IP, name)
- Filters out invalid logs
- Generates summary report with statistics
- Modular architecture

## 🧱 Project structure
```text
security-log-analyzer/
│
├── main.py # Entry point of the application
│
├── analyzer/
│   ├── parser.py # Parses raw log lines into objects
│   ├── validator.py # Validates parsed logs
│   └── report.py # Generates summary reports
│
├── models/
│   └── log_entry.py # LogEntry data model
│
├── data/
│   └── logs.txt # Sample input logs
│
├── reports/
│   └── report.txt # Generated output report
│
├── requirements.txt 
│
└── README.md
```

## 🚀 Technologies

- Python 3.12
- Git/GitHub
- Regular Expressions (re module)
- File handling
- OOP

## 📊 Example output
```text
========= LOG REPORT =========

Total logs: 7

SUCCESS: 4
FAIL: 3
```

## 🧠 What I learned?

- Working with files in Python
- Data parsing and validation
- Regular expressions
- Object-oriented programming
- Project structuring

## 🔧 Possible improvements

- Add CLI interface
- Support additional log formats
- Improve error handling for malformed log lines
- Export report to JSON or CSV format

# 👤 Author

Created by Szczypiorrrr  
🔗 GitHub: https://github.com/Szczypiorrr