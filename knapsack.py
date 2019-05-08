#Solves a modified version of the 'knapsack' problem, where there are multiple knapsacks (people)
# that can be filled, each with it's own weight limit. The program takes a text file as input,
# which contains test cases to run through the algorithm. Each test case contains a list of 
# items by value and weight, as well as a list of people and their weight capacity. Output is written
# to a file, and consists of the total value carried by all people, as well as the items each
# person carried
#Author: Shawn McMannis
#Last mod date: 4/18/19

from itertools import islice

#main

#Open the export file
exportFile = open("results.txt", "w")

#Number of test cases
tests = 0

#Number of items in the test case
numItems = 0

#Array of values for items
values = []

#Array of weights for items
weights = []

#Number of people in the family
numPops = 0

#Weight capacity of each family member
capacity = []

#Weight capacity of each family member, sorted
sortedCap = []

#Value of items each family member carries
popVal = []

#Total value of items carried by all family members
totVal = 0

#Matrix used to store items carried by each family member
itemMatrix = []

#Counts the current family member
famMem = 1

#Boolean used to write family contributions to file
flag = 0

#Open import file 'sampleInput.txt'
with open("sampleInput.txt", "r") as importFile:

    #Set number of tests included in input file
    tests = list(islice(importFile, 1))
    tests = int(tests[0])

    for test in range(0, tests):
        #Slice number of items
        numItems = list(islice(importFile, 1))
        numItems = int(numItems[0])

        #Slice items (price weight)
        items = list(islice(importFile, numItems))
        for i in range(0, len(items)):
            temp1 = items[i].split()
            tempVal = temp1[0].split()
            tempWgt = temp1[1].split()
            values.append(tempVal[0])
            weights.append(tempWgt[0])

        #Convert values to integers
        for i in range(0, len(values)):
            values[i] = int(values[i])

        for i in range(0, len(weights)):
            weights[i] = int(weights[i])

        #Slice number of family members
        numPops = list(islice(importFile, 1))
        numPops = int(numPops[0])

        #Slice weight capacity of family members
        for i in range(0, numPops):
            temp1 = list(islice(importFile, 1))
            temp2 = temp1[0].split()
            temp2 = int(temp2[0])
            capacity.append(temp2)

            sortedCap = sorted(capacity)

        #Create matrix to store items carried by each family member
        itemMatrix = [[-1 for x in range(numItems)] for y in range(numPops)]

        #Process data
        for i in range(numPops):

            #Create the solution matrix
            valMatrix = [[0 for x in range(capacity[i] + 1)] for y in range(numItems + 1)]

            #Populate the solution matrix
            for j in range(numItems + 1):
                for k in range(capacity[i] + 1):
                    if j==0 or k==0:
                        valMatrix[j][k] = 0
                    elif weights[j-1] <= k:
                        valMatrix[j][k] = max(values[j-1] + valMatrix[j-1][k-weights[j-1]], valMatrix[j-1][k])
                    else:
                        valMatrix[j][k] = valMatrix[j-1][k]

            #Store the total value carried by family member i
            popVal.append(valMatrix[numItems][capacity[i]])

            results = popVal[i]
            popCap = capacity[i]

            #Reconstruct the items the family member collected and store them in itemMatrix
            for q in range(numItems, 0, -1):
                if q > 0 and results > 0:
                    if results != valMatrix[q-1][popCap]:
                        itemMatrix[i].append(q)
                        results = results - values[q-1]
                        popCap = popCap - weights[q-1]

        #Calculate the total value carried by all family members
        for pop in popVal:
            totVal = totVal + pop

        #Write initial results to file
        exportFile.write("Test Case ")
        exportFile.write(str(test + 1))
        exportFile.write("\n")
        exportFile.write("Total Price ")
        exportFile.write(str(totVal))
        exportFile.write("\n")
        exportFile.write("Member Items")
        exportFile.write("\n")

        #Write the item numbers collected to file
        for row in itemMatrix:
            exportFile.write("\t")
            exportFile.write(str(famMem))
            famMem = famMem + 1
            exportFile.write(":")
            row.sort()
            for elem in row:
                if elem >= 0:
                    exportFile.write(" ")
                    exportFile.write(str(elem))
                    flag = 1
            if flag == 0: #Writes '0' if the family member couldn't carry anything
                exportFile.write(" 0")

            exportFile.write("\n")

        exportFile.write("\n")
        
        #Reset arrays / variables
        values = []
        weights = []
        capacity = []
        popVal = []
        totVal = 0
        famMem = 1
        flag = 0

#Close export file
exportFile.close()