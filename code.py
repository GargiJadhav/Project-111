import pandas as pd
import statistics as st
import random


data = pd.read_csv("data.csv")

readingTime = data["reading_time"].tolist()

mean = st.mean(readingTime)
mode = st.mode(readingTime)
median = st.median(readingTime)
stdev = st.stdev(readingTime)

print("----------------------------------------------------------------------------")

print("Mean of population is " , mean)
print("Mode of population is ", mode)
print("Median of population is " , median)
print("Stdev of population is ", stdev)

#--------------------------------Sampling-----------------------------

meanList=[]
for i in range(100):
    dataSet=[]
    for i in range(30):
        id = random.choice(readingTime)
        dataSet.append(id)
    meanList.append(st.mean(dataSet))

meanOfSample = st.mean(meanList)
stdevOfSample = st.stdev(meanList)

print("---------------------------------------------------------------------------------")

print("Mean of Sample is " , meanOfSample)
print("Stdev of Sample is ", stdevOfSample)

#----------------------------Sample.csv---------------------------------------------

df = pd.read_csv("sample.csv")

sampleData = df["reading_time"].tolist()

mean1 = st.mean(sampleData)
mode = st.mode(sampleData)
median = st.median(sampleData)
stdev1 = st.stdev(sampleData)


zScore = (mean1 - meanOfSample)/stdev

print("----------------------------------------------------------------------------")

print("Z score is ", zScore)
print("Mean of New Sample is " , mean1)
print("Mode of New Sample is ", mode)
print("Median of New Sample is " , median)
print("Stdev of New Sample is ", stdev1)

