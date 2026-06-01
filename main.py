from analyzer.parser import parser
from analyzer.validator import validate_log
from analyzer.report import generate_report

with open("data/logs.txt", "r") as f:
    parsed_logs = []
    validated_logs = []

    for log in f:
        parsed_log = parser(log)
        if parsed_log:
            parsed_logs.append(parsed_log)


    for line in parsed_logs:
        validated_log = validate_log(line)

        if validated_log:
            validated_logs.append(validated_log)
            
    print(validated_logs)
    generate_report(validated_logs)
