import pandas as pd
p = {'Houses':['Bugalow','Flat','Skyscraper'],
     'Around':[7,6,2]
}

mydat = pd.DataFrame(p, index=['h1','h2','h3'])
print(mydat)

print(pd.__version__)

a = [1,23,34,'boy']
mya = (pd.Series(a))
print(mya[0])
myaa = pd.Series(a, index=[ 'e','r','t','g'])
print(myaa)

b = { 'day1': 'wednesday', 'day2':'thursday','day3':'friday'
} 
c = pd.Series(b)
print(c.loc['day1'])
# to_string => display all the data contain in a dataframe
# pd.options.display.max_rows => displays the total amount of data in a dataframe
# hea() => display first 10 data # tail() => display last ten data
# info() => display an overview of the data
# dropna() => drop rows having empty cells 
#fillna(rows, inplace = True) => fill rows with empthy cells
#dropna(subset=['Date'], inplace = True) => removing a specific row
# to_datatime => set a colume to data and time 
#plot(kind = 'scatter', x = 'Duration', y = 'Calories') => Specify dat u want a scatter plot with d kind argument kind ='scatter'
# pd.plot(kind = 'hist')
