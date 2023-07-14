#!/usr/bin/env python
# coding: utf-8

# In[1]:


#connect sql to pandas and load file
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\receipts.json",lines = True,typ='frame')


# In[2]:


df


# In[8]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df2 = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\brands.json",lines = True,typ='frame')


# In[9]:


df2


# In[5]:


import pandas as pd
from sqlalchemy import create_engine
engine3 = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df3 = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\users.json",lines = True,typ='frame')


# In[6]:


df3

