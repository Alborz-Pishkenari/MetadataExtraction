import rdflib
listDistinctProperties = []
listNumberOfTimesPerProperty = []


##--------------------------------------------------------------------------------------------------
def retrieveDistinctProperties(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)
    qres = g.query("""SELECT DISTINCT ?property
                      WHERE {
                                [] ?property [] .
                            }
                      ORDER BY ?property
                  """)
    for row in qres:
        listDistinctProperties.append("%s" % row)

    return listDistinctProperties
##--------------------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------------------
## Stats about properties
## This query tells for each property how many times it has been used.
def numberOfTimesPerProperty(inputSourceName, inputFormatName):
    g = rdflib.Graph()
    g = g.parse(source = inputSourceName, format = inputFormatName)

    qres = g.query(
           """SELECT ?property (COUNT(?property) AS ?propTotal)
           WHERE { ?s ?property ?o . }
           GROUP BY ?property
           ORDER BY DESC(?propTotal)
    """)

    for row in qres:
        listNumberOfTimesPerProperty.append("%s %s " % row)

    return listNumberOfTimesPerProperty
##--------------------------------------------------------------------------------------------------
