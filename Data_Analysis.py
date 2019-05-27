import pandas as pd 
import matplotlib as mpl 
from matplotlib import pyplot as plt 
import seaborn as sns

#sets the seaborn template; makes graphs look nicer
sns.set()

data = pd.read_csv('countries.csv')
#print(country)

#Compare the population growth in the US and China

#Isolates all the rows with United States as its country
US = data[data.country == 'United States']

#Same thing for China
china = data[data.country == 'China']

#same thing for Canada
canada = data[data.country == 'Canada']

# * Be Careful of the dtype of the elements when making comparisons

print(US)
print("\n")
print(china)
print("\n")
print(canada)
print("\n")

#show relative growth of population by dividing by the first year 
print (US.population * 100 / US.population.iloc[0])
print ("\n")
print(china.population * 100 / china.population.iloc[0])
print("\n")
print(canada.population * 100/ canada.population.iloc[0])



#plot year on x-axis, and population on y-axis
# ** -> ^ 

#Code below is for a simple population vs time graph

#plt.plot(US.year, US.population / 10 ** 6)
#plt.plot(china.year, china.population/ 10 ** 6)
#plt.legend(['United States', 'China'])
#plt.ylabel('population millions')
#plt.xlabel('year')
#plt.ylabel('population (millions)')

#code below is for a population growth analysis

plt.plot(US.year, US.population* 100/US.population.iloc[0])
plt.plot(US.year, US.population* 100/US.population.iloc[0], 'o')
plt.plot(china.year, china.population*100/china.population.iloc[0])
plt.plot(china.year, china.population*100/china.population.iloc[0],'o')
plt.plot(canada.year, canada.population*100/canada.population.iloc[0])
plt.plot(canada.year, canada.population*100/canada.population.iloc[0],'o')

plt.legend(['United States', 'China','Canada'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100%)')
plt.show()

