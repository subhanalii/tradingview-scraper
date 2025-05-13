# tradingview-scraper

# 📊 TradingView Screener Scraper (Crypto, Stocks, ETFs)

This Python script scrapes **market screener data** directly from [TradingView](https://www.tradingview.com/) using its internal APIs — no browser automation required.

It supports:
- ✅ Crypto Screener
- ✅ CEX & DEX token lists
- ✅ US Stock Market Screener
- ✅ ETF Screener

All extracted data (including name, price, 24h change, market cap, and volume) is saved to **CSV files**, grouped by type.

---

## 📽️ Demo

[![Watch the demo](https://img.youtube.com/vi/MKZG7XTtqrU/0.jpg)](https://youtu.be/MKZG7XTtqrU)

> 💬 Want the full working code or a custom scraper?  
> 📧 Email me at [isubhanali3@gmail.com](mailto:isubhanali3@gmail.com)  
> 💼 [Hire me on Upwork](https://www.upwork.com/freelancers/~01b6c1b6819be875f2)
> 💬 Discord: `s.a3`
💬 Discord: [`s.a3`](https://discord.com/users/s.a3)


---

## 🔍 Features

- Uses `requests` to query TradingView’s JSON-based screener API
- Extracts dynamic data for:
  - **Crypto coins**
  - **DEX/CEX tokens**
  - **US stocks**
  - **ETFs**
- Saves results to separate `.csv` files
- Prints symbols to console in real time
- Handles pagination internally

---

## 📦 Dependencies

- Python 3.x
- `requests`
- `json`
- `csv`
- `time`

Install with:

```bash
pip install requests
