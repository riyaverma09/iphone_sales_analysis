# i phone sales analysis

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data=pd.read_csv(r'C:/python/apple_products.csv')
print(data.isnull().sum())
print(data.describe())
highest_rated=data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])
iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated,x=labels,y=counts,title="Number of ratings of highest rated i phones")
figure.show()

iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated,x=labels,y=counts,title="Number of Reviews of highest rated i phones")
figure.show()

figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",title="Relationshop between sales Price and number of rating")
figure.show()
figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",title="Relationship between discount percentage and number of rating")
figure.show()