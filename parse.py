import argparse
import csv
import importlib


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Mongoose Item Text File Parser')
    arg_parser.add_argument('type')
    arg_parser.add_argument('filename')
    arg_parser.add_argument('csvfilename')
    args = arg_parser.parse_args()
    item_parser = importlib.import_module(f'parsers.{args.type}')
    with open(args.csvfilename, 'wt', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(item_parser.columns())
        with open(args.filename, 'rt') as items:
            for line in items:
                line = line.strip()
                item = item_parser.parse(line)
                writer.writerow(item)

