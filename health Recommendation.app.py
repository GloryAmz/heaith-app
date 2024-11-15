import pandas as pd
import numpy as np
df = pd.read_csv('update_data.csv')
df
def add_aggregate_metrics(df):
    df['avg_daily_steps'] = df.groupby('user_id')['steps'].transform('mean')
    df['avg_weekly_calories'] = df.groupby('user_id')['calories'].transform(lambda x: x.rolling(7).mean())
    return df

def add_health_ratios(df):
    df['activity_to_rest_ratio'] = df['steps'] / df['rest']
    return df
from sklearn.cluster import KMeans

def cluster_users(df, num_clusters=3):
    kmeans = KMeans(n_clusters=num_clusters)
    df['fitness_profile'] = kmeans.fit_predict(df[['avg_daily_steps', 'BMI', 'calorie_intake']])
    return df
def collaborative_filtering_recommendation(user_data):
    
    pass

def rule_based_recommendation(user_row):
    if user_row['fitness_profile'] == 0:
        return "Increase daily steps, try light activities like walking, and reduce calorie intake."
    elif user_row['fitness_profile'] == 1:
        return "Maintain current activity level, add strength training twice a week, keep balanced diet."
    elif user_row['fitness_profile'] == 2:
        return "Focus on recovery with stretching and hydration, increase protein intake for muscle repair."
    else:
        return "Custom recommendation based on goals."

def apply_recommendations(df):
    df['recommendation'] = df.apply(rule_based_recommendation, axis=1)
    return df
print(df.columns)
from sklearn.tree import DecisionTreeClassifier

def train_recommendation_model(X, y):
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model

def evaluate_recommendations(df, feedback_column):
    
    satisfaction_score = df[feedback_column].mean()
    return satisfaction_score
import pandas as pd
import streamlit as st

def load_data():
    return pd.read_csv("update_data.csv")

def generate_recommendation(row):
    if row['avg_daily_steps'] < 5000:
        return "Increase daily steps to improve health."
    elif row['bmi'] > 25:
        return "Consider a balanced diet and regular exercise to manage bmi."
    else:
        return "Maintain current healthy lifestyle."

def show_dashboard():
    st.title("Personalized Health Recommendation System")
    df = load_data()
    
    
    df['recommendation'] = df.apply(generate_recommendation, axis=1)
    
    st.dataframe(df[['user_id', 'recommendation', 'avg_daily_steps', 'bmi']])

if __name__ == "__main__":
    show_dashboard()
pip install pandas streamlit

import streamlit as st
st.title("Health Recommendation App")
st.header("Welcome!")
st.write("This is where content will go.")
