# **Heart Disease Prediction System**

Heart disease is a serious worldwide health concern that affects individuals of all ages. Due to the complexity of cardiac disease, traditional risk assessment techniques frequently fail to accurately anticipate the condition. This study analyzes a variety of health-related parameters, including age, gender, blood pressure, and diabetes levels, in order to improve the accuracy of heart disease forecasts by utilizing advanced machine learning techniques.

## **Project Overview**

The goal of this research is to use machine learning techniques to create an advanced system for heart disease prediction. Through the integration of data from several sources and the application of distinct machine learning techniques, our goal is to furnish healthcare practitioners with significant insights. In addition to increasing prediction accuracy, our method places a strong emphasis on data privacy and ethical issues.

### **Key Features:**

- **Data Analysis**: Comprehensive analysis of heart disease datasets.
- **Multiple Models**: Implementation of various machine learning algorithms.
- **Web Interface**: A Flask web application for user interaction and predictions.
- **Prediction Accuracy**: Enhanced prediction capabilities through advanced techniques.
- **Ethical Considerations**: Prioritization of data privacy and ethical concerns.

## **Machine Learning Algorithms Used**
1. **Logistic Regression:** A statistical model that in its basic form uses a logistic function to model a binary dependent variable.
2. **Support Vector Machine (SVM):** A supervised learning model that finds the optimal hyperplane to separate different classes.
3. **K-Nearest Neighbours (KNN):** A non-parametric method that classifies data based on the majority label among the nearest neighbors.
4. **Decision Tree:** A model that splits the data into subsets based on different features to create a tree-like structure.
5. **Random Forest:** An ensemble method that uses multiple decision trees to improve prediction accuracy and control overfitting.
6. **Gradient Boosting:** A technique that builds models sequentially to correct errors made by previous models.
7. **Ensemble Model (Voting Classifier)**

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Flask
- Required Python libraries (listed in `requirements.txt`)

**Navigate to the project directory:**
```bash 
cd heart-disease-prediction
```

**Install required libraries:**
```bash
pip install -r requirements.txt
```

## Running the Machine Learning Models
1. Open and run the Jupyter Notebook to analyze the dataset and train the models.
2. Train and save the model:
   - The trained ensemble model is saved as `model_heart` using `joblib`.

## Running the Flask Web Application
1. Navigate to the directory containing app.py.
2. Run the Flask application:
```bash
python app.py
```
3. Open your web browser and go to `http://127.0.0.1:5000` to access the prediction interface.

## Dataset
The dataset used in this project is named `heart_disease.csv` and should be placed in the same directory as the Jupyter Notebook.

## Acknowledgements
- Kaggle for providing the dataset.
- Various libraries and frameworks used in this project.























