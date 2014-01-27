datavizTO
===========

This is a demo for the Data + Visualization Toronto Meetup group for the Kung-Fu Pandas Meetup.

## Setup Instructions
  
### Pre-requisites & Setup
1. Get [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Download the virtual box image from 
2. Import the image into virtualbox (File > Import Appliance...)
3. Start the VM
4. Login with username: dataviz, password: dataviz

OR if you already have a python environment you can just install [Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html).  Note that Pandas has several dependencies and installing it might require additional libraries.  Particularly on Windows this can be tricky, so if you are a python novice the VirtualBox might be easier.
  
The facebook.csv file is inlcuded in the VirtualBox image, but if you are using your own python install you can get it from this repository.

### Verification
Once you have the VirtualBox running or Pandas installed, ensure you can start python, import pandas and load the csv:

If you are using the VM, activate the virtualenv and start python in the dataviz home directory:

    source dataviz/bin/activate
    python

Once you have started python, import pandas and load the csv.  

    >>> import pandas as pd
    >>> dataframe = pd.read_csv('facebook.csv')

The shape property gives the number of rows and columns loaded.  Verify you get something like this:

    >>> dataframe.shape
    (511, 14)

  
