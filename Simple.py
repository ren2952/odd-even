#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import numpy as np
def oddoreven(a, b):
  if a%b==0:
    return 'even'
  else:
    return 'odd'
st.title('Simple')
a = st.number_input(' a number')
b = st.number_input('Enter another number')
st.write(div(a, b))



# In[ ]:




