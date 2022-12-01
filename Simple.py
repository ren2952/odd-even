#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import numpy as np
def oddoreven(a):
  if a%2==0:
    return 'even'
  else:
    return 'odd'
st.title('Simple')
a = st.number_input(' a number')
st.write(oddoreven(a))



# In[ ]:




