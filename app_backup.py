from mpu9250_jmdev.mpu_9250 import MPU9250
from mpu9250_jmdev.registers import *

from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.io as pio
import plotly

from collections import deque
import numpy as np
from time import *
import random
import dash
import os


####################################################################################################
# Getting data from GY91
####################################################################################################
mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ)
mpu.configure()

def module_data(type):
    accelerometer = mpu.readAccelerometerMaster()
    gyroscope = mpu.readGyroscopeMaster()
    magnetometer = mpu.readMagnetometerMaster()
    temperature = mpu.readTemperatureMaster()

    #Accelerometer sorted values if [0][1][2] are X,Y,Z axis respectively
    xA = round(accelerometer[0], 6)
    yA = round(accelerometer[1], 6)
    zA = round(accelerometer[2], 6)
    outA = [xA, yA, zA]

    #Gyroscope sorted values if [0][1][2] are X,Y,Z axis respectively
    xG = round(gyroscope[0], 2)
    yG = round(gyroscope[1], 2)
    zG = round(gyroscope[2], 2)
    outG = [xG, yG, zG]

    #Magnetometer sorted values if [0][1][2] are X,Y,Z axis respectively
    xM = round(magnetometer[0], 6)
    yM = round(magnetometer[1], 6)
    zM = round(magnetometer[2], 6)
    outM = [xM, yM, zM]

    if type == 'xG':
        return xG
    elif type == 'yG':
        return yG
    elif type == 'zG':
        return zG
    else:
        print('\nF')

<<<<<<< HEAD
####################################################################################################
# Setting up variables for live-update graph
#####################################################################################################
=======

####################################################################################################
# Setting up variables for live-update graph
#####################################################################################################

Xt = deque(maxlen=30)
Xt.append(np.random.randint(-1,1))

>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1
X = deque(maxlen=30)
X.append(module_data(type='GyroX'))
#X.append(np.random.randint(15,20))

Y = deque(maxlen=30)
Y.append(module_data(type='GyroY'))
<<<<<<< HEAD
Y.append(module_data(type='GyroY'))
=======
>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1
#Y.append(np.random.randint(35,40))

Z = deque(maxlen=30)
Z.append(module_data(type='GyroZ'))
<<<<<<< HEAD
Z.append(module_data(type='GyroZ'))
=======
>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1
#Z.append(np.random.randint(50,60))


####################################################################################################
# App set-up
#####################################################################################################

#1000 miliseconds = 1 second
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 850)

app = dash.Dash(
	__name__,
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
<<<<<<< HEAD
app.title = 'SIMESAT 1 - DRAFT DASHBOARD'
=======
app.title = "SIMESAT 1 - DRAFT DASHBOARD"
>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1

colors = {'background':'#111111', 'text':'#7FDBFF'}
colors['text']

server = app.server

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

# Main layout
app.layout = html.Div(
	[
		#header
		html.Div(
			[
				html.Div(
					[
						html.H4('🛰️ SIMESAT 1 - DRAFT DASHBOARD',
						className='app__header__title'
						),
						html.P(
							'This app continually queries csv files and displays live charts of the modules in the OBC at the nano-satellite',
							className='app__header__title--grey',
						),
					],
					className='app__header__desc'
				),
				html.Div(
					[
						html.Img(
							src=app.get_asset_url('SIMES_white.png'),
							className='app__menu__img',
						)
					],
					className='app__header__logo',
				),
			],
			className='app__header',
		),
        html.Div(
            [
        		#GY-91 container
        		html.Div(
        			[
        				#GY91 simulation
        				html.Div(
        					[
        						html.Div(
        							[html.H6("GY-91 - simulation",
        							className='graph__title')]
        						),
        						dcc.Graph(
        							id = 'live-graph',
        							animate = True
        						),
        						dcc.Interval(
        							id = 'graph-update',
        							interval = int(GRAPH_INTERVAL),
        							n_intervals = 0
        						),
        					],
        				),
        			],
                className="two-thirds column wind__speed__container",
    			#className='app__content'
                ),
            ],
        ),
        # Second column container
        html.Div(
            [   # Second graph
                html.Div(
                    [
                        html.Div(
                            [html.H6('2ND GRAPH CONTAINER',
                                    className='graph__title')]
                        ),
                        dcc.Graph(
                            id = 'gps-tracker',
                            animate = True,
                        ),
                        dcc.Interval(
                            id = 'gps-update',
                            interval = int(GRAPH_INTERVAL),
                            n_intervals = 0
                        ),
                    ],
                    className='graph__container first'
                )
            ],
            className='one-third column histogram__direction',
        ),
        # footer
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(children=[
                                            '© 2021 Academia de Ciencias SIMES. Todos los derechos reservados.'
                                            #Creado por ', html.A('Kenobi', href='https://github.com/CxrlosKenobi')
                                            ],
                                            className='app__footer--grey',
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            #className='app__content',
        ), # footer's end
	],
	className='app__container',
)

'''
def get_current_time():
    """ Helper function to get the current time in seconds. """

    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time
'''

<<<<<<< HEAD
max_value = [max(X), max(Y), max(Z)]
maximum = max(max_value)
=======

X = deque(maxlen=20)
X.append(module_data('xG'))
#X.append(np.random.randint(15,20))

Y = deque(maxlen=20)
Y.append(module_data('yG'))
#Y.append(np.random.randint(35,40))
>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1

min_value = [min(X), min(Y), min(Z)]
minimum = min(min_value)

<<<<<<< HEAD
Xt = deque(maxlen=30)
Xt.append(np.random.randint(minimum, maximum))

####################################################################################################
# Live-update graph GY91
#####################################################################################################
=======
>>>>>>> b7a6fdc6e857d9bb6cdf4adc42e106821e1334e1
@app.callback(
	Output('live-graph', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
    Xt.append(Xt[-1]+ 1)

    Xval = module_data(type='xG')
    Yval = module_data(type='yG')
    Zval = module_data(type='zG')
    '''
    X.append(Xval)
    Y.append(Yval)
    Z.append(Zval)
    '''

    X.append(X[1] + X[-1] * Xval)
    Y.append(Y[-1] + Y[-1] * Yval)
    Z.append(Z[-1] + Z[-1] * Zval)

    trace0 = go.Scatter(
    			x=list(Xt),
    			y=list(X),
    			name='X',
    			mode= 'lines+markers',
                line={"color": "#FF0000"}
                )
    trace1 = go.Scatter(
    			x=list(Xt),
    			y=list(Y),
    			name='Y',
    			mode= 'lines+markers',
                line={"color": "#00FF00"}
                )
    trace2 = go.Scatter(
                x=list(Xt),
    			y=list(Z),
    			name='Z',
    			mode= 'lines+markers',
                line={"color": "#FFFF00"}
                )
    data = [trace0, trace1, trace2]
    return {'data': data,
            'layout':go.Layout(
                        xaxis = {
                            'range':[min(Xt), max(Xt)],
                            'title':'X axis',
                            'showline':True,
                        },
                        yaxis = {
                            'range':[min(X),max(Z)],
                            'title':'Y axis',
                            'showgrid':True,
                            "showline": True,
                            "zeroline": False,
                            "gridcolor": app_color["graph_line"]
                        },
                        plot_bgcolor=app_color["graph_bg"],
                        paper_bgcolor=app_color["graph_bg"],
                        font={"color": "#fff"},
                        height=400
					)
			}
@app.callback(
    Output('counter_text', 'children'),
    [ Input('interval-component', 'n_intervals')]
)
def update_layout_gps(n):
    #something

@app.callback(
    Ourput('gps-tracker', 'figure'),
    [ Input('gps-update', 'n_intervals') ]
)
def gps_tracker_update(n):
    #append varibales for update then the graph
    fig = go.Figure(
        go.Scattermapbox(
            mode = 'markers+lines',
            lon = [],
            lat = [],
            marker = {'size': 10}
        )
    )
    fig.update_layout(
        margin = {'l':0, 't': 0, 'b':0, 'r':0},
        mapbox = {
            'center': {'lon':n, 'lat':n},
            'style' : 'stamen-terrain',
            'center': {'lon':n, 'lat':nn},
            'zoom':1
        }
    )
    return {'data':fig,
        'layout':go.Layout()
        }

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
	app.run_server(debug=True)
