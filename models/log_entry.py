class LogEntry():
    def __init__(self, name, status, ip):
        self.name = name
        self.status = status
        self.ip = ip

    def __repr__(self):
        return f"{self.name} | {self.status} | {self.ip}"
