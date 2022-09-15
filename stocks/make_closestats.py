# df.values gives you all content of dataframe
# print(df[['Open'], ['High']]).head()
import plotting
import web_to_csv
import read_csv
import re

datelist = []
closelist = []
closedict = {}

'''Populates CSV with data'''
# web_to_csv.web_to_csv('spy', 'yahoo')

'''Plots, will clean & add args'''
# plotting.do_plot()

df = read_csv.create_df("spy.csv", True, 0)
Close = df['Close']
dfdate = df['Date']
#print(adjClose)

pattern = r'\.\d?\d?\d'
#adjClose = df['Adj Close'].to_string(index= False)
print(Close)

for roll in Close:
    z = re.search(pattern, str(roll))
    x = z.group(0)
    closelist.append(x)

for roll in dfdate:
    datelist.append(roll)

closelist.sort()
closedict.update({roll : 0 for roll in closelist})

for roll in closelist:
    closedict[roll] += 1

print(closedict)

with open('closestats.txt', "w") as file:
    for thing in closedict:
        file.write(thing + " : " + str(closedict[thing]) + '\n')

