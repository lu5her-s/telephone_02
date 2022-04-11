import csv

NAME, EXISTS = 'name', 'Exists'

# Read old data from file to list
with open('02_tel.csv', 'r') as inp:
    reader = csv.DictReader(inp)
    inputs = list(reader)

# Update input row that name match
with open('edit.csv', 'r') as sea:
    sea_reader = csv.DictReader(sea)
    for row in sea_reader:
        name = row[NAME]
        for input_ in inputs:
            if input_[NAME] == name and row['note']:
                input_['note'] = row['note']
                break

# Write update 02_tel.csv data out in to a file
with open('update.csv', 'w') as outp:
    fieldnames = inputs[0].keys()
    writer = csv.DictWriter(outp, fieldnames)
    writer.writeheader()
    writer.writerows(inputs)

print('done')
