class StudentGWA:
    def __init__(self, filename):
        self.filename = filename
class StudentGWA:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            data = [line.strip().split() for line in file.readlines()]
        return data
