import streamlit as st
import pandas as pd
from numerize import numerize

# tittle tabel data store
st.title("Tabel Data Store")

# Deklarasi dataset
df = pd.read_csv("store.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df["Ship Date"])
# End of Data Prep

# Menampilan dataframe
st.dataframe(df)

# Title Charting
st.title("Charting")

# Sidebar
with st.sidebar:
    st.title("Dashboard store")
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))

# Metric 1, 2, 3
met1, met2, met3 = st.columns(3)
with met1:
    st.metric(
        "Total Sales", 
        "$ " + numerize.numerize(df['Sales'].sum()),
        "5%"
        )
with met2:
    st.metric("Total Order", df['Order ID'].nunique())
with met3:
    st.metric("Number of Customers", df['Customer ID'].nunique())

# Line chart (Sales)
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()

st.line_chart(sales)
    