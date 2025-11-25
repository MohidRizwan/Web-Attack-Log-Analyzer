import re
from analyzer.patterns import PATTERNS
from analyzer.utils import extract_ip, extract_request, extract_timestamp

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.results = []

    def parse(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    self._analyze_line(line.strip())
        except FileNotFoundError:
            print(f"[!] File not found: {self.filepath}")

        return self.results

    def _analyze_line(self, line):
        ip = extract_ip(line)
        request = extract_request(line)
        timestamp = extract_timestamp(line)

        if not request:
            return

        for attack_type, pattern_list in PATTERNS.items():
            for pattern in pattern_list:
                if pattern.search(line):
                    self.results.append({
                        "ip": ip,
                        "timestamp": timestamp,
                        "attack_type": attack_type,
                        "request": request,
                        "raw_line": line
                    })
                    return  # Stop after first match to avoid duplicates
