#! /usr/bin/python
# -*- coding: utf-8 -*-

def zapis(s):
    dataX = {}
    s = s

    reesNum = ['Реєстраційний номер      ', '\nоб’єкта нерухомого', 'Номер запису']
    address = ['Адреса:                  ', '\n\n                       Актуальна', 'Сільрада']
    kadnum = ['Kадастровий номер:       ', '\nОпис об’єкта', 'Кадастровий номер']


    allParams = [reesNum, address, kadnum]

    def ret(s, start, end, dname):
        if s.find(start) == -1:
            res = None
        else:
            res = (s[s.find(start)+len(start):s.rfind(end)])
        d = {dname: res}
        dataX.update(d)

    for i in allParams:
        ret(s, i[0], i[1], i[2])

    return dataX

if __name__ == '__main__':
    print(zapis(s))
