```markdown
# 🔍 Log Analyzer for Suspicious Activity
A lightweight **web security log analysis tool** that scans Apache/Nginx access logs for suspicious activity such as **SQL Injection, XSS, Path Traversal, Command Injection, Brute Force attacks**, and more.

This tool is perfect for:
- Cybersecurity students
- Portfolio projects
- Bug bounty hunters
- DFIR beginners
- System administrators

---

## 🚀 Features

- Detects common attack patterns:
  - SQL Injection  
  - XSS  
  - Path Traversal  
  - File Inclusion  
  - Command Injection  
  - Bruteforce / Sensitive Endpoint Scanning  
- Easy command-line interface  
- JSON and HTML report generation  
- Clean project structure  
- Works with real Apache/Nginx logs  
- Beginner friendly

---


## 🔧 Installation

```bash
git clone https://github.com/MohidRizwan/log-analyzer.git
cd log-analyzer

pip install -r requirements.txt
````

---

## 🖥 Usage

### Basic Scan

```bash
python3 main.py --file logs/access.log
```

### Save JSON Report

```bash
python3 main.py --file logs/access.log --json
```

### Generate HTML Report

```bash
python3 main.py --file logs/access.log --html
```

### Both at once:

```bash
python3 main.py --file logs/access.log --json --html
```

---

## 📊 Sample Output (Terminal)

```
=== Suspicious Activity Detected ===

[!] SQL Injection
    IP:        192.168.10.2
    Time:      12/Feb/2025:10:14:23 +0000
    Request:   GET /index.php?id=1 UNION SELECT 1,2 --
-----------------------------------------
```

---

## 📌 Example HTML Report

> A clean, readable table of all suspicious requests (screenshot recommended!)

Place your screenshot here when you run the project:

```
![Report Screenshot](images/report.png)
```

---

## 🧩 How It Works

1. Reads each log line
2. Extracts IP, timestamp, HTTP request
3. Checks each line against regex signatures
4. Groups results by attack category
5. Outputs report in terminal, JSON, or HTML

---

## 🛠 Extend It

You can add:

* More regex patterns
* GeoIP lookup (IP → country)
* Discord/Telegram alert webhook
* Visualization charts
* Machine learning anomaly detection

---

## 📜 License

MIT License — free to use, modify, and share.

---
