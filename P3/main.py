class NumberStats:
    def __init__(self, filename):
        self.filename = filename
class NumberStats:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers
