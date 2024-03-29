import pandas as pd
import numpy as np
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
print(num_series.value_counts().index[:1])
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print(num_series)