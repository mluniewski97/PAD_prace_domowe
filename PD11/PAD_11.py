from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/michalluniewski/Documents/PAD/11_PAD/Zadanie domowe/winequelity.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Wine Quality'),
    generate_table(df),

    html.Br(),
    html.Label('Wybór modelu'),
    dcc.Dropdown(['Regresja','Klasyfikacja'], 'Regresja', id='model_choice'),
    html.Label('Wybór parametru'),
    dcc.Dropdown(['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol'], 'alcohol', id='parameter_choice'),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('model_choice', 'value'),
    Input('parameter_choice', 'value'))
def update_figure(model_choice, parameter_choice):

    if model_choice == 'Regresja':
        compared = 'pH'
        fig = px.scatter(df, x=parameter_choice, y=compared)
    else:
        compared = 'target'
        fig = px.box(df, x=parameter_choice, y=compared)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)