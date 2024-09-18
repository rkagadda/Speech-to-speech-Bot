import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
#Here in place of data we can use any dataset.
data = {
    'overs': [10, 15, 20, 25, 30, 35, 40, 45, 50],
    'wickets': [1, 2, 3, 3, 4, 5, 6, 7, 8],
    'score': [60, 80, 120, 140, 180, 200, 220, 250, 270]
}
df = pd.DataFrame(data)
x = df[['overs', 'wickets']]
y = df['score']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
overs =int(input("Enter the no of overs:"))
wickets = int(input("Enter the no of wickets lost: "))
predicted_score = lr.predict([[overs, wickets]])
print(f"Predicted score after {overs} overs and {wickets} wickets lost: {int(predicted_score[0])}")
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='overs', y='score', data=df, palette='coolwarm', s=100)
# Set plot title and labels
plt.title("Relationship between Overs, Wickets, and Score")
plt.xlabel("Overs")
plt.ylabel("Score")

# Show the plot
plt.show()
