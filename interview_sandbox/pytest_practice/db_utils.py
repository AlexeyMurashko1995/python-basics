class DatabaseConnection():
    def __init__(self):
        self.is_connected = False

    def connect(self):
        self.is_connected = True

    def disconnect(self):
        self.is_connected = False