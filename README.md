#  RideFare AI Pricing App

An AI-powered Dynamic Pricing Prediction System built using **Machine Learning** and **Flask**. The project predicts the optimal price of a ride based on demand, stock availability, distance, season, customer rating, discount, and other business-related features.

---

##  Project Overview

Dynamic pricing is commonly used in ride-hailing and e-commerce platforms to adjust prices according to market conditions.

This project:
- Generates a realistic synthetic dataset
- Performs Exploratory Data Analysis (EDA)
- Applies Feature Engineering
- Trains multiple Machine Learning models
- Compares model performance
- Deploys the best model using Flask

---

##  Features

- 📊 Synthetic data generation
- 📈 Exploratory Data Analysis (EDA)
- 🧹 Data preprocessing
- ⚙️ Feature Engineering
- 🤖 Multiple Machine Learning models
- 🌐 Flask Web Application
- 📉 Model evaluation using multiple metrics

---

##  Dataset Features

| Feature | Description |
|---------|-------------|
| Demand | Current customer demand |
| Stock | Available drivers/resources |
| CompetitorPrice | Competitor pricing |
| Season | Seasonal condition |
| DayTime | Time of day |
| CustomerRating | Customer rating |
| Discount | Applied discount |
| HistoricalSales | Historical demand |
| Distance_km | Trip distance |
| Price | Target variable |

---

##  Machine Learning Models

The following regression models were implemented and compared:

- Multiple Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

##  Model Performance

| Model | Performance |
|--------|------------|
| Multiple Linear Regression | R² = **0.9884** |
| Decision Tree Regressor | Train R² = **1.0000**, Test R² = **0.9858** *(Overfitting observed)* |
| Random Forest Regressor | Train R² = **0.9992**, Test R² = **0.9941** *(Best Model)* |

### Best Model

 **Random Forest Regressor**

Reason:
- Highest prediction accuracy
- Excellent generalization
- Minimal overfitting
- Lowest prediction error

---

##  Evaluation Metrics

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

##  Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn
- Flask
- HTML
- CSS
- JavaScript

---

##  Project Structure

```
RideFare-AI-pricing-app
│
├── app.py
├── model.py
├── requirements.txt
├── dynamic_pricing_data.csv
├── EDA.ipynb
├── data.ipynb
├── model.ipynb
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/gunjan01-source/RideFare-AI-pricing-app.git
```

Move into the project directory

```bash
cd RideFare-AI-pricing-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

---

## Future Improvements

- SHAP Explainability
- XGBoost Regressor
- Hyperparameter Tuning
- Better UI Design
- Cloud Deployment (Render)

---

## Author

**Gunjan**

Aspiring Data Scientist | Machine Learning Enthusiast | Flask Developer

---

 If you found this project useful, consider giving it a star!
