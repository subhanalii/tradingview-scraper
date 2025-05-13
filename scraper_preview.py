import requests
import json
import csv

# 🔍 Preview of TradingView Screener Configuration
screeners = {
    "crypto": {
        "url": "https://scanner.tradingview.com/coin/scan",
        "columns": ["base_currency", "close", "24h_close_change|5", "market_cap_calc"]
    }
}

# 🛠️ Preview of Core Logic
def fetch_screener_to_csv(name, config):
    payload = {
        "columns": config["columns"],
        "range": [0, 100],
        "sort": {
            "sortBy": config["columns"][0],
            "sortOrder": "asc"
        }
    }

    response = requests.post(
        config["url"],
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    data = response.json().get("data", [])
    with open(f"{name}_preview.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["symbol"] + config["columns"])
        for row in data:
            writer.writerow([row['s']] + row['d'])

# ▶️ Run Preview
fetch_screener_to_csv("crypto", screeners["crypto"])

# 📌 This is a simplified preview. Contact for the full version with CEX/DEX/Stock/ETF support.
