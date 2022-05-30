import csv

PATH = './dataset/gl_entries_id.csv'


def load_data(path: str = PATH):
    with open(path, 'r') as file:
        data = csv.reader(file)
        next(data, None)
        for line in data:
            yield int(line[0])
