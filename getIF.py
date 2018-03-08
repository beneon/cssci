import csv,os,sys,pyperclip,time,re
searchWord = sys.argv[1]
print(searchWord)
fuzzyWord = re.compile(searchWord+'.*')
dataFile = open('journalscore.csv')
abbrevFile = open('abbrev.csv')

dataReader = csv.reader(dataFile)
abbrevReader = csv.reader(abbrevFile)

dictData = {}
dictAbbrev = {}
for row in dataReader:
    dictData[row[0]]=row[1]
for row in abbrevReader:
    dictAbbrev[row[0]]=row[1]

if searchWord in dictData:
    pyperclip.copy(dictData[searchWord])
elif searchWord in dictAbbrev:
    pyperclip.copy(dictData[dictAbbrev[searchWord]])
else:
    swSuggestion = []
    for e in dictData:
        if fuzzyWord.search(e)!=None:
            swSuggestion.append('journal:%s,IF:%s'%(e,dictData[e]))
    for e in dictAbbrev:
        if fuzzyWord.search(e) != None:
            swSuggestion.append('abbrev:%s,full%s'%(e,dictAbbrev[e]))
    print('\n'.join(swSuggestion))
    time.sleep(60)
