import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Function to generate synthetic data for population by age group and gender
def generate_synthetic_data():
    age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
    age_populations = [709_443_245, 720_045_847, 303_132_843]  # Adjusted to reflect more people in the 0-20 age group
    total_population = sum(age_populations)
    male_percentage = np.random.uniform(0.50, 0.52)
    male_population = int(total_population * male_percentage)
    female_population = total_population - male_population

    return pd.DataFrame({
        'Age Group': age_groups,
        'Population': age_populations,
        'Male': [int(p * male_percentage) for p in age_populations],
        'Female': [int(p * (1 - male_percentage)) for p in age_populations]
    }), male_population, female_population

# Load or generate data
age_df, male_population, female_population = generate_synthetic_data()

# Create bar chart for age distribution
fig_age = go.Figure()

# Add bar chart trace
fig_age.add_trace(go.Bar(
    x=age_df['Age Group'], 
    y=age_df['Population'], 
    marker_color='#FF9999',  # Lighter pinkish red color
    name='Population',
    text=age_df['Population'].apply(lambda x: f'{x:,}'),  # Add text labels
    textposition='auto'  # Auto position of text
))

# Update layout for age distribution chart
fig_age.update_layout(
    title={
        'text': 'Age Distribution in Population',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Age Group',
    yaxis_title='Population',
    template='plotly_white',
    barmode='group',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="Black"
    ),
    title_font=dict(
        family='Arial, sans-serif',
        size=20,
        color='Black'
    ),
    xaxis=dict(
        title_font=dict(
            family='Arial, sans-serif',
            size=18,
            color='Black'
        )
    ),
    yaxis=dict(
        title_font=dict(
            family='Arial, sans-serif',
            size=18,
            color='Black'
        )
    )
)

# Show the age distribution chart
fig_age.show()

# Create pie chart for gender distribution
fig_gender = go.Figure()

# Add pie chart trace
fig_gender.add_trace(go.Pie(
    labels=['Male', 'Female'], 
    values=[male_population, female_population], 
    marker_colors=['blue', 'yellow'], 
    name='Gender Distribution',
    textinfo='label+percent',
    hole=0.3  # Donut chart
))

# Update layout for gender distribution chart
fig_gender.update_layout(
    title={
        'text': 'Gender Distribution in Population',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    template='plotly_white',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="Black"
    ),
    title_font=dict(
        family='Arial, sans-serif',
        size=20,
        color='Black'
    )
)

# Show the gender distribution chart
fig_gender.show()
