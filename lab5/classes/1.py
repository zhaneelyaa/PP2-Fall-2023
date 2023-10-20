class StringManipulator:
    def __init__(self, string):
        self.string = string

    def getString(self):
        self.string = input(" ")

    def printString(self):
        print(self.string.upper())


s = StringManipulator("")

s.getString()
s.printString()
