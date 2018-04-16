import csv
write = []
with open('NAPA.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row = str(row)
        row = row.strip()
        sep = "/"
        row = row.split(sep, 1)[0]
        if(row != " " and row != "0"):
           write.append(row) 
           #print(row)
        
writer = csv.writer(open("NAPA.csv", "w"), delimiter=",", lineterminator="\n")
for x in write:
    if(x != "[]" and x != "['0']" and x != "[' ']"):
        x = x.replace("[","")
        x = x.replace("]", "")
        x = x.replace("'", "")
        writer.writerow([x])     
        print(x)
        