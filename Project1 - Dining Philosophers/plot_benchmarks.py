import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("data.txt")
# the columns are 'meals', 'meal_time', and 'run_time'

# x = df['meals']
# y = df['meal_time']
# z = df['run_time']

df = df.sort_values(['meals','meal_time']).reset_index()
df_unq = df.groupby(['meals','meal_time']).size().reset_index(name='Freq')
# ^ is table of unique pairs (meal, meal_time) and how many
#print(df)
#print(df_unq)

# Collect Average and StDev for each unique pair
mean = []
std = []
a = 0 #start slice
b = 0 #end slice
for i in df_unq.index:
    # slice df
    b = a + df_unq.iat[i,2] #add Freq of this pair
    df_slice = df[a:b]
    #print(df_slice)
    a = b #set start for next cycle
    # calculate 
    mn = df_slice.run_time.mean()
    sd = df_slice.run_time.std()
    # append
    mean.append(mn)
    std.append(sd)

df_unq['mean_run_time'] = mean
df_unq['std_run_time'] = std

# print(df_unq)

#### DO THE PLOTTING ####

# Plot meal_time vs run_time, for different meals curves
length = len(df_unq.index)
x = df_unq.loc[0:3,'meal_time']
ab = zip(range(0,length,4),range(3,length,4))
ys = [
    df_unq.loc[a:b,'mean_run_time']
    for a,b in ab
]
ystds = [
    df_unq.loc[a:b,'std_run_time']
    for a,b in ab
]
params = [
    'meals='+str(df_unq.loc[a:a,'meals'])
    for a,b in ab
]
# print(x)
# print(y)

fig = plt.figure()

for y, ystd, param in zip(ys,ystds,params):
    plt.errorbar(x, y, yerr=ystd, uplims=True, lolims=True, label=param)

plt.legend(loc='lower right')
plt.show()

# Plot meals vs run_time, for different meal_time curves