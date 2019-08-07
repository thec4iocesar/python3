#!/usr/bin/python3.7

import csv

with open('arquivo.csv', 'w', newline = '') as arq:
    arquivo = csv.writer(arq, delimiter = ',')
    arquivo.writerow(['teste'] * 5)