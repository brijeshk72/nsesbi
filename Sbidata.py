#This project Run Only online otherwise Show message Error
#Import Some important module

import requests
import json
import matplotlib.pyplot as plt #use only for plotting data 

#  Requests.get() use to fetch NSE/SBI data from Quandl.com, All data will be fetch online  

a = requests.get('https://www.quandl.com/api/v3/datasets/NSE/SBIN.json?api_key=x6Gyy2XMCzxuAWXjKpm3')

b = json.loads(a.text)
my_data = b['dataset'] ['data']
useful_data = [i[1] for i in reversed(my_data)]
x_data = [i for i in range(len(useful_data))]

# Plot Used to Show data on screen 
plt.plot(x_data, useful_data)
plt.title('State Bank Of india (NSE data) Made By Brijesh')
plt.ylabel('Stock Price')
plt.xlabel('Time')
plt.show()

