import pandas as pd
import numpy as np

class timeseriesplayground:

  def __init__(self):
    pass

  def generate_synthetic_time_series(self,length=200, amplitude=10, frequency=5, noise_level=2, trend=0.1):
    # time Sequence
    time_series = None
    timed       = None
    timed = pd.date_range(end=pd.to_datetime("today").normalize(),periods=length,freq="B")

    time = np.arange(length)
    sin_wave = amplitude * np.sin(2 * np.pi * frequency * time / length)
    noise = np.random.normal(0, noise_level, length)
    if trend != 0:
      time_series = sin_wave + noise + trend * time
    else:
      time_series = sin_wave + noise

    datats = {"Time":timed,"Series":time_series}
    return pd.DataFrame(datats).set_index('Time')


  def series_to_supervised(self,data, window=1, lag=1, dropnan=True):
    if len(data.columns)>1:
       print("[*] Only univariant time series..")
       return -1
    cols, names = list(), list()
    # Input sequence (t-n, ... t-1)
    for i in range(window, 0, -1):
        cols.append(data.shift(i))
        names += [('%s(t-%d)' % (col, i)) for col in data.columns]
    # Current timestep (t=0)
    cols.append(data)
    names += [('%s(t)' % (col)) for col in data.columns]
    # Target timestep (t=lag)
    cols.append(data.shift(-lag))
    names += [('%s(t+%d)' % (col, lag)) for col in data.columns]
    # Put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # Drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg



