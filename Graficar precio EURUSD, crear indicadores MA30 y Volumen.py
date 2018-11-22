import pandas as pd
import numpy as np
import plotly
from plotly import tools
import plotly.graph_objs as go

df=pd.read_csv('EURUSD.CSV')
df.head()
df.columns =['date','open','high','low','close','volume']
df.head()
df.date=pd.to_datetime(df.date,format='%d.%m.%Y %H:%M:%S.%f')
df.head()
df=df.set_index(df.date)
df=df[['open','high','low','close','volume']]
df.head()
df=df.drop_duplicates(keep=False)
df.head()
ma = df.close.rolling(center=False, window=30).mean()
trace0=go.Ohlc(x=df.index,open=df.open, high=df.high, low=df.low, close=df.close, name='Cotizacion EURUSD')
trace1=go.Scatter(x=df.index, y=ma)
trace2=go.Bar(x =df.index, y=df.volume)
data=[trace0, trace1, trace2]
fig=tools.make_subplots(rows=2, cols=1,shared_xaxes=True)
fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,1)
fig.append_trace(trace2,2,1)
plotly.offline.plot(fig,filename='EURUSD.MA30.VOLUME')