import re
from models.log_entry import LogEntry

VALID_STATUS = {"SUCCESS", "FAIL"}

# Strick IPv4 validation pattern
IP_PATTERN = r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

TIMESTAMP_PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

def validate_log(log: LogEntry):
    
    if log is None:
        return None

    # Status must be SUCCESS or FAIL
    if log.status not in VALID_STATUS:
        return None
    
    # IP must match IPv4 pattern
    if not re.match(IP_PATTERN, log.ip):
        return None
    
    # Timestamp must match expected format
    if not re.match(TIMESTAMP_PATTERN, log.timestamp):
        return None
    
    return log