import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import pandas as pd
bar1 = go.Bar(x =['virat','rohit','dhoni','rahul','moni','modi','kartik','bumrah'],
                y =[10,20,30,40,50,60,70,80])
params = [
    'X','Y'
]

trace1 = go.Bar(
    x=['virat', 'rohit', 'rahul','hardik'],
    y=[40, 34, 23,20],
    name='ODI'
)
trace2 = go.Bar(
    x=['virat', 'rohit', 'rahul','hardik'],
    y=[32, 38, 29,25],
    name='test'
)
params1 = [
    'Name','X','Y'
]
subject=['Mathematics','Science','Social Science']
frequency=[100,105,200]
df_subject = pd.DataFrame.from_dict({'subject':subject,'passed':frequency})
graph_subject =go.Bar(x=df_subject['subject'],y=df_subject['passed'],marker={'color':'red'})
graph_lay =go.Layout(title='your sample graph should look like this')

text ="""A bar graph can be defined as a chart or a graphical representation of data, quantities or numbers using bars or strips.
Bar graphs are used to compare and contrast numbers, frequencies or other measures of distinct categories of data."""
 
bar_layout = html.Div(className='nav_div',children=[
				
				html.Nav(className='nav',
                children=[
                    
                    html.Ul(
                        className='main-ul',
                       children= [
                            html.Li(html.A('Graphvidz',href='#')),
                            
                            html.Li(html.A('Visualize',href='#')),
                            html.Li(html.A('learn',href='#')),
                            html.Li(html.A('About Me',href='#'))
                        ]
                    )
                ]
            ),
	
	
			
				html.Section(  className ='basic-graph',
				children=[html.H2(children='Basic Bar Graph'),
						html.P(children=text),
            dcc.Graph(id ='bar_graph1',figure ={'data':[bar1],'layout':{'title':'simple bar graph'}}),
            html.H2('Learn to plot bar graph',style={'color':'red'}),
            html.P('''Bar graph is one of the most easiest graph to plot.But this graph is very important and informative while 
            	representing categorical data.'''),
            html.P('The first step of plotting a bar graph is to get the data.If you already have the data ,then follow it!'),
            html.P('''You have to observe your data and make a frequency table to your data. Frequency table consist 
            	the number of repeatation of each data point. Lets say you have a dataset which represent the number of
            	student passed in Mathematics,Science and Social Science.If 100 student is in Mathematics,105 in Science and 200 in 
            	Social Science.Then your frequence table look like this'''),

            html.Div(className='table-co',children=[
            	dash_table.DataTable(columns=(
			            
			            [{"name":i,"id":i} for i in ['subject','passed']]
			        ),
			        	data=df_subject.to_dict("rows"),
			        editable=True
			    )],style={'padding-left':'10%'}),
            html.P('''After making the frequency table making bar graph is simple.Take the category in x axis and frequency in y axix.
            	Draw box with height of the respective frequency for each category.Keep the width of all box same.'''),
             dcc.Graph(id='ddd',figure={'data':[graph_subject],'layout':graph_lay}),


            dcc.Graph(id='bar_graph2'),
            html.Span('min-X',style={'padding':'5px'}),
            dcc.Input(id='input-1-keypress', type='number',value=10),
            html.P(),
            html.Span('max-X',style ={'padding':'5px'}),
            dcc.Input(id='input-2-keypress', type='number',value=50),
            html.P(),
            html.Span('Number of bar',style ={'padding':'5px'}),
            dcc.Input(id='input-3-keypress', type='number', value=10),
            html.P(),
            html.H1('Represent Your Data in Bar'),
            html.P('Enter your data to create the bar Graph'),
            
    		html.Div([dash_table.DataTable(
			        id='table-editing-simple',
			        columns=(
			            
			            [{'id': p, 'name': p} for p in params]
			        ),
			        data=[
			            dict(**{param: 0 for param in params})
			            for i in range(1, 10)
			        ],
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='table-editing-simple-output'),


			    #second type of bar graph

			    html.Div([
			    		html.H2('Grouped Bar Chart'),
			    		html.P('''A grouped bar chart, also known as clustered bar graph, 
			    			multi-set bar chart, or grouped column chart, is a type of bar 
			    			graph that is used to represent and compare d
			    			ifferent categories of two or more groups.The following chart shows the exact example''',style={'padding-right':'5%','padding-left':'5%'})

			    			,
			    		dcc.Graph(id='bar_graph3',figure={'data':[trace1,trace2],'layout':dict(title='Grouped bar graph')}),
			    		html.H2('Learn and Create Your grouped graph'),
			    		html.P('Enter the data in the table completely plot the data'),

			    		html.Div([dash_table.DataTable(
			        id='table-editing-simple1',
			        columns=(
			            
			            [{'id': p, 'name': p} for p in params1]
			        ),
			        data=[
			            dict(**{param: 0 for param in params1})
			            for i in range(1, 10)
			        ],
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='table-editing-simple-output1'),
			    	],style={'textAlign':'center'}),

			    #bar graph stacked type
			    html.Div([

			    		html.H2('Stacked Bar Chart',style={'color':'red'}),
			    		html.P('''A stacked bar graph (or stacked bar chart) is a chart that uses bars to 
			    			show comparisons between categories of data, 
			    			but with ability to break down and compare parts of a whole. 
			    			Each bar in the chart represents a whole, and segments in the bar represent different 
			    			parts or categories of that whole.Below is a real example of stack bar graph''',
			    			style={'padding-left':'5%','padding-right':'5%'}),
			    		dcc.Graph(id='bar_graph4',figure={'data':[trace1,trace2],'layout':dict(title='Stacked bar graph',
			    			barmode='stack')}),
			    		html.H2('Create your own Stacked Bar Chart',style={'color':'red'}),
			    		html.P('Input data in the table as the given format .Automatically graph will come'),


			    	]),
			    html.Div([dash_table.DataTable(
			        id='table-editing-simple2',
			        columns=(
			            
			            [{'id': p, 'name': p} for p in params1]
			        ),
			        data=[
			            dict(**{param: 0 for param in params1})
			            for i in range(1, 10)
			        ],
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='table-editing-simple-output2'),

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

