import argparse
from analyzer.parser import LogParser
from analyzer.reporter import Reporter

def main():
    parser = argparse.ArgumentParser(description="Suspicious Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--json", action="store_true", help="Save JSON report")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")

    args = parser.parse_args()

    print("[*] Reading log file:", args.file)

    # Parse log file
    lp = LogParser(args.file)
    results = lp.parse()

    # Display in terminal
    reporter = Reporter(results)
    reporter.print_console()

    # Output options
    if args.json:
        reporter.save_json()

    if args.html:
        reporter.save_html()


if __name__ == "__main__":
    main()
