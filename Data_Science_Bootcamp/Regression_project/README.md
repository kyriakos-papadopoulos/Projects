# Household Income Prediction Using Regression Techniques

## Overview

This project involves analyzing and predicting household income using various regression techniques. Conducted as part of the Data Science Bootcamp from Big Blue Data Academy, it aims to explore the relationships between demographic and socioeconomic factors and to evaluate the performance of different machine learning models in predicting annual household income.

- **Date Completed:** July 13, 2024

## Table of Contents

- [Objectives](#objectives)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Tools and Libraries](#tools-and-libraries)
- [Results](#results)
- [Model Interpretation](#model-interpretation)
- [Conclusion](#conclusion)
- [Notebooks](#notebooks)
- [Presentation](#presentation)
- [Acknowledgments](#acknowledgments)

## Objectives

The primary objectives of this project were:

- **Exploratory Data Analysis (EDA):** Understand the dataset by assessing data distributions and identifying skewness.
- **Data Preprocessing:** Prepare the data for modeling by encoding categorical variables and handling ordinal features.
- **Model Building:** Develop and evaluate regression models for predicting household income.
- **Model Interpretation:** Use SHAP and LIME to interpret the models and gain insights into feature importance.

## Dataset

The dataset is a synthetic representation of various demographic and socioeconomic factors that influence annual household income. It includes features such as age, education level, occupation, number of dependents, location, work experience, and more.

- **Source:** [Kaggle - Regression Dataset for Household Income Analysis](https://www.kaggle.com/datasets/stealthtechnologies/regression-dataset-for-household-income-analysis)
- **Target Variable:** `Annual Household Income` (in USD)

## Methodology

The project followed a structured machine learning workflow:

1. **Exploratory Data Analysis:**
   - Assessed data distributions using summary statistics, box plots, and violin plots.
   - Identified skewness in the `Income` variable and applied a logarithmic transformation.

2. **Data Preprocessing:**
   - Encoded categorical variables using One-Hot Encoding.
   - Handled ordinal features by manual encoding.
   - Constructed pipelines for data transformation.

3. **Model Training:**
   - Evaluated multiple regression models:
     - Linear Regression
     - Lasso Regression
     - Ridge Regression
     - Decision Trees
     - Random Forest
     - XGBoost
   - Used GridSearchCV for hyperparameter tuning.

4. **Model Evaluation:**
   - Applied cross-validation with metrics:
     - Mean Squared Error (MSE)
     - Mean Absolute Error (MAE)
     - R² Score
   - Used Stratified K-Fold cross-validation to handle target variable distribution.

5. **Interpretability:**
   - Applied SHAP (SHapley Additive exPlanations) to interpret global feature importance.
   - Used LIME (Local Interpretable Model-agnostic Explanations) for local instance explanations.
   - Generated Partial Dependence Plots to visualize feature effects.

## Tools and Libraries

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** scikit-learn, XGBoost
- **Model Interpretability:** SHAP, LIME

## Results

Despite rigorous modeling efforts, the models yielded low predictive performance:

- **R² Scores:** Ranged from approximately 0.02 to 0.09.
- **Best Model:** XGBoost with an R² score of about 0.09.
- **Observations:**
  - **Low Correlations:** Most features had low correlations with the target variable.
  - **Counterintuitive Findings:** Some model interpretations contradicted real-world expectations.

## Model Interpretation

### SHAP Analysis

- **Key Features:**
  - `Homeownership_Status_Rent`: Renting was associated with higher predicted income, which is counterintuitive.
  - `Location_Urban`: Urban locations were linked to higher predicted income levels.
  - `Type_of_Housing_Single-family home`: Positive impact on income predictions.
  - `Employment_Status_Part-time`: Part-time employment associated with lower predicted income.

### LIME Explanations

- Provided local explanations for individual predictions.
- Due to low model performance, these interpretations were of limited practical value.

### Partial Dependence Plots

- Visualized the marginal effect of features on the predicted outcome.
- Revealed some unexpected trends, reinforcing the need for careful data examination.

## Conclusion

The project demonstrated that:

- **Data Quality Matters:** The synthetic datasets lack of meaningful relationships limited the predictive power of the models.
- **Model Limitations:** Even advanced models like XGBoost cannot compensate for inadequate data.
- **Importance of EDA:** Early identification of data issues is crucial for realistic modeling expectations.

## Notebooks

- **Exploratory Data Analysis Notebook:** [income_analysis.ipynb](notebooks/income_analysis.ipynb)
- **Modeling Notebook:** [income_modeling.ipynb](notebooks/income_modeling.ipynb)

## Presentation

A presentation summarizing the project findings is available:

- [Project Presentation](https://kyriakos-papadopoulos.com/projects/household-income-prediction)

## Acknowledgments

- **Big Blue Data Academy:** For providing the opportunity and resources to undertake this project.
- **Kaggle:** For the synthetic dataset used in the analysis.
- **Open-Source Community:** For the development and maintenance of the tools and libraries used.
