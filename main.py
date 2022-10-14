#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries

from snowflake.snowpark.session import Session
import streamlit as st
import pandas as pd
from Config import connection_parameters as CP
import plotly.express as px



# In[2]:

connection_parameters = CP
session = Session.builder.configs(connection_parameters).create()

# In[3]:


# Fetching the Data from tables to DF.
snow_df_rfm = session.table('RFM_RESULTS')

# Convert Snowpark DataFrames to Pandas DataFrames for Streamlit
pd_df_rfm = snow_df_rfm.to_pandas()


# In[5]:

st.set_page_config(layout="wide")

header = st.container()




with header:
    st.title("Demo Title")    
    
