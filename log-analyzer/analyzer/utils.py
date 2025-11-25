import re

# Extract IP from common log formats
def extract_ip(line):
    match = re.match(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
    return match.group(1) if match else "Unknown"

# Extract timestamp from log line
def extract_timestamp(line):
    match = re.search(r"\[(.*?)\]", line)
    return match.group(1) if match else "Unknown"

# Extract request part: GET /index.php?id=1 HTTP/1.1
def extract_request(line):
    match = re.search(r"\"(GET|POST|HEAD|PUT|DELETE|OPTIONS|PATCH).*?\"", line)
    return match.group(0).strip('"') if match else None
