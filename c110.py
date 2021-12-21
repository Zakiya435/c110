from os import name
import pandas as pd, plotly.figure_factory as ff, csv, statistics, random, plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["average"].to_list()
mean_a = statistics.mean(data)
std = statistics.stdev(data)

print(mean_a,std)

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean_b = statistics.mean(dataset)
std_b = statistics.stdev(dataset)
print(mean_b,std_b)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,100):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def standard_deviation():
    mean = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(100)
        mean.append(set_of_means)

    std = statistics.stdev(mean)
    print("STD: ",std)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)

setup()

standard_deviation()