#!/usr/bin/env python
# coding=utf-8

from numpy import * #科学计算包
import operator     #运算符模块
from os import listdir #列出给定目录的文件名

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

#k-近邻算法
def classify0(inX, dataSet, labels, k):
    #距离计算
    dataSetSize = dataSet.shape[0] #形状(行列)
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet #tile(A, B)重复A B次
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1) #.sum(axis = 1)将一个矩阵的每一行向量相加
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort() #argsort()返回按distance中的元素进行升序排序后得到的对应下表的列表

    #选择距离最小的k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    #排序
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

#将文本转换到NumPy的解析程序
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines) #得到文件行数
    returnMat = zeros((numberOfLines, 3)) #创建返回的numpy矩阵
    classLabelVector = []
    index = 0
    #解析文件数据到列表
    for line in arrayOLines:
        line = line.strip()
        listFromline = line.split('\t') #split分割字符串， 返回列表
        returnMat[index,:] = listFromline[0:3]
        classLabelVector.append(int(listFromline[-1]))
        index += 1
    return returnMat, classLabelVector

#归一化特征值 newValue = (oldValue - min) / (max - min)
def autoNorm(dataSet):
    minVals = dataSet.min(0) #参数0使得函数可以从列中选取最小值，而不是选取当前行的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1)) #tile()函数将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = normDataSet / tile(rangds, (m, 1)) #注意这是特征值相除,而对于某些数值处理软件包，/可能意味着矩阵除法，但在numpy库中，矩阵除法需要使用函数linalg.solve(matA, matB)
    return normDataSet, ranges, minVals

#分类器针对约会网站的测试代码
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataSet)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount +=1.0
    print "the total error rate is : %f" % (errorCount/float(numTestVecs))

#约会网站预测函数
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("frequent flier miles earned per year?"))
    ffMiles = float(raw_input("freguent flier miles earnd per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    calssifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels,3)
    print "You will probably like this person: ", resultList[classifierResult - 1]

#将图像转换成向量
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i + j] = int (lineStr[j])
    return returnVect

#手写数字识别系统的测试代码
def handwritingClassTest():
    hwLabels = []
    trainingFieldList = listdir('trainingDigits') #获取目录内容
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        #从文件名解析分类数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr):
            errorCont += 1.0
    print "the total number of errors is : %d" % errorCount
    print "the total error rate is : %f" % (errorCount / float(mTest))
