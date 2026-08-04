# 🚖 RideFare AI Pricing App

An AI-powered Dynamic Pricing Prediction System built using **Machine Learning** and **Flask**. The application predicts the optimal ride fare based on real-time market conditions such as customer demand, driver availability, competitor pricing, distance, season, discounts, and customer ratings.

---

# 📌 Project Overview

Dynamic pricing is widely used in ride-hailing and e-commerce platforms to automatically adjust prices according to changing market conditions.

This project demonstrates an end-to-end Machine Learning workflow by:

- Generating a realistic synthetic dataset
- Performing Exploratory Data Analysis (EDA)
- Engineering new features
- Training multiple regression models
- Comparing model performance
- Deploying the best-performing model with Flask
- Creating an interactive web interface for fare prediction

---

# ✨ Features

- 📊 Synthetic data generation
- 📈 Exploratory Data Analysis (EDA)
- 🧹 Data preprocessing
- ⚙️ Feature Engineering
- 🤖 Multiple Machine Learning models
- 🏆 Best model selection
- 🌐 Flask Web Application
- 🎨 Interactive frontend (HTML, CSS & JavaScript)
- 📉 Performance evaluation using multiple metrics

---

# 📂 Dataset Features

| Feature | Description |
|---------|-------------|
| Demand | Current customer demand |
| Stock | Available drivers/resources |
| CompetitorPrice | Competitor ride price |
| Season | Seasonal condition |
| DayTime | Time of the day |
| CustomerRating | Customer rating |
| Discount | Discount applied |
| HistoricalSales | Historical ride demand |
| Distance_km | Trip distance |
| Price | Target variable |

---

# 🤖 Machine Learning Models

The following regression models were implemented and evaluated:

- Multiple Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

# 📊 Model Performance

| Model | Performance |
|--------|------------|
| Multiple Linear Regression | **R² = 0.9884** |
| Decision Tree Regressor | **Train R² = 1.0000**<br>**Test R² = 0.9858** *(Overfitting observed)* |
| Random Forest Regressor | **Train R² = 0.9992**<br>**Test R² = 0.9941** ✅ *(Best Model)* |

---

# 🏆 Best Model

### Random Forest Regressor

### Why?

- Highest prediction accuracy
- Excellent generalization
- Minimal overfitting
- Lowest prediction error
- Most reliable performance on unseen data

---

# 📈 Evaluation Metrics

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

# 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- NumPy
- Pandas
- Scikit-Learn

### Data Visualization
- Matplotlib

### Frontend
- HTML
- CSS
- JavaScript

---

# 📁 Project Structure

```text
RideFare-AI-pricing-app
│
├── images/
│   ├── home.png
│   └── prediction.png
│
├── app.py
├── model.py
├── requirements.txt
├── dynamic_pricing_data.csv
├── EDA.ipynb
├── data.ipynb
├── model.ipynb
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# 📸 Screenshots

## 🏠 Home Page

<img width="3200" height="1904" alt="Screenshot 2026-08-04 103437" src="https://github.com/user-attachments/assets/9d20f757-8080-4147-89da-9c379891b1e8" />


The application provides a clean interface where users can enter ride information including demand, available drivers, competitor pricing, discounts, customer ratings, trip distance, season, and time of day.

---

## 💰 Fare Prediction

<img width="3200" height="1904" alt="Screenshot 2026-08-04 103501" src="https://github.com/user-attachments/assets/8c6ec75c-cdab-40f2-9e67-c22b118244ef" />


After submitting the trip details, the trained **Random Forest Regressor** predicts the estimated ride fare in real time.

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/gunjan01-source/RideFare-AI-pricing-app.git
```

### Navigate to the project directory

```bash
cd RideFare-AI-pricing-app
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

# 🔮 Future Improvements

- SHAP Explainability
- XGBoost Regressor
- Hyperparameter Tuning
- Cross Validation
- Docker Support
- REST API
- User Authentication
- Cloud Deployment (Render / Railway / Azure)
- CI/CD using GitHub Actions

---

# 👩‍💻 Author

**Gunjan**

Aspiring Data Scientist • Machine Learning Enthusiast • Flask Developer

- 🌟 Passionate about Machine Learning and AI
- 📊 Interested in Data Science and Analytics
- 🚀 Currently building end-to-end ML projects

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps support my work and motivates me to build more Machine Learning projects!
