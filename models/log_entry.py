class LogEntry():
    """
    Represents a single parsed log entry
    """

    def __init__(self, timestamp, name, status, ip):
        self.timestamp = timestamp
        self.name = name
        self.status = status
        self.ip = ip

    def __repr__(self):
        return f"{self.timestamp} | {self.name} | {self.status} | {self.ip}"
