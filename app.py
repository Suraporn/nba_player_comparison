from dash import dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import altair as alt


# Data - Loading and Pre-processing
raw = pd.read_csv('data/player_stats.csv')
player = raw[['Player', 'Year', 'Pos', 'Tm', 'G',
             'FG%', 'FT%', '3P%', 'ORB%', 'AST%', 
             'BLK%', 'DRB%', 'STL%'
            ]]
player = player.fillna(0)
player = player.rename(columns={'Player':'Name','Tm':'Team','G':'Game',
             'FG%':'FGp', 'FT%':'FTp', '3P%':'3Pp', 'ORB%':'ORBp', 'AST%':'ASTp', 
             'BLK%':'BLKp', 'DRB%':'DRBp', 'STL%':'STLp'
            })
player['Year'] = player['Year'].astype(int)


# Front-end - START
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([

    # Row1 = Title and Logo
    html.Img(src='/img/nba_logo.jpg'),
    # html.Img(src=dash.get_asset_url('img/nba_logo.png')),
    html.H1('NBA Player Statistics Comparison', style={'textAlign': 'center'}),

    # Row2 = Search players
    dbc.Row([
        # Col - Player A
        dbc.Col([
            html.P('Player A'),
            # Dropdown - Player A
            dcc.Dropdown(
                id='dd_player_A', 
                style={'height':'30px', 'align-items':'center', 'justify-content':'center'},
                value = 'LeBron James',
                options = player['Name'].unique(),
                multi = False,
                placeholder = 'Select player A'),
                html.P(""),
            html.P('Player A - Detail'),
            dash_table.DataTable(
                id='datatable_A',
                columns=[{'name': i, 'id': i} for i in player.columns],
                data=player.to_dict('records')
            )

        ], style={'textAlign': 'center'}),

        # Col - Player B
        dbc.Col([
            html.P("Player B"),
            # Dropdown - Player B
            dcc.Dropdown(
                id='dd_player_B', 
                style={'height':'30px', 'align-items':'center', 'justify-content':'center'},
                value = 'Kobe Bryant',
                options = player['Name'].unique(),
                multi = False,
                placeholder = 'Select player B'),
            html.P(""),
            html.P("Player B - Detail"),
            dash_table.DataTable(
                id='datatable_B',
                columns=[{'name': i, 'id': i} for i in player.columns],
                data=player.to_dict('records')
            )
        ], style={'textAlign': 'center'})
    ], style={'textAlign': 'center'}),
    html.P(""),

    # Row3 - Offensive Dropdown
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

    filter_playerA = df.loc[(player['Name']==player_A)].tail(5)
    filter_playerB = df.loc[(player['Name']==player_B)].tail(5)
    filter_player = df.loc[(player['Name']==player_A) | (player['Name']==player_B)]
    x_min=filter_player['Year'].min()
    x_max=filter_player['Year'].max()
    
    off_title = "Offensive Statistic Comparison : " + off_selection
    chart_off = alt.Chart(filter_player, title=off_title).mark_point().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max))),
        y = off_selection,
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
)

    def_title = "Defensive Statistic Comparison : " + def_selection
    chart_def = alt.Chart(filter_player, title=def_title).mark_point().encode(
        x = alt.X('Year',scale=alt.Scale(domain=(x_min, x_max))),
        y = def_selection,
        color = alt.Color('Name', title='Player')
    ).properties(
    width=700,
    height=200
    )

    return filter_playerA.to_dict('records'), filter_playerB.to_dict('records'), chart_off.to_html(), chart_def.to_html()


# Update
if __name__ == '__main__':
    app.run_server(debug=True)