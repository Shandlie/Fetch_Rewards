#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\receipts.json",lines = True,typ='frame')
# df.to_sql("newTable", con=engine, if_exists = 'replace', index=False)


# In[2]:


df


# In[8]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df2 = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\brands.json",lines = True,typ='frame')
# df.to_sql("newTable", con=engine, if_exists = 'replace', index=False)


# In[9]:


df2


# In[5]:


import pandas as pd
from sqlalchemy import create_engine
engine3 = create_engine('mysql+pymysql://root:Shandlie*23@localhost/fetch_rewards')
df3 = pd.read_json("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\users.json",lines = True,typ='frame')
# df.to_sql("newTable", con=engine, if_exists = 'replace', index=False)


# In[6]:


df3


# In[7]:


import mysql.connector


# In[ ]:


try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='fetch',
                                         user='pynative',
                                         password='pynative@#29')


# In[18]:


import pandas as pd
import json

with open("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\receipts.json") as file:
    json_data = json.load(file)
df = pd.json_normalize(json_data)

 

# # Export the DataFrame to CSV
# df.to_csv('table.csv', index=False)


# In[19]:


import json


# In[21]:


import gzip


# In[23]:


# Specify the path to your .gz file
file_path = "C:\\Users\\shayc\\Downloads\\receipts.json.gz"

# Open the .gz file in binary mode
with gzip.open(file_path, 'rb') as file:
    # Read the contents of the .gz file
    extracted_data = file.read()

# Now you can process the extracted data as needed
extracted_data


# In[27]:


# extracted_data = extracted_data.decode('utf-8')


# In[31]:


# first_key = next(iter(extracted_data))
# first_value = extracted_data[first_key]

