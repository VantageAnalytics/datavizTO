# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd

# <headingcell level=4>

# Let's make a small DataFrame 

# <codecell>

df = pd.DataFrame([[34.3,1,"Toronto"],
                   [35.6,1,"New York"],
                   [43.3,2,"Toronto"]])
df

# <headingcell level=4>

# Index and Column Values could be better...

# <codecell>

df = pd.DataFrame([[34.3,1,"Toronto"],
                   [35.6,1,"New York"],
                   [43.3,2,"Toronto"]], 
                  index=[1,2,3], 
                  columns=["Age","Gender","City"])
df

# <headingcell level=4>

# Index values don't have to be numbers.

# <codecell>

df = pd.DataFrame([[34.3,1,"Toronto"],
                   [35.6,1,"New York"],
                   [43.3,2,"Toronto"]], 
                  index=["Bob","Steve","Jane"], 
                  columns=["Age","Gender","City"])
df

# <headingcell level=4>

# Let's look at some basic operations for getting at pieces of the DataFrame

# <codecell>

df[0]

# <codecell>

df[0:3]

# <codecell>

df['Age']

# <codecell>

df.Age

# <codecell>

df.describe()

# <codecell>

df[['Age','City']]

# <codecell>

df.iloc[1,0]

# <codecell>

df.iloc[1,0] = 38
df

# <codecell>

df['age2'] = df.Age + df.Gender
df

# <codecell>

df.iloc[1:3,0:2]

# <codecell>

df.ix['Steve','Age']

# <codecell>

df.loc['Steve', 'Age']

# <headingcell level=4>

# Want more?  See http://pandas.pydata.org/pandas-docs/stable/indexing.html

