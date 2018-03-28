import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.cluster.vq import vq, kmeans, whiten
#assuming the first line is labels, throwing them away for now
def readArray(dataFileName,dimensionList,dataStart):
    count = 0
    dataFile = open(dataFileName,'r')
    matrix = np.zeros(tuple(dimensionList))
    for line in dataFile:
        if count == 0:
            #do something with these later
            labels = line
        else:
            elems = line.split('\t')
            dataElems = map(float,elems[dataStart:])
            flatArray = np.asarray(dataElems)
            fixedArray = np.reshape(flatArray,tuple(dimensionList[1:]))
            matrix[count-1] = fixedArray

        count += 1
    return matrix

def numMeasured(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

def matrixOps(matrix):
    #get correaltion matrix between different samples
    matA = matrix[:,:,0]
    matB = matrix[:,:,1]
    matC = matrix[:,:,2]
    #corr = np.corrcoef(matA,matB)

    #
    mat1 = matrix[:,0,:].flatten()
    mat2 = matrix[:,1,:].flatten()
    mat3 = matrix[:,2,:].flatten()
    mat4 = matrix[:,3,:].flatten()

    #plt.hist(mat1)
    #plt.show()

    #do some basic clustering with an arbitrary k
    whitened = whiten(matB)
    codebook, distortion = kmeans(whitened,4)
    plt.scatter(whitened[:, 0], whitened[:, 1])
    plt.scatter(codebook[:, 0], codebook[:, 1], c='r')
    plt.show()



m = numMeasured('ModifiedData.tsv')
dimList = [m,4,3]
dStart = 2
fname = 'ModifiedData.tsv'
matrix = readArray(fname,dimList,dStart)
matrixOps(matrix)
