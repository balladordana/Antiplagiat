import argparse
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


parser = argparse.ArgumentParser()
parser.add_argument("input_text", help="File with list of document's pairs")
parser.add_argument("output", help="Path to output file")
args = parser.parse_args()

try:
    input_file = open(args.input_text)
    f = input_file.read().splitlines()
    out = open(args.output, 'w')

    for i in range(len(f)):
        files = f[i].split(' ')
        try:
            f1 = open(files[0])
            f2 = open(files[1])

            out.write(str(round(similar(f1.read(), f2.read()), 3)) + '\n')
            f1.close()
            f2.close()
        except Exception as e:
            print(e)
    input_file.close()
    out.close()
except Exception as e:
    print(e)
