import streamlit as st
import pandas as pd

# Create some example data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Title
st.title('Simple Dashboard')

# Subtitle
st.write('Exploring some data')

# Display the data
st.write('### Data')
st.write(df)

# Bar chart of ages
st.write('### Bar Chart of Ages')
st.bar_chart(df['Age'])

# Line chart of salaries
st.write('### Line Chart of Salaries')
st.line_chart(df['Salary'])

# Table
st.write('### Data Table')
st.table(df)
