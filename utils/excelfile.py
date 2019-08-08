import os
import csv
import sys

def get_from_csv(filename):
    list = []
    # dirname, runname = os.path.split(os.path.abspath(__file__))
    # filename = dirname + filename
    with open(filename, 'r', newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        print("CSV Reader: READING CSV FILE >>", filename)
        try:
            for row in reader:
                for q in row:
                    if q == None or len(q) == 0:
                        pass
                    else:
                        list.append(q)
            print("CSV Reader: FINISHED READING CSV FILE =>", filename)
            return list
        except csv.Error as i:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, i))
            return None
        except EOFError as e:
            print("Can not read file CSV:", filename)
            print("System error:", e)
            return None

def get_absolute_filename(filename):
    dirname, runname = os.path.split(os.path.abspath(__file__))
    filename = dirname + filename
    return filename