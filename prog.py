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
    html.H1('ROLETA DE BANS E SKINS', style={'text-align': 'center', 'color': 'DodgerBlue'}),

    #Dropdown button
    dcc.Dropdown(id='slct_ban_skin',
                options=[
                    {'label':'BAN', 'value':'ban'},
                    {'label':'SKIN', 'value':'skin'}],
                multi=False,
                style=Settings().dropdown_style
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    #Drawer
    html.Div(id='output_drawer', children=[], style=Settings().div_style),
    html.Br(),
    html.Div(id='output_slctd', children=[], style=Settings().div_style)
])


"""The call back: connecting the app components with the Plotly graphics"""
@app.callback(
    [Output(component_id='output_drawer', component_property='children'),
    Output(component_id='output_slctd', component_property='children')],
    Input(component_id='slct_ban_skin', component_property='value')
)

def selector(opt):
    if opt == 'ban':
        phrase_slctd = RandomSelector().ban_select()[0]
        opt_slctd = RandomSelector().ban_select()[1]

    else:
        if opt == 'skin':
            phrase_slctd = RandomSelector().skin_select()[0]
            opt_slctd = RandomSelector().skin_select()[1]
        else:
            phrase_slctd = f'SELECIONE O SORTEADO!'
            opt_slctd = f''

    return phrase_slctd, opt_slctd


"""Run server"""
if __name__ == '__main__':
    app.run_server(debug=True)
