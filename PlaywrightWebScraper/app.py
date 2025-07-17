import streamlit as st
from scraper import download_arxiv_pdfs

st.title("📄 ArXiv PDF Downloader")
st.markdown("Enter a search topic (e.g., 'neural networks') to download PDF papers from arXiv.")

search_term = st.text_input("🔍 What do you want to search?", value="neural networks")
start = st.button("🚀 Download PDFs")

if start and search_term.strip():
    with st.spinner("Fetching and downloading..."):
        count = download_arxiv_pdfs(search_term)
    st.success(f"✅ Download complete! {count} PDF(s) saved in the data/ folder.")