import re

# Suspicious regex signatures for common web attacks
PATTERNS = {
    "SQL Injection": [
        re.compile(r"(union(\s+all)?\s+select)", re.IGNORECASE),
        re.compile(r"(\bor\b\s+1=1)", re.IGNORECASE),
        re.compile(r"('|\")\s*or\s*('|\")", re.IGNORECASE),
        re.compile(r"(--|#)"),  # SQL comment indicators
    ],

    "XSS Attempt": [
        re.compile(r"(<script>.*?</script>)", re.IGNORECASE),
        re.compile(r"(<.*?on\w+=)", re.IGNORECASE),
        re.compile(r"(javascript:)", re.IGNORECASE),
    ],

    "Path Traversal": [
        re.compile(r"(\.\./|\.\.\\)"),
    ],

    "File Inclusion": [
        re.compile(r"(php://|data://|expect://)", re.IGNORECASE),
    ],

    "Command Injection": [
        re.compile(r"(;|\|\||&&)\s*\w+", re.IGNORECASE),
    ],

    "Bruteforce / Scanning": [
        re.compile(r"(wp-login\.php)"),         # Common WordPress brute force
        re.compile(r"(xmlrpc\.php)"),           # WP brute force
        re.compile(r"(/\.git/|/\.env)"),        # Sensitive file probing
        re.compile(r"(admin|login|signin)"),    # High-value endpoints
    ],
}
