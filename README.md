DVTO #5
=======

This is a demo for the Data + Visualization Toronto Meetup group for the Kung-Fu Pandas Meetup.

## Setup Instructions
  
### Pre-requisites & Setup

#### Use the DVTO Pandas Image
1. Get [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Download the virtual box image from http://static.crowdriff.com/dvto/5/dvto-ipython.ova (1.3GB image)
2. Import the image into virtualbox (File > Import Appliance...)
3. Start the VM
4. Login with username: `dataviz`, password: `dataviz`
5. Execute the command `dvto`
6. Point your browser to `http://localhost:8888`
7. Create a new IPython Notebook
8. Run the following commands:

```python
from subprocess import call
call(["wget", "https://raw.github.com/VantageAnalytics/datavizTO/master/facebook.csv"])

import pandas as pd
dataframe = pd.read_csv('facebook.csv')
dataframe.shape
```

![Output](https://s3.amazonaws.com/uploads.hipchat.com/26540/160941/uZwPbAbvDNps64L/Screen%20Shot%202014-02-06%20at%203.27.15%20PM.png)

#### OR, Bring your own pandas
If you already have a python environment you can just install [Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html).  Note that Pandas has several dependencies and installing it might require additional libraries.  Particularly on Windows this can be tricky, so if you are a python novice the VirtualBox might be easier.
  
Once you have started python, import pandas and load the csv.  

    >>> import pandas as pd
    >>> dataframe = pd.read_csv('facebook.csv')

The shape property gives the number of rows and columns loaded.  Verify you get something like this:

    >>> dataframe.shape
    (511, 14)

  
