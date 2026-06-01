import re
from models.log_entry import LogEntry

VALID_STATUS = {"SUCCESS", "FAIL"}
IP_PATTERN = r"^\d{1,3}(\.\d{1,3}){3}$"

TIMESTAMP_PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

def validate_log(log: LogEntry):
    
    if log is None:
        return None

    if log.status not in VALID_STATUS:
        return None
    
    if not re.match(IP_PATTERN, log.ip):
        return None
    
    if not re.match(TIMESTAMP_PATTERN, log.timestamp):
        return None
    
    return log