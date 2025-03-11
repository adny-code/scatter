import csv
from datetime import datetime
import os

abs_work_space = os.getcwd()
filename1 = os.path.join(abs_work_space, "rsc", "50100.csv")
filename2 = os.path.join(abs_work_space, "rsc", "50100C.csv")
filename3 = os.path.join(abs_work_space, "rsc", "50100L.csv")

"""
change two-dimension pattern into one-dimension index

0 1 0
1 0 1   ==>  [1 3 5 7】
0 1 0
"""
def sahpe_to_line(file):
    filename = file
    wordinline = []
    with open(filename, 'r', encoding='UTF-8') as file_obj:
        reader = csv.reader(file_obj)
        cout = 0
        for row in reader:
            for num in row:
                if(num == '1'):
                    wordinline.append(cout)
                cout += 1
        file_obj.close()
    return wordinline
