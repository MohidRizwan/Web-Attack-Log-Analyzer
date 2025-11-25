import json
import os

class Reporter:
    def __init__(self, results):
        self.results = results

    def print_console(self):
        if not self.results:
            print("[✓] No suspicious activity detected.")
            return

        print("\n=== Suspicious Activity Detected ===\n")
        for r in self.results:
            print(f"[!] {r['attack_type']}")
            print(f"    IP:        {r['ip']}")
            print(f"    Time:      {r['timestamp']}")
            print(f"    Request:   {r['request']}")
            print(f"    Raw Line:  {r['raw_line']}")
            print("-----------------------------------------")

    def save_json(self, filepath="output/suspicious.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=4)

        print(f"[+] JSON report saved to {filepath}")

    def save_html(self, filepath="output/report.html"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        html_content = """
        <html>
        <head>
            <title>Suspicious Log Report</title>
            <style>
                body { font-family: Arial; background: #f4f4f4; padding: 20px; }
                table { width: 100%; border-collapse: collapse; background: white; }
                th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
                th { background: #333; color: white; }
                tr:nth-child(even) { background: #eee; }
            </style>
        </head>
        <body>
            <h2>Suspicious Activity Report</h2>
            <table>
            <tr><th>IP</th><th>Time</th><th>Attack</th><th>Request</th></tr>
        """

        for r in self.results:
            html_content += f"""
            <tr>
                <td>{r['ip']}</td>
                <td>{r['timestamp']}</td>
                <td>{r['attack_type']}</td>
                <td>{r['request']}</td>
            </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"[+] HTML report generated at {filepath}")
