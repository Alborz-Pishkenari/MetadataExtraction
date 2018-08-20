# -*- coding: utf8 -*-
import rdflib
from langdetect import detect

naWordsList = ['http:', 'resource', 'fr.dbpedia.org', 'dbpedia.org', 'wikiPageWikiLink', 'property', 'ontology', 'Paris\n', 'Berlin', 'it.dbpedia.org', ]
tempList1 = []
tempList2 = []
langList = []
langDic = {}

##Get data from dataset and prepare it for language detection
##--------------------------------------------------------------------------------------------------
def prepareData(inputSourceName, inputFormatName):
    tempData = open('tempData.txt', 'w')
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT *
                      WHERE {
                                ?s ?p ?o .
                            }
                  """)
    for row in qres:
        tempData.write("%s " % row[0].encode('utf-8'))
        tempData.write("%s " % row[1].encode('utf-8'))
        tempData.write("%s \n" % row[2].encode('utf-8'))
        
    tempData.close()
    msgPrepareData = 'done...'
    print(msgPrepareData)
    return msgPrepareData
##--------------------------------------------------------------------------------------------------


##Detect the language of temporary data file extracted from dataset via SPARQL.
##--------------------------------------------------------------------------------------------------
def detectLanguage(inputTempDatasource):
    with open(inputTempDatasource) as tempFile:
        for line in tempFile:
            line = line.split(' ')
            tempList1.append(line)

    for i in range(0, len(tempList1)):
        for j in range(0, len(tempList1[i])):
            tempList2 = []
            tempList2 = tempList1[i][j].split('/')
            for k in range(0, len(tempList2)):
                try:
                    counter = 0
                    for l in range(0, len(naWordsList)):
                        if(tempList2[k] != naWordsList[l]):
                            counter = counter + 1
                    if(counter == len(naWordsList)):
                        langList.append(detect(tempList2[k]))
##                        print(tempList2[k], ' : ', detect(tempList2[k]))
                except Exception:
                    pass
                
    for word in langList:
        langDic[word] = langDic.get(word, 0) + 1

    sortedLanguageDictionary = sorted(langDic, key = langDic.get, reverse = True)
    
##    print(sortedLanguageDictionary)
    LanguageCode = sortedLanguageDictionary[0]
    return LanguageCode
##--------------------------------------------------------------------------------------------------


##msg = prepareData('itF.ttl', 'ttl')
##LC = detectLanguage('tempData.txt')
