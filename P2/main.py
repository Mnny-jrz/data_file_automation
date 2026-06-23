class StudentGWA:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        """Reads student names and GWA values from a text file."""
        with open(self.filename, 'r') as file:
            data = [line.strip().split() for line in file.readlines()]
        return data

    def find_highest_gwa(self):
        """Finds the student with the highest GWA (lowest number)."""
        data = self.read_data()
        # Filter out malformed or empty lines
        valid_data = [entry for entry in data if len(entry) == 2]
        if not valid_data:
            print("⚠️ No valid student data found.")
            return None
        top_student = min(valid_data, key=lambda x: float(x[1]))
        return top_student


if __name__ == "__main__":
    gwa_checker = StudentGWA('students.txt')
    result = gwa_checker.find_highest_gwa()
    if result:
        student, gwa = result
        print(f"🏆 Highest GWA: {student} ({gwa})")

