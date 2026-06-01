from models.log_entry import LogEntry

def parse_log(line):

    # Parse raw log line into structured data
    slowa = [p.strip() for p in line.split("|")]

    # Invalid logs must contain exactly 4 fields
    if len(slowa) != 4:
        return None
    
    # Create LogEntry object from parsed values
    timestamp, name, status, ip = slowa
    return LogEntry(timestamp, name, status, ip)
