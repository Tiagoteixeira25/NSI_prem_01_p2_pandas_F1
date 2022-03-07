import pandas as pd
import matplotlib.pyplot as plt


original = pd.read_csv("Classeur_projet.csv", encoding = "ISO-8859-1")
original = original.set_index('nom pilote')


result = pd.DataFrame()
result.index =["Average","Top 1","Top 2","Top 3","Top 4","Lowest 1", "Lowest 2", "Lowest 3", "Lowest 4"]

average = {}
sort_value = {}

    

for column in original:
    average[column] = original[column].mean()
    sort_value[column] = original.sort_values(by = column)
    result.insert(0,column,"")
    result.at["Average",column] = average[column]
    a = sort_value[column]
    b = a.index
    result.at["Lowest 1",column] = b[0]
    result.at["Lowest 2",column] = b[1]
    result.at["Lowest 3",column] = b[2]
    result.at["Lowest 4",column] = b[3]
    result.at["Top 1",column] = b[19]
    result.at["Top 2",column] = b[18]
    result.at["Top 3",column] = b[17]
    result.at["Top 4",column] = b[16]
    


original.plot.bar(x="abandon",y="grand prix")



print(original)
print(average)
print(sort_value)
print(result)

