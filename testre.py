#! /usr/bin/python
# -*- coding: utf-8 -*-

def zapis(s):
    dataX = {}
    s = s
    reesNum = ['Реєстраційний номероб’єкта нерухомогомайна:', 'Об’єкт нерухомогомайна:', 'reesNum']
    objectMajno = ['Об’єкт нерухомогомайна:', 'Кадастровий номер:', 'objectMajno']
    kadNum = ['Кадастровий номер:', 'Опис об’єкта:Площа (га): ', 'kadNum']
    ploscha = ['Опис об’єкта:Площа (га): ', 'Цільове призначення:', 'ploscha']
    cilPr = ['Цільове призначення:', 'Адреса:', 'cilPr']
    adress = ['Адреса:', 'Актуальна інформація про державну реєстрацію іншого речового права', 'adress']
    zapysNum = ['Номер запису про інше речове право: ', 'Дата, час державноїреєстрації:', 'zapysNum']
    date = ['Дата, час державноїреєстрації:', 'Державний реєстратор:', 'date']
    derzhReestrator = ['Державний реєстратор:', 'Підстава виникненняіншого речового права:', 'derzhReestrator']
    vynykPravo = ['Підстава виникненняіншого речового права:', 'Підстава внесеннязапису:', 'vynykPravo']
    vnesZap = ['Підстава внесеннязапису:', 'Вид іншого речовогоправа:', 'vnesZap']
    vidPrava = ['Вид іншого речовогоправа:', 'Зміст, характеристикаіншого речового права:', 'vidPrava']
    strokDiy = ['Строк дії: ', 'Відомості про суб’єктаіншого речового права:', 'strokDiy']
    orendar = ['Орендар: ', ', код ЄДРПОУ: ', 'orendar']
    edrpu = ['код ЄДРПОУ: ', ' Орендодавець:', 'edrpu']
    orendodavets = ['Орендодавець: ', 'Опис об’єкта іншогоречового права:', 'orendodavets']
    opys = ['Опис об’єкта іншогоречового права:', '', 'opys']


    allParams = [reesNum, objectMajno, kadNum, ploscha, cilPr, adress, zapysNum, date,
                 derzhReestrator, vynykPravo, vnesZap, vidPrava, strokDiy, orendar,
                 edrpu, orendodavets, opys]

    def ret(s, start, end, dname):
        res = (s[s.find(start)+len(start):s.rfind(end)])
        d = {dname: res}
        dataX.update(d)

    for i in allParams:
        ret(s, i[0], i[1], i[2])

    return dataX

if __name__ == '__main__':
    print(zapis(s))
