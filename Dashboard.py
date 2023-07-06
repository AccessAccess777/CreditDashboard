# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:48:46 2023

@author: msadrzad
"""

import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

# Load the CSV file
df = pd.read_csv(r'C:\Users\msadrzad\Desktop\data.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(
    style={'backgroundColor': '#003366', 'padding': '2rem', 'fontFamily': 'Arial'},
    children=[
        html.H1('Credit Fraud Dashboard', style={'color': 'white', 'fontSize': '3rem', 'textAlign': 'center'}),
        html.Div(
            style={'marginBottom': '0.5cm'},
            children=[
                dcc.Tabs(
                    id='tabs',
                    style={'color': 'white', 'marginTop': '1rem'},
                    children=[
                        dcc.Tab(
                            label='Top 10 Risky Loan Portfolios',
                            selected_style={'backgroundColor': 'darkblue', 'color': 'white','height': '50px'},
                            style={'backgroundColor': '#000033', 'color': 'darkblue', 'marginRight': '0.5cm', 'marginBottom': '0.5cm'},
                            #selected_style={'backgroundColor': 'darkblue', 'color': 'white', 'height': '50px'},
                            #style={'backgroundColor': 'darkblue', 'color': 'white', 'width': '100px', 'height': '30px', 'marginLeft': '0.5cm', 'marginBottom': '0.5cm'},
                            
                            
                            children=[
                                html.Div(
                                    style={'display': 'flex', 'gap': '0.5cm'},
                                    children=[
                                        html.Div(
                                            style={'width': '40%'},
                                            children=[
                                                html.Label('Please select Portfolio size:', style={'color': 'white', 'marginRight': '0.5rem', 'fontSize': '1rem'}),
                                                dcc.Dropdown(
                                                    id='portfolio-size-dropdown',
                                                    options=[
                                                        {"label": "Small", "value": 'Small'},
                                                        {"label": "Medium", "value": 'Medium'},
                                                        {"label": "Large", "value": 'Large'}
                                                    ],
                                                    #value='Small',
                                                    multi=True,
                                                    style={
                                                        'fontSize': '1rem',
                                                        'backgroundColor': 'transparent',
                                                        'color': 'darkblue',
                                                        'hover': {'backgroundColor': 'darkblue'}
                                                    },
                                                    className='custom-dropdown'
                                                ),
                                                html.Label('Please select Branch:', style={'color': 'white', 'marginRight': '0.5rem', 'fontSize': '1rem'}),
                                                dcc.Dropdown(
                                                    id='branch-dropdown',
                                                    options=[
                                                        {'label': 'Baku', 'value': 'Baku'},
                                                        {'label': 'Berlin', 'value': 'Berlin'},
                                                        {'label': 'Lusaka', 'value': 'Lusaka'},
                                                        {'label': 'Salyan', 'value': 'Salyan'},
                                                        {'label': 'Quba', 'value': 'Quba'}
                                                    ],
                                                    ##value='Salyan',
                                                    multi=True,
                                                    ##selected_style={'backgroundColor': 'darkblue', 'color': 'white'},
                                                    style={
                                                        'fontSize': '1rem',
                                                        'backgroundColor': 'transparent',
                                                        'color': 'darkblue',
                                                        'hover': {'backgroundColor': 'darkblue'}
                                                    },
                                                    className='custom-dropdown'
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            style={'width': '60%'},
                                            children=[
                                                dcc.Graph(id='bar-chart', style={'width': '100%', 'height': '400px'})
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    style={'marginTop': '1cm', 'color': 'white', 'fontSize': '1rem'},
                                    children=[
                                        html.H2('Instructions', style={'color': 'white', 'fontSize': '2rem'}),
                                        html.Hr(style={'borderTop': '1px solid white'}),
                                        html.P(
                                            'Risk points are calculated based on the following indicators:',
                                            style={'color': 'white'}
                                        ),
                                        html.Ul(
                                            children=[
                                                html.Li('First installment Ratio', style={'color': 'white'}),
                                                html.Li('Overdue History Ratio', style={'color': 'white'}),
                                                html.Li(
                                                    'Concentration on Mobile transactions [for the details and more information, please use the Mobile dashboard.]',
                                                    style={'color': 'white'}
                                                ),
                                                html.Li('PaR', style={'color': 'white'})
                                            ]
                                        ),
                                        html.P(
                                            'Please use Disb.Loans Filter for specific Portfolio sizes. Loan officers with less than 50 loans are not considered. Moreover, the indicators are calculated based on the loans disbursed within the last 18 months, assuming that we know all old Frauds.',
                                            style={'color': 'white', 'fontSize': '1rem'}
                                        ),
                                        html.P(
                                            'Each indicator has equal weight, implying that they are all equal to 1 by default.',
                                            style={'color': 'white', 'fontSize': '1rem'}
                                        ),
                                        html.P(
                                            'Please click on 0 on the PaR40 Filter in order to drop Portfolios with a PaR ratio above 40%. We assume they are all Recovery Officers.',
                                            style={'color': 'white', 'fontSize': '1rem'}
                                        )
                                    ]
                                )
                            ]
                        ),
                        dcc.Tab(
                            label='Portfolio Data',
                            selected_style={'backgroundColor': 'darkblue', 'color': 'white', 'height': '50px','marginBottom': '0.5cm'},
                            style={'backgroundColor': 'darkblue', 'color': 'white', 'marginLeft': '0.5cm', 'marginBottom': '0.5cm'},
                            #selected_style={'backgroundColor': 'darkblue', 'color': 'white','height': '50px'},
                            #style={'backgroundColor': '#000033', 'color': 'darkblue', 'marginRight': '0.5cm', 'marginBottom': '0.5cm'},
                            children=[
                                dash_table.DataTable(
                                    id='portfolio-data-table',
                                    columns=[{"name": col, "id": col} for col in df.columns],
                                    data=df.to_dict('records'),
                                    style_cell={'textAlign': 'left', 'font-family': 'Arial', 'padding': '5px',
                                                'backgroundColor': 'darkblue', 'color': 'white'},
                                    style_header={'backgroundColor': 'darkblue', 'fontWeight': 'bold'},
                                    page_action='native',
                                    page_size=20,
                                    filter_action='native' 
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


# Define the callback function
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('portfolio-size-dropdown', 'value'),
     Input('branch-dropdown', 'value')]
)
def update_bar_chart(portfolio_size, branch):
    if not portfolio_size and not branch:
        # Return an empty figure if both dropdowns are None or empty
        return px.bar()

    if not portfolio_size:
        # Set default value for portfolio_size if it is None or empty
        portfolio_size = ['Large', 'Medium', 'Small']

    if not branch:
        # Set default value for branch if it is None or empty
        branch = ['Baku', 'Berlin', 'Lusaka', 'Salyan', 'Quba']

    filtered_df = df[df['Portfolio size'].isin(portfolio_size) & df['Branch'].isin(branch)]
    top_10_risky_loan_officers = filtered_df.sort_values('Risk rank', ascending=False).head(10)

    fig = px.bar(
        top_10_risky_loan_officers,
        x='Risk rank',
        y='Loan officer',
        orientation='h',
        color='Risk rank',
        color_continuous_scale='blues'
    )

    fig.update_layout(
        title='Top 10 Risky Loan Officers',
        xaxis_title='Risk Rank',
        yaxis_title='Loan Officer',
        plot_bgcolor='white',
        margin={'t': 30, 'b': 50, 'l': 10, 'r': 10}
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, port=8005)
    
    ####app.run_server(debug=False, port=8078)
