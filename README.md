# TV Series NLP Analysis

This project analyzes a TV series using a complete NLP pipeline powered by Python, Scrapy, Transformers, and modern LLM-based text analysis. It extracts data, processes dialogues, identifies themes, and builds a character interaction network — all in one workflow.

## Features

### **1. Web Scraping (Scrapy)**
- Automatically collects episodes, dialogues, and metadata.
- Clean, structured dataset for downstream NLP tasks.

### **2. NLP + LLM Pipeline**
- Uses Hugging Face Transformers and custom LLM prompts.
- Extracts:
  - Episode summaries  
  - Major themes  
  - Character personalities  
  - Sentiment  
  - Topic modeling  

### **3. Character Network Graph**
- Builds a visual character interaction network.
- Shows which characters appear most and how they connect.
- Useful for story analysis & visualization.

### **4. Modular Code Structure**
- Easy to extend for any TV show.
- Each step kept separate (scraping, preprocessing, modeling, visualization).

---

##  Tech Stack

- **Python**
- **Scrapy** (for data extraction)
- **Transformers (HuggingFace)**  
- **spaCy / NLTK**  
- **NetworkX** (character graphs)
- **Matplotlib / Plotly**  
- **Jupyter Notebook / VS Code**  

---

##  Project Structure

project/
├── data/ # scraped and cleaned data
├── notebooks/ # analysis notebooks
├── scripts/ # main python scripts
├── models/ # saved models + outputs
├── visuals/ # graphs and plots
└── README.md


---

##  How to Run

Install dependencies:

```bash
pip install -r requirements.txt

scrapy crawl series_spider
