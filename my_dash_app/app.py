#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

df=pd.read_csv("/Users/kyriakospapadopoulos/Desktop/University/Big Blue Data Academy/Bootcamp Data Analytics/kyriakos-papadopoulos-exercises/Power BI/Project 2/Assets/lung_cancer_mortality_data_large.csv")


# Function to interpret BMI values
def interpret_bmi(bmi):
    if 0 <= bmi <= 18.4:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 100:
        return "Obese"
    else:
        return "Unknown"

# Apply the function to create the new column
df['BMI_Interpretation'] = df['bmi'].apply(interpret_bmi)

# Define the conditions and corresponding values for the Age_Group column
conditions = [
    (df['age'] >= 0) & (df['age'] < 10),
    (df['age'] >= 10) & (df['age'] < 20),
    (df['age'] >= 20) & (df['age'] < 30),
    (df['age'] >= 30) & (df['age'] < 40),
    (df['age'] >= 40) & (df['age'] < 50),
    (df['age'] >= 50) & (df['age'] < 60),
    (df['age'] >= 60) & (df['age'] < 70),
    (df['age'] >= 70) & (df['age'] < 80),
    (df['age'] >= 80) & (df['age'] < 90),
    (df['age'] >= 90) & (df['age'] <= 100)
]

age_groups = [
    "0-10",
    "10-20",
    "20-30",
    "30-40",
    "40-50",
    "50-60",
    "60-70",
    "70-80",
    "80-90",
    "90-100"
]

# Apply the conditions to create the Age_Group column
df['Age_Group'] = np.select(conditions, age_groups, default='Unknown')

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        html.H1("Correlation Dashboard", style={'textAlign': 'center'}),
    ),
    
    dcc.Graph(id='correlation-graph'),

    html.Div([
        html.Label('Age Group'),
        dcc.Dropdown(
            id='age-group-dropdown',
            options=[{'label': group, 'value': group} for group in df['Age_Group'].unique()],
            multi=True,
            placeholder='Select age group'
        ),
    ], style={'padding': '10px'}),
    
    html.Div([
        html.Label('Country'),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in df['country'].unique()],
            multi=True,
            placeholder='Select country'
        ),
    ], style={'padding': '10px'}),
    
    html.Div([
        html.Label('Family History'),
        dcc.Dropdown(
            id='family-history-dropdown',
            options=[{'label': history, 'value': history} for history in df['family_history'].unique()],
            multi=True,
            placeholder='Select family history'
        ),
    ], style={'padding': '10px'}),
    
    html.Div([
        html.Label('Cancer Stage'),
        dcc.Dropdown(
            id='cancer-stage-dropdown',
            options=[{'label': stage, 'value': stage} for stage in df['cancer_stage'].unique()],
            multi=True,
            placeholder='Select cancer stage'
        ),
    ], style={'padding': '10px'}),
])

# Callback to update the graph based on filters
@app.callback(
    Output('correlation-graph', 'figure'),
    [
        Input('age-group-dropdown', 'value'),
        Input('country-dropdown', 'value'),
        Input('family-history-dropdown', 'value'),
        Input('cancer-stage-dropdown', 'value')
    ]
)
def update_graph(selected_age_group, selected_country, selected_history, selected_stage):
    filtered_df = df.copy()
    
    if selected_age_group:
        filtered_df = filtered_df[filtered_df['Age_Group'].isin(selected_age_group)]
    if selected_country:
        filtered_df = filtered_df[filtered_df['country'].isin(selected_country)]
    if selected_history:
        filtered_df = filtered_df[filtered_df['family_history'].isin(selected_history)]
    if selected_stage:
        filtered_df = filtered_df[filtered_df['cancer_stage'].isin(selected_stage)]
    
    # Select the relevant columns for correlation
    numeric_columns = ['age', 'bmi', 'cholesterol_level', 'hypertension', 'asthma', 'cirrhosis', 'other_cancer']
    correlation_data = filtered_df[numeric_columns + ['survived']]
    
    # Calculate the correlation with the 'survived' column
    correlation_matrix = correlation_data.corr()
    survived_correlation = correlation_matrix['survived'].drop('survived')  # Drop self-correlation
    
    # Convert correlation to a DataFrame for Plotly
    correlation_df = survived_correlation.reset_index()
    correlation_df.columns = ['Variable', 'Correlation']
    
    # Plot the correlation using Plotly Express
    corr = px.bar(correlation_df, x='Variable', y='Correlation',
                  title='Correlation of Variables with Survived',
                  labels={'Variable': 'Variables', 'Correlation': 'Correlation coefficient'},
                  template='seaborn')
    
    # Update bar color
    corr.update_traces(marker_color='#6ebfb5')  # Replace with your desired color
    
    return corr

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




