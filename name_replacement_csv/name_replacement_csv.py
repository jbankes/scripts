#!/usr/bin/python3
import os
import csv
import argparse

# preferred names two tuple
preferred_names = {
            ('Some', 'Person'): ('Some', 'Person'),
            ('Some', 'Person'): ('Some', 'Person')
        }

# Read file name from commandline
parser = argparse.ArgumentParser(description='Format names for transfer between programs.')
parser.add_argument('filename', metavar='csv_filename', help='Filename to format')
args = parser.parse_args()

# set file names
print(f'Pulling in original file: {args.filename}') 
filename = os.path.splitext(args.filename)[0]
new_filename = filename + '-formatted.csv'
print(f'Updated names will be in: {new_filename}')
print('-------------------------------------------------------------------')

# Read CSV file and augment names
with open(args.filename) as csv_file:
    with open(new_filename, 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter=',')
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                row.pop(0)
                titles = ['lastname','firstname']
                row = titles + row
                csv_writer.writerow(row)
                line_count += 1
            else:
                split_name = row[0].split()
                first_last = row.pop(0)
                name = first_last.split()
                if (name[0], name[1]) in preferred_names:
                    preferred_name = preferred_names[(name[0], name[1])]
                    row = [preferred_name[1],preferred_name[0]] + row
                else:
                    row = [name[1],name[0]] + row
                csv_writer.writerow(row)
                line_count += 1
        print(f'Adjust {line_count} lines.')
