#!/usr/bin/python3
import os
import csv
import argparse

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
    print(f'Reading {args.filename}')
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            split_name = row[0].split()
            print(f'{row[0]} will save as \'{split_name[1]},{split_name[0]}\'')
            line_count += 1
    print(f'Read {line_count} lines.')

#  with open(new_filename, 'w', newline='') as csv_file:
#      csv_writer = csv.writer(new_filename, delimiter=',')
