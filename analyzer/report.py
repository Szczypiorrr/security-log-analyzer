def generate_report(logs):
    with open("reports/report.txt", "w") as f:
        f.write("========= LOG REPORT =========\n\n")

        f.write(f"Total logs: {len(logs)}\n\n")

        success = 0
        fail = 0
        for log in logs:
            if log.status == "SUCCESS":
                success += 1
            else:
                fail += 1

        f.write(f"SUCCESS: {success}\n")
        f.write(f"FAIL: {fail}\n")