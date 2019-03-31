import re

from exportPdf import extract_text_from_pdf
from testre import zapis
from newParser import toTxt
import pandas as pd
import os

file = '/home/iraqez/PycharmProjects/parsetxt/data/obolon.pdf'
name = os.path.basename(file).replace('pdf', 'xlsx')

def dataFrames(file):
    datatxt = toTxt(file)
    unsorted_list = []
    # file_obj = open('./data/1.txt', 'rt')
    frame = datatxt
    res = re.split('Актуальна інформація про об’єкт нерухомого майна', frame)[1:-1]
    return res

def toPd(xxx):
    df = pd.DataFrame()
    data = dataFrames(xxx)
    for i in data:
        df = df.append(zapis(i), ignore_index=True)
    df.to_excel('data/'+name)


if __name__ == '__main__':
    toPd(file)
