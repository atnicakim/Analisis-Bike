import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("cleaned_day.csv")
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Streamlit Dashboard
st.title("Bike Sharing Analysis Dashboard")

# Sidebar untuk filter waktu
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", day_df["dteday"].min())
end_date = st.sidebar.date_input("End Date", day_df["dteday"].max())

filtered_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]

# Distribusi Data
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(day_df["cnt"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Jumlah Peminjaman")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# Rata-rata Peminjaman Berdasarkan Musim
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
season_avg = day_df.groupby("season")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="season", y="cnt", data=season_avg, palette="viridis", ax=ax)
ax.set_xlabel("Musim (1=Semi, 2=Musim Panas, 3=Musim Gugur, 4=Musim Dingin)")
ax.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig)


st.header("Visualization & Explanatory Analysis")

# Pertanyaan 1: Bagaimana tren peminjaman sepeda sepanjang tahun?
st.subheader("Tren Peminjaman Sepeda Sepanjang Tahun")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=filtered_df["dteday"], y=filtered_df["cnt"], ax=ax, color="blue")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Pertanyaan 2: Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda?
st.subheader("Pengaruh Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=filtered_df["weathersit"], y=filtered_df["cnt"], ax=ax, palette="Set2")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)


# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
1. **Tren Peminjaman Sepeda**: Peminjaman sepeda menunjukkan pola musiman, dengan peningkatan pada musim semi dan panas, serta penurunan pada musim dingin.
2. **Pengaruh Cuaca**: Kondisi cuaca buruk (hujan atau kabut) menyebabkan penurunan signifikan dalam jumlah peminjaman sepeda.
3. **Korelasi Data**: Temperatur dan kelembaban memiliki korelasi dengan jumlah peminjaman. Semakin nyaman cuaca, semakin banyak pengguna sepeda.
""")

st.caption('Mikacinta Gustina Amalan Toyibah, 2025')