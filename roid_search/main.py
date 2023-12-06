import argparse
import glob

import re
import csv

import textract


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--document_folder', help='Path to your documents',
                        required=True)
    parser.add_argument('--pattern', help='The regex pattern',
                        required=True)
    parser.add_argument('--output_file', help='The name of the output file',
                        required=True)
    return parser.parse_args()


def extract_data(document_folder, pattern):
    extractions = []
    for document in glob.glob(document_folder):
        document_text = textract.process(document)
        extractions.extend(extract(document_text, pattern, document))
    return extractions


def extract(document_text, pattern, source):
    return [{'match': match, 'source': source}
            for match in re.findall(pattern, document_text)]


def dump_to_file(extractions, output_file):
    with open(f'{output_file}.tsv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['match', 'source'],
                                dialect='excel-tab')
        writer.writeheader()
        writer.writerows(extractions)


def main():
    args = parse_args()
    extractions = extract_data(args.document_folder, args.pattern)
    dump_to_file(extractions, args.output_file)


if __name__ == '__main__':
    main()
