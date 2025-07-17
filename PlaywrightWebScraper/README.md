# Playwright-powered-scraping

📘 README.md — ArXiv PDF Downloader with Streamlit

# 📄 ArXiv PDF Downloader

This project is a Python-powered application that enables users to search for academic papers on [ArXiv](https://arxiv.org/) and automatically download matching PDFs. It combines the scraping power of **Playwright** with an intuitive **Streamlit** frontend to create a seamless experience.

---

## 🚀 Features

- 🔍 Search for any topic (e.g., "neural network", "computer vision", "quantum computing")
- 📦 Downloads all matching PDF papers from ArXiv
- 📊 Streamlit dashboard shows download status and count
- 🧠 Scraping logic built with Playwright for full browser automation
- 📂 Saved PDFs are stored locally in the `data/` folder

---

## 🛠️ Tech Stack

Tool

Purpose

Streamlit

Web interface/dashboard

Playwright

Scraping dynamic search results

BeautifulSoup (optional)

HTML parsing

urllib

File downloads

Python 3.7+

Main programming language

📁 Folder Structure

your_project/
├── app.py           # Streamlit frontend interface
├── scraper.py       # Playwright-based PDF downloader
├── data/            # Folder to store downloaded PDFs

📦 Installation

# Install dependencies
pip install streamlit playwright

# Install browser drivers for Playwright
playwright install

▶️ How to Run

streamlit run app.py

Then open http://localhost:8501 in your browser.

✏️ Usage

Type your search query in the Streamlit input box (e.g. "neural networks")

Click Download PDFs

The app will fetch search results from ArXiv and download related papers

You’ll see a status message showing how many PDFs were saved

⚠️ Notes

ArXiv limits search results per query — typically up to 50 items.

PDF files are saved as: data/<paper_id>.pdf

If you run into Windows-related Playwright errors (e.g. _make_subprocess_transport), make sure to set:

import asyncio, sys
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


