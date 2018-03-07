# -*- coding: utf-8 -*-
import csv
word = input("enter: ")
word = ''.join(sorted(word))

with open ('PersianWords.csv','r+', encoding='utf-8') as data:
    reader = csv.DictReader(data)
    for row in reader:
        w3 = row['Moins Dictionary']
        w4 = ''.join(sorted(w3))
        if word == w4:
            print (w3)
'''

print word
list = [word[len(word)-1]]
list2 = []
for i in range(0,len(word)-1):
    for element in list:
        for charNum in range(0,len(list[0])+1):
            list2.append(element[:charNum]+word[i]+element[charNum:])
    list = list2
    list2 = []

for w in list:
    print w
    for w2 in list2:
        if w.encode('utf-8') == w2:
            print "w2"
'''

