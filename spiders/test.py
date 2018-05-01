import csv
writer = []
with open('NAPA.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            row = str(row)
            writer.append(row)
for x in writer:
    x = x[2:-2]
    print(x)