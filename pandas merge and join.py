import pandas as pd
import numpy as np

Employee = [{"Name":["Anthony","David","Bob","Nagesh","Shafi"],
             "Department":["Finance","Health","Hr","Non-tech","Data-science"],
             "Emp_id":[1,2,3,4,5]}]

df = pd.DataFrame(Employee)

df.head()
# The difference between the merge and join is
#1. The merge is used to join based on column names also the indexing
#2. The join is used to join based on indexing
#We often use the merge most of the times
pd.merge(df,df1)