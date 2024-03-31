import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Cargar datos
data = pd.read_csv("C:\\Users\\nicoa\\Desktop\\notas.csv", sep=';')

# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1(children='Dashboard de Estudiantes', style={'textAlign': 'center'}),
    dcc.Graph(id='scatter-plot'),
    html.Div([
        html.Label("Seleccionar una opción:"),
        dcc.Dropdown(
            id='option-dropdown',
            options=[
                {'label': 'Por Nota', 'value': 'Nota'},
                {'label': 'Por Género', 'value': 'Genero'},
                {'label': 'Por Edad', 'value': 'Edad'}
            ],
            value='Nota',  # Valor inicial
            clearable=False,  # No permitir borrar la selección
            style={'width': '50%'}
        ),
    ]),
])

# Callback para actualizar el gráfico de dispersión según la opción seleccionada
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('option-dropdown', 'value')]
)
def update_scatter_plot(selected_option):
    if selected_option == 'Nota':
        fig = px.scatter(data, x='Horas', y='Nota', color='Genero', title="Relación entre horas de estudio y notas")
    elif selected_option == 'Genero':
        fig = px.scatter(data, x='Horas', y='Nota', color='Genero', facet_col='Genero', title="Relación entre horas de estudio y notas por género")
    elif selected_option == 'Edad':
        fig = px.scatter(data, x='Horas', y='Nota', color='Genero', facet_col='Edad', title="Relación entre horas de estudio y notas por edad")
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)



