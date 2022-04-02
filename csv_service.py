import csv
# class for creating a student
# will have to change based on the format of canvas data (what gets passed in).
class CsvDataPoint:
    def __init__(self, first, last, bday) -> None:
        self.first = first
        self.last = last
        self.bday = bday
    
# csv_service, reads a CSV file from data.
class csv_service:
    def __init__(self, filename):
        self.filename = filename
    
    # Getter from the fileName.
    # Returns a list of objects of classtype CsvDataPoint.
    def get_from_csv(self):
        students_from_csv = [] # empty list of students.
    
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            reader.__next__() #skip headers.
            for row in reader:
                students_from_csv.append(CsvDataPoint(row[0], row[1], row[2]))

        return students_from_csv