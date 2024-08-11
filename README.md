# Penguin Species Predictor

## Overview

Welcome to the Penguin Species Predictor app! This Streamlit application allows users to input features of penguins and predict their species using a RandomForestClassifier model trained on the [Penguin dataset](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv). 

## Features

- **Data Exploration:** View the raw data, feature sets, and the distribution of penguin features.
- **Visualization:** Scatter plot visualizing the relationship between bill length and body mass of penguins.
- **User Input:** Enter features of a penguin such as island, bill length, bill depth, flipper length, body mass, and gender.
- **Model Prediction:** The app uses a RandomForestClassifier to predict the species of the penguin based on the input features.
- **Prediction Probability:** See the probability distribution of the prediction across different species.

## Getting Started

To run this application locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ahmed9588406/Penguin-Species-Predictor.git
   cd penguin-species-predictor
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then use pip to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Launch the Streamlit app with:
   ```bash
   streamlit run app.py
   ```

4. **Access the App:**
   Open your web browser and go to `http://localhost:8501` to use the app.

## Features and Functionality

- **Data Exploration:** Provides an overview of the dataset, including raw data, features, and labels.
- **Visualization:** Displays a scatter plot to help visualize the relationship between bill length and body mass.
- **User Input Form:** Allows you to enter the features of a penguin and get predictions.
- **Prediction Results:** Shows the predicted species along with the probability distribution for each species.

## Model Details

- **Model Used:** RandomForestClassifier
- **Dataset:** The app uses a cleaned version of the penguins dataset with features including island, bill dimensions, flipper length, body mass, and gender.

## Acknowledgements

- **Dataset:** [Penguin Dataset](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv)
- **Streamlit:** For creating interactive web apps with Python.
- **Scikit-Learn:** For machine learning models and tools.
