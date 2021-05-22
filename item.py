class item:
    """This class represents an instance of an item in LTTStore.com"""
    def __init__(self, name, link, available):
        self.name = name
        self.link = link
        self.available = available

    def __str__(self):
        return str(self.name) + " is available: "  + str(self.available)
