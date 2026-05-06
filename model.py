import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("houseprice.csv")
# Handle missing values
df['LotFrontage'].fillna(df['LotFrontage'].median(), inplace=True)
df.drop(['Alley'], axis=1, inplace=True)
df.dropna(subset=['SalePrice'], inplace=True)

# Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col].astype(str))

# Feature Engineering
df['TotalArea'] = df['GrLivArea'] + df['TotalBsmtSF']
df['TotalBathrooms'] = df['FullBath'] + (0.5 * df['HalfBath'])

# 🔥 ADD THIS LINE
df.fillna(0, inplace=True)

# Define X and y
X = df.drop(['SalePrice', 'Id'], axis=1)
y = np.log1p(df['SalePrice'])   # Apply log here

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price (log)")
plt.ylabel("Predicted Price (log)")
plt.title("Actual vs Predicted House Prices")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.show()