import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "age": [1,1,1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,2,2,
            3,3,3,3,3,3,3,3,3,3,
            4,4,4,4,4,4,4,4,4,4,
            5,5,5,5,5,5,5,5,5,5,
            6,6,6,6,6,6,6,6,6,6,
            7,7,7,7,7,7,7,7,7,7,
            8,8,8,8,8,8,8,8,8,8,
            9,9,9,9,9,9,9,9,9,9,
            10,10,10,10,10,10,10,10,10,10],
    "price": [20000,20050,19995,19950,20010,19940,19900,20020,19980,20030,
              19500,19450,19520,19480,19510,19490,19530,19470,19540,19460,
              19000,18950,19020,18980,19010,18990,19030,18970,19040,18960,
              18500,18450,18520,18480,18510,18490,18530,18470,18540,18460,
              18000,17950,18020,17980,18010,17990,18030,17970,18040,17960,
              17500,17450,17520,17480,17510,17490,17530,17470,17540,17460,
              17000,16950,17020,16980,17010,16990,17030,16970,17040,16960,
              16500,16450,16520,16480,16510,16490,16530,16470,16540,16460,
              16000,15950,16020,15980,16010,15990,16030,15970,16040,15960,
              15500,15450,15520,15480,15510,15490,15530,15470,15540,15460]
              
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

print("slope :=", model.coef_[0])
print("intercept :=", model.intercept_)
# slope : -500.0
# intercept : 20500.0
# y = -500 * x + 20500  
