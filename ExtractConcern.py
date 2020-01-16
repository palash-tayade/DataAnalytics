import csv

def extractNegativeDocuments(documents):
    #function that removes all positive and neutral documents
    with open('SentimentData.csv',"r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csvFile_rows= list(csv_reader)
       
       #delete all documents that do not have negative sentiment
        for i in range(0,len(csvFile_rows)):
            if csvFile_rows[i][2] != "Negative":
                id=csvFile_rows[i][1]
                del documents[id]
        return documents

#Read the Document.csv file and store it into a dictionary. 
with open("List Table - Text 1.csv", "r") as f:
    lines = f.read().splitlines()
    temp = list(lines)
    documents={}

    #creating a dictionary of documents where the key is the documentID and the value is the feedback posted by the user.
    for i in range(len(temp)):
        documents[temp[i].split("\",\"")[2]]=temp[i].split("\",\"")[0]
          
    extractNegativeDocuments(documents)
    
    #Read the Side effects of medication provided in the SideEffectsConcept.txt file
    with open('SideEffectsConcept.txt',"r") as f:
        sideEffect = f.read().split('\n')
    sideEffectCount =  {}

    #create a dictionary that store the count of documents that mention a side effect
    for row in sideEffect:
        sideEffectCount[row]=0

    #For each side effect, count the number of documents that mentions it and store the count in sideEffectCount dictionary
    for key in sideEffectCount.keys():
        count=0
        for value in documents.values():
            if key.upper() in value.upper():
                count+=1      
        sideEffectCount[key] = count

#Export the data from sideEffectCount dictionary into a file
w = csv.writer(open("OutputAfterSentimentAnalysis.csv", "w"))
for key, val in sideEffectCount.items():
    w.writerow([key, val])

