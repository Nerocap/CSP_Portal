

class XpsDevice:
    def __init__(self):
        self.connection = None
        pass

    def get_status(self):
        self.connection = True
        return self.connection