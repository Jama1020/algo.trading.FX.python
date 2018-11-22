# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:46:33 2018

@author: Jorge_Moreno
"""
import pandas as pd
import numpy as np
import plotly
from plotly import tools
import plotly.graph_objs as go
import funciones_jama

df=pd.read_csv('EURUSD.CSV')
df.head()
df.columns =['date','open','high','low','close','volume']
df.date=pd.to_datetime(df.date,format='%d.%m.%Y %H:%M:%S.%f')
df=df.set_index(df.date)
df=df[['open','high','low','close','volume']]
df=df.drop_duplicates(keep=False)
df.head()
ma = df.close.rolling(center=False, window=30).mean()
HAresults = funciones_jama.heikenashi(df,[1])
HA = HAresults.candles[1]
trace0=go.Ohlc(x=df.index,open=df.open, high=df.high, low=df.low, close=df.close, name='Cotizacion EURUSD')
trace1=go.Scatter(x=df.index, y=ma)
trace2=go.Ohlc(x=HA.index,open=HA.open, high=HA.high, low=HA.low, close=HA.close, name='heikenashi')
data=[trace0, trace1, trace2]
fig=tools.make_subplots(rows=2, cols=1,shared_xaxes=True)
fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,1)
fig.append_trace(trace2,2,1)
plotly.offline.plot(fig,filename='Grafica Heikenashi')


ValueError:
  invalid value type 'pandas.core.frame.DataFrame' received for the 'close' property of ohlc
      the 'close' property is an array that may be specified as a tuple, list numpy array or pandas series
    
 **************Alguien sabe como solucionar este error*************   
