# -*- coding: utf-8 -*-
"""LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RIDzjfZ14pfUmoWHlK46_Bk-OWUAsAMC
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('Google_Stock_Price_Train.csv')
df.head(5)

x = df[['Open']]

plt.plot(ser1,x)

ser1 = pd.to_datetime(df['Date'])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled=scaler.fit_transform(x)

x_train,y_train = [],[]
for i in range(60,x_scaled.shape[0]):
  y_train.append(x_scaled[i])
  x_train.append(x_scaled[i-60:i,:])

import numpy as np

x_train,y_train = np.array(x_train),np.array(y_train)

x_train.shape

A = np.hstack([x_train[:,-1,:],y_train.reshape(-1,1)])

A.shape

A[:10]

x_scaled.shape

from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

model = Sequential()
model.add(LSTM(units=50, input_shape = (60,1), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50,return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train,y_train,epochs=100,batch_size=32)

x.head(5)

df_test = pd.read_csv('Google_Stock_Price_Test.csv')

x1 = df_test[['Open']]

x0 = x.iloc[-60:].values

x0.shape

X0[-20:]

x1 = x1.values

x1.shape

x_test = np.vstack([x0,x1])
x_test.shape

x_test = scaler.transform(x_test)

x_test.shape

x_test1 = []
for i in range(60,80):
    x_test1.append(x_test[i-60:i,:])

x_test1 = np.array(x_test1)
x_test1.shape

y_predict = model.predict(x_test1)

plt.plot(y_predict, c='red')
plt.plot(scaler.transform(df_test[['Open']]),c='blue')

