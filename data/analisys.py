import plotly
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import json
import pandas as pd


plotly.offline.plot({"data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])], "layout": go.Layout(title="hello world")}, auto_open=True)