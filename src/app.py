from dash import dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import altair as alt
# from vega_datasets import data
# Handle large data sets without embedding them in the notebook
# alt.data_transformers.enable('data_server')
# Include an image for each plot since Gradescope only supports displaying plots as images
# alt.renderers.enable('mimetype')
# alt.renderers.enable('default')


# Data - Loading and Pre-processing
raw = pd.read_csv(r'../data/player_stats.csv')
player = raw[['Player', 'Year', 'Pos', 'Tm', 'G',
             'FG%', 'FT%', '3P%', 'ORB%', 'AST%', 
             'BLK%', 'DRB%', 'STL%'
            ]]
player = player.fillna(0)
player = player.rename(columns={'Player':'Name','Tm':'Team','G':'Game',
             'FG%':'FGp', 'FT%':'FTp', '3P%':'3Pp', 'ORB%':'ORBp', 'AST%':'ASTp', 
             'BLK%':'BLKp', 'DRB%':'DRBp', 'STL%':'STLp'
            })
# player = player.tail(3000)
player['Year'] = player['Year'].astype(int)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX]) 
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED]) 
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA]) 
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL]) 
server = app.server
app.title = 'NBA Player Comparison'



# Front-end - START
app.layout = html.Div([

    # Row1 = Title and Logo
    html.Div(
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            # 'height': '5vh'
        },
        children=[
        # html.Img(src='/img/nba_logo.jpg'),
        # html.Img(src=dash.get_asset_url('img/nba_logo.png')),
        html.H1('NBA Player Statistics Comparison', style={'textAlign': 'center', 'align-items':'center', 'justify-content':'center'})
        ]
    ),

    # Row2 = Search players
    dbc.Row([
        dbc.Card([
        # Col - Player A
            dbc.Col([
                html.H4('Select Player A'),
                # Dropdown - Player A
                dcc.Dropdown(
                    id='dd_player_A', 
                    style={'height':'40px', 'align-items':'center', 'justify-content':'center', 'font-weight': 'bold'},
                    value = 'LeBron James',
                    options = player['Name'].unique(),
                    multi = False,
                    placeholder = 'Select player A'),
                    html.P(""),
                html.P('Last 5 years data', style={'text-decoration': 'underline'}),
                dash_table.DataTable(
                    id='datatable_A',
                    columns=[{'name': i, 'id': i} for i in player.columns],
                    data=player.to_dict('records')
                )
            ], style={'textAlign': 'center'})
        ],style={'width': '60rem'}),

        dbc.Card([
            # Col - Player B
            dbc.Col([
                html.H4("Select Player B"),
                # Dropdown - Player B
                dcc.Dropdown(
                    id='dd_player_B', 
                    style={'height':'40px', 'align-items':'center', 'justify-content':'center', 'font-weight': 'bold'},
                    value = 'Kobe Bryant',
                    options = player['Name'].unique(),
                    multi = False,
                    placeholder = 'Select player B'),
                html.P(""),
                html.P('Last 5 years data', style={'text-decoration': 'underline'}),
                dash_table.DataTable(
                    id='datatable_B',
                    columns=[{'name': i, 'id': i} for i in player.columns],
                    data=player.to_dict('records')
                )
            ], style={'textAlign': 'center'})
        ],style={'width': '59rem'})

    ], style={'textAlign': 'center'}),

    # Row3 - Offensive Dropdown
    html.P(""),
    html.P(""),
    html.H4("Offensive Statistics Comparison", style={'text-align': 'center'}),
    html.Div(
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            # 'height': '5vh'
        },
        children=[
            dcc.Dropdown(
            id='dd_off_stat', 
            style={'height':'30px', 'width':'300px'},
            value = 'FGp',
            options=[
            {'label': 'Field Goal Percentage', 'value': 'FGp'},
            {'label': 'Free Throw Percentage', 'value': 'FTp'},
            {'label': '3-Point Percentage', 'value': '3Pp'},
            {'label': 'Offensive Rebound Percentage', 'value': 'ORBp'},
            {'label': 'Assist Percentage', 'value': 'ASTp'}
            ],
            multi = False,
            placeholder = 'Select Off. stats')
        ]
    ),

    # Row4 - Offensive Plot
    html.Div(
            style={
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                # 'height': '45vh'
            },
            children=[
                html.Iframe(
                        id='plot_off',
                        style={
                                'border-width': '0',
                                # 'width': '100%', 
                                'width': '850px', 
                                'height': '280px', 
                                'justify-content': 'center',
                                'align-items': 'center'
                                }
                    )
            ]
    ),

    # Row5 - Defensive Dropdown
    html.H4("Defensive Statistics Comparison", style={'text-align': 'center'}),
    html.Div(
        style={
            'display': 'flex',
            'textAlign': 'center',
            'justify-content': 'center',
            'align-items': 'center',
            # 'height': '10vh'
        },
        children=[
            dcc.Dropdown(
            id='dd_def_stat', 
            style={'height':'30px', 'width':'300px'},
            value = 'BLKp',
            options=[
            {'label': 'Block Percentage', 'value': 'BLKp'},
            {'label': 'Defensive Rebound Percentage', 'value': 'DRBp'},
            {'label': 'Steal Percentage', 'value': 'STLp'}
            ],
            multi = False,
            placeholder = 'Select Off. stats')
        ]
    ),

    # Row6 - Defensive Plot
    html.Div(
            style={
                'display': 'flex',
                'textAlign': 'center',
                'justify-content': 'center',
                'align-items': 'center',
                # 'height': '45vh'
            },
            children=[
                html.Iframe(
                        id='plot_def',
                        style={
                                'border-width': '0', 
                                'width': '850px', 
                                'height': '280px',  
                                'justify-content': 'center',
                                'align-items': 'center'
                                }
                    )
            ]
    )
    

],style={
            # 'display': 'flex',
            # 'justify-content': 'center',
            'align-items': 'center',
        })
# Front-end - FINISH


# Backend - START
@app.callback(
    Output('datatable_A', 'data'),
    Output('datatable_B', 'data'),
    Output('plot_off', 'srcDoc'),
    Output('plot_def', 'srcDoc'),
    Input('dd_player_A', 'value'),
    Input('dd_player_B', 'value'),
    Input('dd_off_stat', 'value'),
    Input('dd_def_stat', 'value')
)

def plot_altair(player_A, player_B, off_selection, def_selection, df=player.copy()):

    df['Year'] = df['Year'].astype(int)
    filter_playerA = df.loc[(df['Name']==player_A)].tail(5)
    filter_playerB = df.loc[(df['Name']==player_B)].tail(5)
    filter_player = df.loc[(df['Name']==player_A) | (df['Name']==player_B)]
    x_min=filter_player['Year'].min()
    x_max=filter_player['Year'].max()

    off_stat = ''
    if off_selection == 'FGp':
        off_stat = 'Field Goal Percentage'
    elif off_selection == 'FTp':
        off_stat = 'Free Throw Percentage'
    elif off_selection == '3Pp':
        off_stat = '3-Point Percentage'
    elif off_selection == 'ORBp':
        off_stat = 'Offensive Rebound Percentage'
    elif off_selection == 'ASTp':
        off_stat = 'Assist Percentage'
    else: off_stat = ''
    
    off_title = off_stat + " Comparison"
    chart_off1 = alt.Chart(filter_player, title=alt.TitleParams(
        text=off_title,
        anchor='start')).mark_point().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max)), axis=alt.Axis(labelExpr="format(datum.value, 'd')")),
        y = alt.Y(off_selection, title=off_stat),
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
    )
    chart_off2 = alt.Chart(filter_player, title=alt.TitleParams(
        text=off_title,
        anchor='start')).mark_line().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max)), axis=alt.Axis(labelExpr="format(datum.value, 'd')")),
        y = alt.Y(off_selection, title=off_stat),
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
    )
    chart_off = chart_off1 + chart_off2

    def_stat = ''
    if def_selection == 'BLKp':
        def_stat = 'Block Percentage'
    elif def_selection == 'DRBp':
        def_stat = 'Defensive Rebound Percentage'
    elif def_selection == 'STLp':
        def_stat = 'Steal Percentage'
    else: def_stat = ''

    def_title = def_stat + " Comparison"
    chart_def1 = alt.Chart(filter_player, title=alt.TitleParams(
        text=def_title,
        anchor='start')).mark_point().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max)), axis=alt.Axis(labelExpr="format(datum.value, 'd')")),
        y = alt.Y(def_selection, title=def_stat),
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
    )
    chart_def2 = alt.Chart(filter_player, title=alt.TitleParams(
        text=def_title,
        anchor='start')).mark_line().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max)), axis=alt.Axis(labelExpr="format(datum.value, 'd')")),
        y = alt.Y(def_selection, title=def_stat),
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
    )
    chart_def = chart_def1 + chart_def2 

    return filter_playerA.to_dict('records'), filter_playerB.to_dict('records'), chart_off.to_html(), chart_def.to_html()


# Update
if __name__ == '__main__':
    app.run_server(debug=True)