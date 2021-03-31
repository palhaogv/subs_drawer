import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from settings import Settings
from draw import RandomSelector


'''Starting the app'''
app = dash.Dash(__name__)

"""App layout"""
app.layout = html.Div(
    [
    #Header
    html.H1('ROLETA DE BANS E SKINS DO BT0', style=Settings().header_style),

    #Dropdown button
    dcc.Dropdown(id='slct_ban_skin',
                options=[
                    {'label':'BAN', 'value':'ban'},
                    {'label':'SKIN', 'value':'skin'}],
                multi=False,
                style=Settings().dropdown_style
    ),

    html.Br(style=Settings().bracket_style1),

    #Drawer
    html.Div(id='output_drawer', children=[], style=Settings().div_style1),

    html.Br(style=Settings().bracket_style2),

    html.Div(id='output_slctd_ban', children=[], style=Settings().div_style_ban),
    html.Div(id='output_slctd_skin', children=[], style=Settings().div_style_skin),

    ], style= Settings().background_style)


"""Connecting the app components with the machine functions"""
@app.callback(
    [Output(component_id='output_drawer', component_property='children'),
    Output(component_id='output_slctd_ban', component_property='children'),
    Output(component_id='output_slctd_skin', component_property='children')],
    Input(component_id='slct_ban_skin', component_property='value')
)

def selector(opt):
    if opt == 'ban':
        phrase_slctd = RandomSelector().ban_select()[0]
        opt_slctd_ban = RandomSelector().ban_select()[1]
        opt_slctd_skin = ''
        print(f'Olá, {opt_slctd_ban}, a máquina de bans e skins te sorteou, voce está banido!')

    else:
        if opt == 'skin':
            phrase_slctd = RandomSelector().skin_select()[0]
            opt_slctd_skin = RandomSelector().skin_select()[1]
            opt_slctd_ban = ''
            print(f'Olá, {opt_slctd_skin}, a máquina de bans e skins te sorteou, voce acaba de ganhar uma SKIN! Parabéns, me responda com seu tradelink para que eu possa te envia-la.')
        else:
            phrase_slctd = f'SELECIONE O SORTEADO!'
            opt_slctd_ban = f''
            opt_slctd_skin = f''

    return phrase_slctd, opt_slctd_ban, opt_slctd_skin


"""Run server"""
if __name__ == '__main__':
    app.run_server(debug=True)
