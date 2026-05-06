 House Price Prediction using Machine Learning

📌 Project Overview

This project focuses on predicting house prices using **regression techniques** based on various features such as area, number of rooms, bathrooms, and other property-related attributes.
The model is trained on a housing dataset and demonstrates the complete machine learning pipeline including **data preprocessing, feature engineering, model training, and evaluation**.

 🚀 Features

* Data Cleaning and Handling Missing Values
* Feature Engineering (Total Area, Bathrooms, etc.)
* Encoding Categorical Variables
* Data Scaling using StandardScaler
* Regression Model (Linear Regression)
* Model Evaluation using R² Score and RMSE
* Data Visualization (Scatter Plot & Heatmap)

 📂 Dataset

* Source: Kaggle - *House Prices Dataset*
* File used: `houseprice.csv`

 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

 ⚙️ Project Workflow

1. **Data Collection**

   * Load dataset using Pandas

2. **Data Preprocessing**

   * Handle missing values
   * Drop unnecessary columns

3. **Feature Engineering**

   * Create new meaningful features like:

     * Total Area
     * Total Bathrooms

4. **Encoding**

   * Convert categorical data into numerical format

5. **Train-Test Split**

   * Split dataset into training and testing sets

6. **Feature Scaling**

   * Normalize data using StandardScaler

7. **Model Training**

   * Train Linear Regression model

8. **Evaluation**

   * Evaluate using:

     * R² Score
     * RMSE (Root Mean Squared Error)

 📊 Results

* The model predicts housing prices with reasonable accuracy.
* Visualization shows correlation between actual and predicted values.

 ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

2. Navigate to the project folder:

```bash
cd house-price-prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the model:

```bash
python model.py
```
 🌐 (Optional) Run Web App

If using Streamlit:

```bash
streamlit run app.py
```

 📁 Project Structure

```
house_price_project/
│
├── model.py
├── app.py
├── houseprice.csv
├── requirements.txt
└── README.md
```
 📈 Future Improvements

* Use advanced models like Random Forest / XGBoost
* Hyperparameter tuning
* Deploy using Streamlit Cloud
* Improve UI for better user experience

👩‍💻 Author

**Janhvi Bhurley**

 ⭐ Acknowledgements

* Kaggle for providing the dataset
* Scikit-learn documentation

 📌 Note

This project is for learning purposes and demonstrates a basic regression pipeline.
