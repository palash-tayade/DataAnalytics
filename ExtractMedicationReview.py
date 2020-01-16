import csv
import copy

def extractNegativeDocuments(documents,csvFile_rows):
    #function that removes all positive and neutral sentiment documents
    
    negativeDocuments = copy.deepcopy(documents)
    
   #delete all documents that do not have negative sentiment
    for i in range(0,len(csvFile_rows)):
        if csvFile_rows[i][2] == "Positive" or csvFile_rows[i][2] == "Neutral":
            id=csvFile_rows[i][1]
            del negativeDocuments[id]
    return negativeDocuments


def extractPositiveDocuments(documents,csvFile_rows):
    #function that removes all negative and neutral documents
    
    positiveDocuments = copy.deepcopy(documents)
       
    #delete all documents that do not have positive sentiment
    for i in range(0,len(csvFile_rows)):
        if csvFile_rows[i][2] == "Neutral" or csvFile_rows[i][2] == "Negative":
            id=csvFile_rows[i][1]
            del positiveDocuments[id]
    return positiveDocuments

def extractNeutralDocuments(documents,csvFile_rows):
    #function that removes all positive and negative sentiment documents
    
    neutralDocuments = copy.deepcopy(documents)
       
   #delete all documents that do not have neutral sentiment
    for i in range(0,len(csvFile_rows)):
        if csvFile_rows[i][2] == "Positive" or csvFile_rows[i][2] == "Negative":
            id=csvFile_rows[i][1]
            del neutralDocuments[id]
                
    return neutralDocuments

def getMedicReview(medication,doc):
    #this function deletes all documents that does not contain the supplied medication
    docCopy = copy.deepcopy(doc)
    tempDocCopy = copy.deepcopy(doc)
    for key,value in docCopy.items():
        if not medication.upper() in value.upper():
            del tempDocCopy[key]
    return tempDocCopy

#Read the Document.csv file and store it into a dictionary. 
with open("Documents.csv", "r") as f:
    lines = f.read().splitlines()
    temp = list(lines)
    documents={}


    #creating a dictionary of documents where the key is the documentID and the value is the feedback posted by the user.
    for i in range(len(temp)):
        documents[temp[i].split("\",\"")[2]]=temp[i].split("\",\"")[0]

#Get sentiment data from SentimentData.csv file
with open('SentimentData.csv',"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    csvFile_rows= list(csv_reader)

    #Get documents with negative sentiment
    negativeDocs = extractNegativeDocuments(documents,csvFile_rows)

    #Get documents with positive sentiment
    positiveDocs = extractPositiveDocuments(documents,csvFile_rows)

    #Get documents with neutral sentiment
    neutralDocs = extractNeutralDocuments(documents,csvFile_rows)

    #Get the name of medication names from MedicationConcept.txt file
    with open('MedicationConcept.txt',"r") as f:
        medication = f.read().split('\n')
    
        medicReview={}
        
        #For each medication retrieve the count of negative,positive and neutral review
        for row in medication:
            negReview = len(getMedicReview(row,negativeDocs))
            posReview = len(getMedicReview(row,positiveDocs))
            neuReview = len(getMedicReview(row,neutralDocs))

            #Store the computed data as a dictionary
            medicReview[row]=str(negReview)+","+str(posReview)+","+str(neuReview)
    

#Export the data from medicReview dictionary into a file
w = csv.writer(open("MedicationReview.csv", "w"))
for key, val in medicReview.items():
    w.writerow([key,val])