

def extractDatasetFeature(fileExtention):
    featureName = ''
    if(fileExtention == 'n3'):
        featureName = 'Notation3'
    elif(fileExtention == 'nt'):
        featureName = 'N-Triples'
    elif(fileExtention == 'ntriples'):
        featureName = 'N-Triples'
    elif(fileExtention == '.nx'):
        featureName = ''
    elif(fileExtention == 'ttl'):
        featureName = 'Turtle'
    elif(fileExtention == 'rdf'):
        featureName = 'RDF/XML'
    elif(fileExtention == 'nq'):
        featureName = 'N-Quads'
    elif(fileExtention == 'csv'):
        featureName = 'SPARQL_Results_CSV'
    elif(fileExtention == 'json'):
        featureName = 'JSON'
    elif(fileExtention == 'json-ld'):
        featureName = 'JSON-LD '

    return featureName
