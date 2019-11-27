import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import numpy as np 
N=100
x = np.random.randn(N)
y = np.random.random(N)
params = [
    'X','Y']


scatter1 =go.Scatter(x=x,y=y,mode ='markers',marker={'color':'#000080','size':15,'opacity':0.4})
layout1 =go.Layout(title='A sample scatter plot',xaxis=dict(title='X'),yaxis=dict(title='Y'))


N = 500

trace0 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Above',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'blue',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'Below',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'red',
        line = dict(
            width = 2,
        )
    )
)
data = [trace0, trace1]
layout = dict(title = 'Scatter Plot1',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

trace3 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color = np.random.randn(500), #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)

scatter_layout =html.Div(className='nav_bar',children=[
	html.Nav(className='nav',
                children=[
                    
                    html.Ul(
                        className='main-ul',
                       children= [
                            html.Li(html.A('Graphvidz',href='#')),
                            
                            html.Li(html.A('Visualize',href='#')),
                            html.Li(html.A('learn',href='/learn')),
                            html.Li(html.A('About Me',href='#'))
                        ]
                    )
                ]
            ),
	
		html.Section(className='basic-graph',children=[

		html.H1('Scatter Plot',style={'color':'red'}),
		html.P('''ScatterPlot is One of The most Powerful data visualiazation tool.It display alot of information.And of course 
			the hidden one!!!'''),
		html.P('''Scatter Plot is a two dimensional Data Visualization which uses dots to represent the data point
			 the two variables are plotted on x and y axis respectively.'''),
		html.P('''The two variables are related by a single point(i.e a dot).And relation means you can find one using others.And Yes 
			 they are always not related(just like someone u don't like).'''),

		html.H2('A live Example'),
		dcc.Graph(id='scatter2',figure={'data':[scatter1],'layout':layout1}),
		html.P('''We have taken 100 random values as X and 100 random values as Y and have plotted the points with each pair of X and Y.
			Basically its a Cool Graph.is not??'''),

		html.H2('Here are some of  the most beautiful Scatter Plot',style={'color':'red'}),
		dcc.Graph(id='scatter3',figure={'data':data,'layout':layout}),
		html.P('The above Scatter Plot shows two category of points .Anyway The its looking awesome'),

		dcc.Graph(id='scatter4',figure={'data':[trace3],'layout':{'title':'scatter plot'}}),
		html.P('''Oh yes Scatter plot are the coolest graph and one of the most informative graph.But Is it easy to learn and Plot?
			I think Yes it is.Follow the tutorial below'''),
		html.H2('How to Plot Scatter Plot',style={'color':'red'}),
		
			html.P('To plot scatter plot yout should have data set.of course! your dataset'),
			html.P('Your Dataset should be numerical'),
			html.P('Calculate the range of your dataset(both x and y) and according to that draw your x and y axis'),
			html.P('Take each point and find the respective x and y coordinate and just plot it.Yes its a Simple Thing'),
			
			html.H3('A Live Workbook to learn',style={'color':'red'}),
			html.P('Enter your data in x and y column in the table.Your Graph will be automatically plotted'),
			html.Div([dash_table.DataTable(
			        id='scatter-plot',
			        columns=(
			            
			            [{'id': p, 'name': p} for p in params]
			        ),
			        data=[
			            dict(**{param: 0 for param in params})
			            for i in range(1, 15)
			        ],
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='scatterplot1'),
			html.P('You can plot the scatter Plot and join the line,Its a cool idea to add line for scatter plot with less point',
				style={'color':'lightgreen'}),

			
			html.Div([dash_table.DataTable(
			        id='scatter-plot2',
			        columns=(
			            
			            [{'id': p, 'name': p} for p in params]
			        ),
			        data=[
			            dict(**{param: 0 for param in params})
			            for i in range(1, 15)
			        ],
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='scatterplot2'),

			   html.Div([html.P('Plot Scatterplt with large number of data points.'),
			   html.P('Enter data below to plot your graph'),
			   dcc.Input(id='scatter3-point',type='number',value=100),
			   html.P('size of Point:-'),
			   dcc.Input(id='size_of_point',type='number',value=12),
			   html.P('Enter Color of the Point'),
			   dcc.Input(id='color',type='text',value='red'),
			   dcc.Graph(id='scatterplot3')]),
			  ]),
			html.Section(
            className='footer',
            children=[
                html.P('kartik naik'),
                html.P('email-krtknaik595@gmail.com'),
                html.P('ph: +91-8018665502')
            ]
        )














	])