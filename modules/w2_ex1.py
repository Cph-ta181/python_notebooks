import sys
import argparse

parser= argparse.ArgumentParser(description='A program that reads .csv files as a list and prints said list')
parser.add_argument('csv', help='Location, name, and extension of file')
parser.add_argument('--file', help='Location of file to write to')


def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()
        return contents

def write_list_to_file(output_file, *line):
    with open(output_file, 'w') as file_object:
        for lines in line:
            file_object.write(str(lines))

def read_csv(input_file):
    print(input_file)
    values = []
    with open(input_file) as file_object:
        content = file_object.readlines()
    for line in content:
        values.append(line)
    return values

if __name__ == '__main__':
    args = parser.parse_args()
    if args.file == None:
        print(read_csv(args.csv))
    else:
        write_list_to_file(args.file, read_csv(args.csv))

