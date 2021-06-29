import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('model1_1905_lr-2_f5ff10_convp20_e30.csv', header=None)

y=data[7]
x=data[5]

# plotting the points 
plt.plot(y)
  
# naming the x axis
plt.xlabel('Step')
# naming the y axis
plt.ylabel('Error')
#plt.yscale('log')
plt.xlim([0, 50])
#plt.ylim([0, 250])  
# giving a title to my graph
plt.title('Training error per iteration (0 epoch)')
  
# function to show the plot
plt.show()


