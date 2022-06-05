from unicodedata import name


class Node:
    def __init__(self, id, nameStreet):
        self.id = id
        self.nameStreet = nameStreet
    def getId(self):
        return self.id
    def getNameStreet(self):
        return self.nameStreet
