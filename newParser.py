import subprocess, os, tempfile

file = '/home/iraqez/PycharmProjects/parsetxt/data/Водички.pdf'

def toTxt(file):
    # filein = '/home/iraqez/PycharmProjects/parsetxt/data/Водички.pdf'
    filein = file
    fileout = os.path.abspath(filein).replace('pdf', 'txt')
    # fileout = tempfile.TemporaryFile()
    subprocess.call(['pdftotext', '-layout',  filein, fileout])
    f = open(fileout)
    f = f.read()
    os.remove(fileout)
    return f
