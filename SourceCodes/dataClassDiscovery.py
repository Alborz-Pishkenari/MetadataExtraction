import rdflib
listFetchData = []
listDistinctClasses = []
dicCountSubjects = {}
dicCountPredicates = {}
dicCountObjects = {}

##Gives us all classes that have any members
##--------------------------------------------------------------------------------------------------
def retrieveDistinctClasses(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT DISTINCT ?class
                      WHERE {
                                [] a ?class
                            }
                      ORDER BY ?class
                  """)
    for row in qres:
        listDistinctClasses.append("%s" % row)

    return listDistinctClasses
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def countAndRateSubjects(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT ?s (COUNT(?s) AS ?count)
                      WHERE {
                                ?s ?p ?o .
                            }
                      GROUP BY ?s
                      ORDER BY DESC (?count)
                  """)
    for row in qres:
        dicCountSubjects[("%s" % row[0]).encode('utf-8')] = int("%s" % row[1])

    return dicCountSubjects
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def countAndRatePredicates(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT ?p (COUNT(?p) AS ?count)
                      WHERE {
                                ?s ?p ?o .
                            }
                      GROUP BY ?p
                      ORDER BY DESC (?count)
                  """)
    for row in qres:
        dicCountPredicates[("%s" % row[0]).encode('utf-8')] = int("%s" % row[1])

    return dicCountPredicates
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def countAndRateObjects(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT ?o (COUNT(?o) AS ?count)
                      WHERE {
                                ?s ?p ?o .
                            }
                      GROUP BY ?o
                      ORDER BY DESC (?count)
                  """)
    for row in qres:
        dicCountObjects[("%s" % row[0]).encode('utf-8')] = int("%s" % row[1])

    return dicCountObjects
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def fetchDataToList(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT ?o
                      WHERE {
                                ?s ?p ?o
                            }
                  """)
    for row in qres:
        sTemp = ("%s" % row)
        if (sTemp.startswith('http')):
            listFetchData.append(sTemp)

    return listFetchData
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def extractNumberOfInstancesPerClass(inputSourceName, inputFormatName, inputFullName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    s1 = ''

    qres = g.query("""SELECT (COUNT(?s) AS ?totalNumberOfInstances)
                      WHERE {
                                ?s rdfs:subClassOf """ + inputFullName + """
                            }
                  """) 
    for row in qres:
        s1 = ("%s" % row)

    return s1
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def getNumberOfDistinctSubjects(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    lengthDistinctSubjects = ''
    
    qres = g.query("""SELECT (COUNT(DISTINCT ?s) as ?cnt)
                      WHERE {
                                ?s ?p ?o .
                            }
                   """)
    for row in qres:
        lengthDistinctSubjects = ("%s" % row)

    return lengthDistinctSubjects
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def getNumberOfDistinctObjects(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    lengthDistinctObjects = ''
    
    qres = g.query("""SELECT (COUNT(DISTINCT ?o) as ?cnt)
                      WHERE {
                                ?s ?p ?o .
                            }
                   """)
    for row in qres:
        lengthDistinctObjects = ("%s" % row)

    return lengthDistinctObjects
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def getNumberOfDistinctPredicates(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    lengthDistinctPredicates = ''
    
    qres = g.query("""SELECT (COUNT(DISTINCT ?p) as ?cnt)
                      WHERE {
                                ?s ?p ?o .
                            }
                   """)
    for row in qres:
        lengthDistinctPredicates = ("%s" % row)

    return lengthDistinctPredicates
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
def getNumberOfTripples(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    tripplesLength = ''
    
    qres = g.query("""SELECT (COUNT(*) as ?cnt)
                      WHERE {
                                ?s ?p ?o .
                            }
                   """)
    for row in qres:
        tripplesLength = ("%s" % row)

    return tripplesLength
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

