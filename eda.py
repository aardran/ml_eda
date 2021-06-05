import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Public Perception of Artificial Intelligence")
df = pd.read_csv('data.csv')
tips= df.head(10)
st.table(tips)
st.header("Visualisation Using Seaborn")
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()
st.subheader("Displot")
sns.displot(tips['WorkTimeInSeconds'])
st.pyplot()
st.subheader("JointPlot")
sns.jointplot(x='WorkTimeInSeconds',y='AI Mood',data=tips,kind='scatter')
st.pyplot()

st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()