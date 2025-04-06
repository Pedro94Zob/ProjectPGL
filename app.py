import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de suivi TSLA"),
    html.P("Si vous voyez ce texte, le layout fonctionne."),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000,  # 5 minutes
        n_intervals=0
    )
])

@app.callback(
    dash.dependencies.Output('live-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    try:
        df = pd.read_csv("data.csv", names=["datetime", "price"])
    except Exception:
        df = pd.DataFrame(columns=["datetime", "price"])
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    data = go.Scatter(
        x=df["datetime"],
        y=df["price"],
        mode='lines+markers'
    )
    layout = go.Layout(
        title='Évolution du prix TSLA en temps réel',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Prix')
    )
    return {'data': [data], 'layout': layout}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
