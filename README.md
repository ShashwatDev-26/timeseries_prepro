# timeseries-prep

Simple utilities for generating and converting time series data to supervised format.

## Usage

```python
from timeseries_prep import timeseriesplayground

ts = timeseriesplayground()
data = ts.generate_synthetic_time_series()
supervised = ts.series_to_supervised(data, window=3, lag=2)
