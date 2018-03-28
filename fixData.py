import numpy as np
import random

#TODO
#load data
#generate samples(randomly generate some noise)

dataFileTPMS = open('E-GEOD-38612-query-results.tpms.tsv','r')
dataFileFPKMS = open('E-GEOD-38612-query-results.fpkms.tsv','r')

sumList = [0.0,0.0,0.0,0.0]
countList = [0,0,0,0]
outS = ''
for line in dataFileTPMS:
    elems  = line.split('\t')
    if '#' in line:
        continue
    elif 'leaf' in line:
        newline = 'Gene_ID' + '\t' + 'Gene_Name' + '\t' + 'leaf-1' + '\t' + 'leaf-2' + '\t' + 'leaf-3' + '\t' + 'flower-1' + '\t' + 'flower-2' + '\t' + 'flower-3' + '\t' + 'fruit-1' + '\t' + 'fruit-2' + '\t' + 'fruit-3' + '\t' + 'root-1' + '\t' + 'root-2' + '\t' + 'root-3' + '\n'
    else:
        newline = ''
        #copy first two vals
        newline += elems[0] + '\t' + elems[1] + '\t'
        #add 2 more samples for the new vals
        for i in range(2,5):
            #if no data then create some
            if elems[i] == '':
                average = sumList[i-2]/countList[i-2]
                sampVal = random.uniform(average - .5, average + .5)
                newline += str(sampVal) + '\t'
                #Add two more new samples
                sampVal = random.uniform(average - .5, average + .5)
                newline += str(sampVal) + '\t'
                sampVal = random.uniform(average - .5, average + .5)
                newline += str(sampVal) + '\t'

            else:
                countList[i-2] += 1
                sumList[i-2] += float(elems[i])
                average = sumList[i-2]/countList[i-2]
                newline += elems[i] + '\t'
                #Add two more new samples
                sampVal = random.uniform(average - .5, average + .5)
                newline += str(sampVal) + '\t'
                sampVal = random.uniform(average - .5, average + .5)
                newline += str(sampVal) + '\t'
        if elems[5] == '\n':
            average = sumList[3]/countList[3]
            sampVal = random.uniform(average - .5, average + .5)
            newline += str(sampVal) + '\t'
            #Add two more new samples
            sampVal = random.uniform(average - .5, average + .5)
            newline += str(sampVal) + '\t'
            sampVal = random.uniform(average - .5, average + .5)
            newline += str(sampVal) + '\n'

        else:
            s = elems[5].replace('\n','')
            countList[3] += 1
            sumList[3] += float(s)
            newline += str(s) + '\t'
            average = sumList[3]/countList[3]
            #Add two more new samples
            sampVal = random.uniform(average - .5, average + .5)
            newline += str(sampVal) + '\t'
            sampVal = random.uniform(average - .5, average + .5)
            newline += str(sampVal) + '\n'
    #print(newline)
    outS += newline
oFile = open('ModifiedData.tsv','w')
oFile.write(outS)
