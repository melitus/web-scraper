
---

````markdown
# 📘 AI Saturdays Lagos - Week 2 Assessment: Web Scraping Project

Welcome to **Week 2** of **AI Saturdays Lagos Cohort 9 - Flipped!** 🎉

This week's challenge is all about applying Python and data skills in a real-world scenario. After learning Python fundamentals and numerical computing with NumPy in Week 1, we're now using that foundation to extract meaningful data from the web — a key step in any data science or machine learning pipeline.

---

## ✅ Assessment Overview

This task required:
- Creating a **GitHub account** (if you don’t have one)
- Creating a **public repository**
- Choosing a **publicly available website** that could serve as data for a future ML project
- Writing a **Python script to scrape data** from that website
- Ensuring the scraping follows **ethical practices**
- Pushing the project to **GitHub**

---

## 🕸️ About the Website Scraped

**[Books to Scrape](http://books.toscrape.com/)** is a website built for practicing web scraping. It contains structured data about books, including:
- Title
- Price
- Availability

This site is ideal for beginners and allows scraping for educational purposes without any ethical or legal concerns.

---

## 📂 Project: Book Scraper 📚

This is a simple Python scraper that navigates multiple pages of the website and extracts:
- Book titles
- Prices
- Stock availability

The extracted data could be further cleaned and used in machine learning tasks like:
- Price prediction
- Sentiment analysis (if descriptions are added)
- Recommendation systems

---

## ⚙️ Features

- Scrapes structured book data across multiple pages
- Uses `requests` and `BeautifulSoup` for efficient parsing
- Can be extended or modified easily
- Follows ethical scraping guidelines

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/melitus/web-scraper.git
cd book-scraper
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Scraper

```bash
python scraper.py
```

The script will print the title, price, and availability of books from the first 3 pages.

---

## 📦 Files Included

* `scraper.py`: Main script that performs the scraping
* `requirements.txt`: Python dependencies
* `README.md`: Project documentation

---

## ✅ Ethical Considerations

* This project scrapes **only publicly available data**
* The site used (`books.toscrape.com`) is built specifically for scraping practice
* No bots or login access was used
* Request rate is controlled to avoid server overload

---

## 🙌 Acknowledgments

Thanks to the **AI Saturdays Lagos** team and community for creating this opportunity to apply learning in a practical way.

Let’s keep building!

