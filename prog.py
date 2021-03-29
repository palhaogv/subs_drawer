import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from settings import Settings
from draw import RandomSelector



'''Starting the app'''
app = dash.Dash(__name__)


"""App layout"""
app.layout = html.Div([
    #Header
    html.H1('ROLETA DE BANS E SKINS', style={'text-align': 'center', 'color': 'blue'}),

    #Dropdown button
    dcc.Dropdown(id='slct_ban_skin',
                options=[
                    {'label':'ban', 'value':'ban'},
                    {'label':'skin', 'value':'skin'}],
                multi=False,
                style={'width': '40%'}
    ),

    html.Br(),
    #Drawer
    html.Div(id='output_drawer', children=[])
])


"""The call back: connecting the app components with the Plotly graphics"""
@app.callback(
    Output(component_id='output_drawer', component_property='children'),
    Input(component_id='slct_ban_skin', component_property='value')
)

def selector(opt):
    if opt == 'ban':
        opt_slcted = RandomSelector().ban_select()

    else:
        if opt == 'skin':
            opt_slcted = RandomSelector().skin_select()
        else:
            opt_slcted = f'SORTEADOR'

    return opt_slcted


"""Run server"""
if __name__ == '__main__':
    app.run_server(debug=True)
