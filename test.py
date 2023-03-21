import yfinance as yf
import pandas as pd
import streamlit as st
aapl= yf.Ticker("GOOG")
print(aapl.fast_info)

aapl_historical = aapl.history(period='max',start='2019-5-31',end='2023-3-16',interval='5d')
aapl_historical=aapl_historical.reset_index()

print(aapl_historical)

st.line_chart(aapl_historical,y = 'Volume',x='Date')