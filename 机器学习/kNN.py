#!/usr/bin/env python
# coding=utf-8

from numpy import * #科学计算包
import operator     #运算符模块

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

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
