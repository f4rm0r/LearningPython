from csv import reader
def load_csv(filename):
    file = open(filename,"r", newline='')
    lines = reader(file)
    data = list(lines)
    return data


file_path = "test_import.csv"
dataset = load_csv(file_path)
print(dataset)

#with open('test_import.csv', newline='') as csvfile:
#    dataset = csv.reader(csvfile, delimiter= ' ', quotechar='|')

#print(dataset)