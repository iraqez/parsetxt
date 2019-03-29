import subprocess, os


filein = '/home/iraqez/PycharmProjects/parsetxt/data/Водички.pdf'
fileout = os.path.abspath(filein).replace('pdf', 'txt')

subprocess.call(['pdftotext', '-layout',  filein, fileout])

