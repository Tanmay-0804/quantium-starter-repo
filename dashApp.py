from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('pink_morsel_sales.csv')
df = df.sort_values(by=['date'])
fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales')
# fig.show()


app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    # html.Div(children='''
    #     Dash: A web application framework for your data.
    # '''),

    dcc.Graph(
        id='Sales Graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)