import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "age": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price": [20000, 19000, 18000, 17000, 16000, 15000, 14000, 13000, 12000, 11000]
}

df = pd.DataFrame(data)

# line 
plt.plot(df['age'], df['price'], marker='o')
plt.xlabel('Age of Car (years)')
plt.ylabel('Price of Car (USD)')
plt.title('Car Price vs Age')
plt.show()

#  line y = mx + b
# m - slope
# b - y intercept
# b = 21000
# m - slope -1000
# y = -1000 * x + 21000
# y = -1000 * 11 + 21000
# y = 10000

# 15 years
# y = -1000 * 15 + 21000
# y = 6000
# 13 years
# y = -1000 * 13 + 21000
# y = 8000

model = LinearRegression()
model.fit(df[['age']], df['price'])



age = int(input("Enter the age of the car (in years): ").strip())
predicted_price = model.predict(np.array([[age]]))[0]
print(f"The estimated price of the car is: ${predicted_price:.2f}")

plt.plot(df['age'], df['price'], marker='o', label='Actual Data')
plt.plot(age, predicted_price, marker='x', color='red', label='Predicted Price')
plt.xlabel('Age of Car (years)')
plt.ylabel('Price of Car (USD)')
plt.title('Car Price vs Age')
plt.legend()
plt.show()