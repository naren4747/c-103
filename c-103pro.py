import pandas as pd
import plotly.express as px

df=pd.read_csv(r"c-103pro.csv")
fig=px.scatter(df,x="Date",y="Cases",color="Country",size_max=60)
fig.show()