import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("pink_morsels_sales.csv")

# Convert date column to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    labels={
        "date": "Date",
        "sales": "Sales"
    },
    title="Pink Morsels Sales Over Time"
)

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

