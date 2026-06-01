from models.log_entry import LogEntry

def parser(line):
    slowa = [p.strip() for p in line.split("|")]

    if len(slowa) != 4:
        return None
    
    timestamp, name, status, ip = slowa
    return LogEntry(timestamp, name, status, ip)
