class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_duplicates(self):
        numbers = self.read_numbers()
        duplicates = set([n for n in numbers if numbers.count(n) > 1])
        return duplicates

    def most_frequent(self):
        numbers = self.read_numbers()
        return max(set(numbers), key=numbers.count)
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_duplicates(self):
        numbers = self.read_numbers()
        duplicates = set([n for n in numbers if numbers.count(n) > 1])
        return duplicates

    def most_frequent(self):
        numbers = self.read_numbers()
        return max(set(numbers), key=numbers.count)

    def highest_number(self):
        numbers = self.read_numbers()
        return max(numbers)

    def sort_descending(self):
        numbers = self.read_numbers()
        return sorted(numbers, reverse=True)

    def average(self):
        numbers = self.read_numbers()
        return sum(numbers) / len(numbers)
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_duplicates(self):
        numbers = self.read_numbers()
        duplicates = set([n for n in numbers if numbers.count(n) > 1])
        return duplicates

    def most_frequent(self):
        numbers = self.read_numbers()
        return max(set(numbers), key=numbers.count)

    def highest_number(self):
        numbers = self.read_numbers()
        return max(numbers)

    def sort_descending(self):
        numbers = self.read_numbers()
        return sorted(numbers, reverse=True)

    def average(self):
        numbers = self.read_numbers()
        return sum(numbers) / len(numbers)


if __name__ == "__main__":
    processor = NumberProcessor('numbers.txt')
    print(f"🔁 Duplicates: {processor.find_duplicates()}")
    print(f"📊 Most frequent: {processor.most_frequent()}")
    print(f"⬆️ Highest number: {processor.highest_number()}")
    print(f"📉 Sorted descending: {processor.sort_descending()}")
    print(f"➗ Average: {processor.average():.2f}")
