import os
import streamlit as st
import pandas as pd

st.write("Current directory:", os.getcwd())
st.write("Files:", os.listdir("."))

df = pd.read_csv("final_employee_analysis.csv")
import streamlit as st
import pandas as pd

df = pd.read_csv("final_employee_analysis.csv")

st.title("Career Progression and Promotion Gap Analysis")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Total Employees")
st.write(len(df))



import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("final_employee_analysis.csv")

# Title
st.title("Career Progression and Promotion Gap Analysis")

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Employees", len(df))

with col2:
    st.metric("Departments", df['Department'].nunique())

with col3:
    st.metric("Job Roles", df['JobRole'].nunique())

# Sidebar Filters
st.sidebar.header("Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df['Department'].unique())
)

# Filter Logic
if department != "All":
    filtered_df = df[df['Department'] == department]
else:
    filtered_df = df

# Dataset Preview
st.subheader("Filtered Dataset")
st.dataframe(filtered_df.head())

# Cluster Distribution
st.subheader("Career Cluster Distribution")

cluster_counts = filtered_df['CareerCluster'].value_counts()

st.bar_chart(cluster_counts)



st.subheader("Promotion Gap Monitor")

high_gap = filtered_df[
    filtered_df['PromotionGapScore'] == 'High'
]

st.write("High Promotion Gap Employees:", len(high_gap))

st.dataframe(
    high_gap[[
        'Age',
        'Department',
        'JobRole',
        'PromotionGapScore',
        'RetentionOpportunityIndex'
    ]]
)




st.subheader("Retention Opportunity Panel")

retention_opportunity = filtered_df[
    (filtered_df['Attrition'] == 0) &
    (filtered_df['PromotionGapScore'] == 'High')
]

st.write(
    "Employees Requiring Career Intervention:",
    len(retention_opportunity)
)

st.dataframe(
    retention_opportunity[[
        'Department',
        'JobRole',
        'PromotionGapScore',
        'RetentionOpportunityIndex',
        'TrainingNeedIndicator'
    ]]
)



st.subheader("Managerial Insight Dashboard")

manager_growth = filtered_df.groupby(
    'YearsWithCurrManager'
)['RetentionOpportunityIndex'].mean()

st.line_chart(manager_growth)

role = st.sidebar.selectbox(
    "Select Job Role",
    ["All"] + list(df['JobRole'].unique())
)

if role != "All":
    filtered_df = filtered_df[
        filtered_df['JobRole'] == role
    ]

cluster = st.sidebar.selectbox(
    "Select Career Cluster",
    ["All"] + list(df['CareerCluster'].unique())
)

if cluster != "All":
    filtered_df = filtered_df[
        filtered_df['CareerCluster'] == cluster
    ]


threshold = st.sidebar.slider(
    "Retention Opportunity Threshold",
    0.0,
    1.0,
    0.5
)


high_priority = filtered_df[
    filtered_df['RetentionOpportunityIndex'] >= threshold
]



