import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math_score"])
#fig.show()
mean = statistics.mean(data)
stdv = statistics.stdev(data)
#print(mean , stdv)

def randomSetOfMean(counter):
    dataset = []
    for i in range (0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

meanlist = []
for i in range(0,1000):
    setOfmean = randomSetOfMean(100)
    meanlist.append(setOfmean)

stnd = statistics.stdev(meanlist)
mean1 = statistics.mean(meanlist)
#print(stnd , mean)

fsdvs,fsdve = mean-stnd,mean+stnd
ssdvs,ssdve = mean-(2*stnd),mean+(2*stnd)
tsdvs,tsdve = mean-(3*stnd),mean+(3*stnd)

fig = ff.create_distplot([meanlist],["studentMarks"])
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fsdvs,fsdvs],y = [0,0.17],mode = "lines", name = "fsdvs"))
fig.add_trace(go.Scatter(x = [fsdve,fsdve],y = [0,0.17],mode = "lines", name = "fsdvs"))
fig.add_trace(go.Scatter(x = [ssdvs,ssdvs],y = [0,0.17],mode = "lines", name = "ssdvs"))
fig.add_trace(go.Scatter(x = [ssdve,ssdve],y = [0,0.17],mode = "lines", name = "ssdvs"))
fig.add_trace(go.Scatter(x = [tsdvs,tsdvs],y = [0,0.17],mode = "lines", name = "tsdvs"))
fig.add_trace(go.Scatter(x = [tsdve,tsdve],y = [0,0.17],mode = "lines", name = "tsdvs"))
#fig.show()

zScore = (mean - mean1 / stnd)
print(zScore)