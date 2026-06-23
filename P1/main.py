class NumberSeparator:
    def __init__(self, source_file):
        self.source_file = source_file
class NumberSeparator:
    def __init__(self, source_file):
        self.source_file = source_file

    def read_numbers(self):
        with open(self.source_file, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers
class NumberSeparator:
    def __init__(self, source_file):
        self.source_file = source_file

    def read_numbers(self):
        with open(self.source_file, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def separate_numbers(self):
        numbers = self.read_numbers()
        even_nums = [str(n) for n in numbers if n % 2 == 0]
        odd_nums = [str(n) for n in numbers if n % 2 != 0]

        with open('even.txt', 'w') as even_file:
            even_file.write('\n'.join(even_nums))
        with open('odd.txt', 'w') as odd_file:
            odd_file.write('\n'.join(odd_nums))
