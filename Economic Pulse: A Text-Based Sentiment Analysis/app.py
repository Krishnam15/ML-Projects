import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load your CSV
articles_df = pd.read_excel(r"C:\Users\KIIT\Desktop\Mini_Project\articles.xlsx")

# Title
st.title("📰 News Article Sentiment Dashboard")

# Sidebar filter
sentiment = st.sidebar.selectbox("Select Sentiment", ["All"] + list(articles_df['Sentiment'].unique()))

# Filter DataFrame
if sentiment != "All":
    filtered_df = articles_df[articles_df['Sentiment'] == sentiment]
else:
    filtered_df = articles_df

# Show basic stats
st.subheader("Sentiment Distribution")
st.bar_chart(articles_df['Sentiment'].value_counts())

# Word Cloud
st.subheader("Word Cloud of News Content")
text = " ".join(filtered_df['Cleaned Content'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
st.image(wordcloud.to_array())

# Article Search
st.subheader("Search Articles")
search_term = st.text_input("Enter keyword to search in titles")
if search_term:
    results = articles_df[articles_df['Title'].str.contains(search_term, case=False)]
    st.write(f"Found {len(results)} articles")
    for i, row in results.iterrows():
        st.markdown(f"**{row['Title']}**")
        st.write(row['Content'])
        st.markdown("---")


