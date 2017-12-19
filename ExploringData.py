import pandas as pd   # We give the libraries short names for easier referencing
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline  
# This allows us to display plots right within our Jupyter notebook

## DISPLAY DATA TABLE FROM CSV FILE
data = pd.read_csv('../datasets/kaggle/tmdb_data.csv')
data.head(10)  # Try changing the number of rows and removing the argument to check what pandas uses as the default value

# grouping the data
genres = np.random.choice(['scary', 'funny', 'action packed'], 20)
revenue = 100.*np.random.normal(size = 20)**2
viewers = np.random.randint(100, size = 20)
fake_movies = pd.DataFrame(
    {'genres':genres, 'revenue': revenue, 'viewers': viewers})
fake_movies.head()
grouped = fake_movies.groupby(genres)
grouped.get_group('funny')

data.groupby('title_year').count()
data.loc[data.gross>1e9,['original_title', 'gross']].sort_values('gross', ascending=False)
# filtering data
data.loc[(data.title_year<2017)&(data.title_year>=2007), :].groupby('title_year')[['id']].count()

# function to go through csv files to gather the actual numbers for statistics
pd.read_csv

# creating a df within python
# Take a look at the df we've created:

daily_aggregate = track_daily[np.isfinite(track_daily['Date'])].groupby('Date').aggregate({'US':np.sum, 'CO':np.sum})
daily_aggregate.head()

# We'll probably want to do a fillna(0) here, since a lot of the artists in the data set might not have been 
# streamed in the US or Colombia:
artist_daily = track_daily.groupby('Name').aggregate({'US':np.sum,'CO':np.sum}).dropna(how='all').fillna(0.)

artist_daily[artist_daily['CO']>artist_daily['US']]

## notebook 3, 4 distributions and stats
# margin of error, T-stats / T-distributions
# consider linear regression and lines of best fit, but it might not be applicable

# plotting data
#DataFrame.plot.pie(y=None, **kwds)
#y = columns/ positions to plot
#kwds is optional, given to pandas.DataFrame.plot()
