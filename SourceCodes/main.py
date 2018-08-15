# -*- encoding: utf-8 -*-
import rdflib
from langdetect import detect
import shutil
from collections import OrderedDict
from dataClassDiscovery import retrieveDistinctClasses
from dataClassDiscovery import countAndRateSubjects
from dataClassDiscovery import countAndRatePredicates
from dataClassDiscovery import countAndRateObjects
from dataClassDiscovery import fetchDataToList
from dataClassDiscovery import extractNumberOfInstancesPerClass
from dataClassDiscovery import getNumberOfDistinctSubjects
from dataClassDiscovery import getNumberOfDistinctObjects
from dataClassDiscovery import getNumberOfDistinctPredicates
from dataClassDiscovery import getNumberOfTripples
from dataPropertyDiscovery import retrieveDistinctProperties
from geodataDiscovery import discoverLatitudinalLongitudinalData
from setMetadataProperties import initializingMetadataFile
from estimateDataset import extractDatasetFeature
from datasetLanguageDetection import prepareData
from datasetLanguageDetection import detectLanguage

lst = []
start = '<'
end = '>'
s2 = ''
currentDatasetNumber = 1
triplesOldValue = 'void:triples'
distinctObjectsOldValue = 'void:distinctObjects'
distinctSubjectsOldValue = 'void:distinctSubjects'
distinctPropertiesOldValue = 'void:properties'
distinctClassesOldValue = 'void:classes'
oldKeywords = 'dcat:keyword'
entitiesOldValue = 'void:entities'
oldFeature = 'void:feature'
featureBase = 'http://www.w3.org/ns/formats/'
oldLanguage = 'dct:language'
oldDocuments = 'void:documents'
languageBase = 'http://id.loc.gov/vocabulary/iso639-1/'
oldDatasetName = ':datasetName'
newKeywords = ''
TestnewKeywords = ''

shutil.copy("C:/Python27/MasterThesis/DatasetDiscovery/templates/m1.ttl", "C:/Python27/MasterThesis/DatasetDiscovery/templates/m2.ttl")

datasetName = raw_input('Dataset Name: ')
##datasetFormat = raw_input('Dataset Format: ')
print
print
storeNameExtension = datasetName.split('.')
datasetFormat = storeNameExtension[1]

listDistinctClasses = retrieveDistinctClasses(datasetName, datasetFormat)
print('----------Results from retrieveDistinctClasses----------')
for i in range(0, len(listDistinctClasses)):
    print(listDistinctClasses[i])
print(len(listDistinctClasses))
distinctClassesNewValue = 'void:classes ' + str(len(listDistinctClasses))
distinctClassesMSG = initializingMetadataFile(distinctClassesOldValue, distinctClassesNewValue)
print(100*'-')
print


dicCountSubjects = countAndRateSubjects(datasetName, datasetFormat)
print('----------Results from countAndRateSubjects----------')
sortedDicCountSubjects = OrderedDict(sorted(dicCountSubjects.items(), reverse = True, key = lambda x: x[1]))
subjectSecondaryList = []
for k, v in sortedDicCountSubjects.iteritems():
    print(k, v)
    subjectPrimaryList = []
    subjectPrimaryList.append(k.rsplit('/'))
    subjectSecondaryList.append(subjectPrimaryList[0][-1])
   
for i in range(0, 5):
    if(i < 3):
        newKeywords = newKeywords + '"' + subjectSecondaryList[i] + '", '
    elif(i == 3):
        newKeywords = newKeywords + '"' + subjectSecondaryList[i] + '"'
    print(subjectSecondaryList[i])
    
print(newKeywords)
newKeywords = 'dcat:keyword ' + newKeywords
keywordsMSG = initializingMetadataFile(oldKeywords, newKeywords)
print(100*'-')
print


dicCountPredicates = countAndRatePredicates(datasetName, datasetFormat)
print('----------Results from countAndRatePredicates----------')
sortedDicCountPredicates = OrderedDict(sorted(dicCountPredicates.items(), reverse = True, key = lambda x: x[1]))
predicateSecondaryList = []
for k, v in sortedDicCountPredicates.iteritems():
    print(k, v)
    predicatePrimaryList = []
    predicatePrimaryList.append(k.rsplit('/'))
    predicateSecondaryList.append(predicatePrimaryList[0][-1])

print(len(predicateSecondaryList))
for i in range(0, 2):
    print(predicateSecondaryList[i])
print(100*'-')
print


dicCountObjects = countAndRateObjects(datasetName, datasetFormat)
sortedDicCountObjects = OrderedDict(sorted(dicCountObjects.items(), reverse = True, key = lambda x: x[1]))
print('----------Results from countAndRateObjects----------')
objectSecondaryList = []
for k, v in sortedDicCountObjects.iteritems():
    print(k, v)
    objectPrimaryList = []
    objectPrimaryList.append(k.rsplit('/'))
    objectSecondaryList.append(objectPrimaryList[0][-1])
    
for i in range(0, 5):
    print(objectSecondaryList[i])
print(100*'-')
print


tempEntityList = subjectSecondaryList + predicateSecondaryList + objectSecondaryList
print('???????????????????')
print(len(tempEntityList))
entityList = list(OrderedDict.fromkeys(tempEntityList))
print(len(entityList))
print('???????????????????')
entitiesNewValue = 'void:entities ' + str(len(entityList))
entitiesMSG = initializingMetadataFile(entitiesOldValue, entitiesNewValue)


######tempLST = list(set(fetchDataToList(datasetName, datasetFormat)))
####
####print('----------Results from extractNumberOfInstancesPerClass----------')
####for i in range(0, len(tempLST)):
####    s2 = extractNumberOfInstancesPerClass(datasetName, datasetFormat, start + tempLST[i] + end)
####    if (s2 != '0'):
####        print(start + tempLST[i] + end)
####        print(s2)
####print(100*'-')
####print
####
####
listDistinctProperties = retrieveDistinctProperties(datasetName, datasetFormat)
print('----------Results from retrieveDistinctProperties----------')
for i in range(0, len(listDistinctProperties)):
    print(listDistinctProperties[i])
print(len(listDistinctProperties))
distinctPropertiesNewValue = 'void:properties ' + str(len(listDistinctProperties))
distinctPropertiesMSG = initializingMetadataFile(distinctPropertiesOldValue, distinctPropertiesNewValue)
print(100*'-')
print


####listGeoData = discoverLatitudinalLongitudinalData(datasetName, datasetFormat)
####print('----------Results from discovering geodata----------')
####for i in range(0, len(listGeoData)):
####    print(listGeoData[i])
####print(100*'-')
####print


lengthDistinctSubjects = getNumberOfDistinctSubjects(datasetName, datasetFormat)
print('----------Results from distinct subjects length------')
print(lengthDistinctSubjects)
print(distinctSubjectsOldValue)
distinctSubjectsNewValue = 'void:distinctSubjects ' + str(lengthDistinctSubjects)
print(distinctSubjectsNewValue)
distinctSubjectsMSG = initializingMetadataFile(distinctSubjectsOldValue, distinctSubjectsNewValue)
print(100*'-')
print


lengthDistinctObjects = getNumberOfDistinctObjects(datasetName, datasetFormat)
print('----------Results from distinct objects length------')
print(lengthDistinctObjects)
distinctObjectsNewValue = 'void:distinctObjects ' + str(lengthDistinctObjects)
distinctObjectsMSG = initializingMetadataFile(distinctObjectsOldValue, distinctObjectsNewValue)
print(100*'-')
print


lengthDistinctPredicates = getNumberOfDistinctPredicates(datasetName, datasetFormat)
print('----------Results from distinct predicates length------')
print(lengthDistinctPredicates)
print(100*'-')
print


triplesLength = getNumberOfTripples(datasetName, datasetFormat)
print('----------Results from triples length------')
print(triplesLength)
triplesNewValue = 'void:triples ' + str(triplesLength)
triplesMSG = initializingMetadataFile(triplesOldValue, triplesNewValue)
print(100*'-')
print

newFeatureBaseAddress = 'void:feature <' + featureBase + extractDatasetFeature(datasetFormat) + '>'
featureMSG = initializingMetadataFile(oldFeature, newFeatureBaseAddress)

prepareDataMSG = prepareData(datasetName, datasetFormat)
print('----------Results from prepare data------')
print(prepareDataMSG)
print(100*'-')
print

languageCode = detectLanguage('tempData.txt')
print('----------Results from prepare data------')
print(languageCode)
print(100*'-')
print
newLanguageAddress = 'dct:language <' + languageBase + languageCode.decode('utf8') + '>'
languageMSG = initializingMetadataFile(oldLanguage, newLanguageAddress)

newDocuments = 'void:documents ' + str(currentDatasetNumber)
documentsMSG = initializingMetadataFile(oldDocuments, newDocuments)

newDatasetName = ':dataset-' + storeNameExtension[0] + '-' + storeNameExtension[1]
datasetNameMSG = initializingMetadataFile(oldDatasetName, newDatasetName)


print("end of execution...")
