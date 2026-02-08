import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("pink_morsels_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize app
app = Dash(__name__)

# App layout with radio buttons and styling
app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'Arial'}, children=[
    html.H1("Pink Morsels Sales Visualiser", style={'color': '#d63384'}),

    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin': '0 10px'}
        )
    ], style={'marginBottom': '20px'}),

    dcc.Graph(id='sales-line-chart', style={'height': '600px'})
])

# Callback to update graph based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]
    
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        labels={'date': 'Date', 'sales': 'Sales'},
        title=f"Pink Morsels Sales Over Time - Region: {selected_region.capitalize()}"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
