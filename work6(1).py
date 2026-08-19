import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [120, 180, 150, 220, 300, 280]

plt.plot(months, sales)

plt.title('Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()