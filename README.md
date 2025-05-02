# ✈️ Wizzair Best Trip Planner

**Wizzair Best Trip Planner** is a Python-based tool that automates the search for the best airfare deals on the Wizzair website. Built using `pandas` and `BeautifulSoup`, it scrapes fare data, filters the cheapest options, and exports your best trips to Excel — all based on user-defined preferences.

---

## 📌 Features

- 🔎 Scrapes live fare data from the Wizzair website  
- 💰 Selects the **lowest fares** for specified routes  
- 🧮 Calculates best **return trip intervals** based on user input  
- 🎯 Filters results based on a **target price**  
- 📤 Exports selected fare data to an **Excel file**

---

## ⚙️ How It Works

The program takes the following input parameters:

```python
FROM = 'KUT'       # Departure location (IATA code)
TO = 'AUH'         # Destination location (IATA code)
INTERVAL = 7       # Days between departure and return
USER_PRICE = 123   # Desired maximum fare price

```

## 📦 Requirements
- Python 3.8+
- pandas
- beautifulsoup4
- requests
- openpyxl (for Excel export)
