# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
from subprocess import call

# <codecell>

call(["wget", "https://raw.github.com/VantageAnalytics/datavizTO/master/facebook.csv"])
dataframe = pd.read_csv('facebook.csv', index_col=0)
dataframe.shape

# <codecell>

dataframe

# <codecell>

dataframe.describe()

# <codecell>

dataframe.head()

# <codecell>

dataframe['gender_label'] = dataframe['gender'].astype(str)

# <codecell>

dataframe['gender_label'] = dataframe['gender_label'].replace({'1':'Male','2':'Female'})

# <codecell>

dataframe['is_toronto'] = dataframe['location'] == 'Toronto, Ontario'

# <codecell>

dataframe['is_toronto']

# <codecell>

dataframe.head()

# <codecell>

len(dataframe)

# <codecell>

toronto_df = dataframe[dataframe['is_toronto']]

# <codecell>

len(toronto_df)

# <codecell>

grouped = dataframe.groupby('is_toronto')

# <codecell>

len(grouped.groups)

# <codecell>

grouped['fb_groups'].mean()

# <headingcell level=1>

#     Now It's Your Turn

# <headingcell level=3>

# What is the average number of single male friends? How does it change for men and women?

# <codecell>

dataframe['fb_single_male_friends'].mean()

# <codecell>

dataframe.groupby('gender_label')['fb_single_male_friends'].mean()

# <headingcell level=3>

# Is the average different between people in Toronto and elsewhere?

# <codecell>

dataframe.groupby(['gender_label', 'is_toronto'])['fb_single_male_friends'].mean()

# <headingcell level=3>

# Calculate the percentage of single friends that are female for all records

# <codecell>

dataframe['percent_female'] = dataframe['fb_single_female_friends'] / (dataframe['fb_single_male_friends'] + dataframe['fb_single_female_friends'])

# <codecell>

dataframe.head()

# <codecell>

dataframe['percent_female'] = dataframe['fb_single_female_friends'].astype(float) * / (dataframe['fb_single_male_friends'] + dataframe['fb_single_female_friends'])

# <codecell>

dataframe['percent_female'].max()

# <headingcell level=3>

# Do people in toronto have a higher proportion of female single friends? What about men vs women?

# <headingcell level=4>

# (If you want to connect with single women, who should you ask?)

# <codecell>

dataframe['percent_female'].max()

# <codecell>

dataframe['percent_female'].mean()

# <codecell>

dataframe['percent_female'] = dataframe['percent_female'].replace([np.inf, -np.inf], np.nan)

# <codecell>

dataframe['percent_female'].mean()

# <codecell>

to_grouped = dataframe.groupby('is_toronto')

# <codecell>

to_grouped['percent_female'].mean()

# <codecell>

mf_grouped = dataframe.groupby('gender_label')

# <codecell>

mf_grouped['percent_female'].mean()

# <codecell>

all_grouped = dataframe.groupby(['is_toronto','gender_label'])

# <codecell>

all_grouped['percent_female'].mean()

# <headingcell level=3>

# Which user has the most single friends?

# <codecell>

dataframe['single_friends'] = dataframe['fb_single_female_friends'] + dataframe['fb_single_male_friends']

# <codecell>

sorted_df = dataframe.sort('single_friends')

# <codecell>

sorted_df.tail()

# <codecell>


