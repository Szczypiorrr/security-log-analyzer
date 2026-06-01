from analyzer.parser import parse_log
from analyzer.validator import validate_log
from analyzer.report import generate_report

# Read raw logs
with open("data/logs.txt", "r") as f:
    parsed_logs = []
    validated_logs = []

    # Pass raw logs into parsing
    for log in f:
        parsed_log = parse_log(log)
        if parsed_log:
            parsed_logs.append(parsed_log)

    # Pass parsed logs into validator
    for line in parsed_logs:
        validated_log = validate_log(line)

        if validated_log:
            validated_logs.append(validated_log)
            
    # Generate final report with statistics
    generate_report(validated_logs)
