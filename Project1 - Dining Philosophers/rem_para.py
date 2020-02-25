# 2/19/2020 by Andrew Reid
#
# Purpose of script: 
# remove all '(' and ')' characters from the data text file, 
# "benchmark_data_philosopher_waiter.txt"
#
# For example: a line "(1, 0.0, 0.01499)" becomes "1, 0.0, 0.01499"

newfilename = input("Enter new file save data name: ")

f1 = open("benchmark_data_philosopher_waiter.txt", "r")
data = f1.read()
f1.close()

a = [
    i for i in data
    if (i != '(' and i != ')')
]
output = ''.join(a)
output = 'meals,meal_time,run_time\n'+output #insert header line at top

f2 = open(newfilename, "w")
f2.write(output)
f2.close()