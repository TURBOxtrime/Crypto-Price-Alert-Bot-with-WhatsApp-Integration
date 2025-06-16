# Crypto-Price-Alert-Bot-with-WhatsApp-Integration

This Python project tracks real-time cryptocurrency prices and sends WhatsApp alerts when prices meet user-defined buy or sell thresholds. It's designed to help users monitor crypto markets automatically using simple APIs and automation tools.

## 🚀 Features

- 📊 Fetches live crypto prices from CoinMarketCap API
- 📋 Reads buy/sell thresholds from a Google Sheet (via Sheety API)
- 💬 Sends WhatsApp alerts using Twilio when conditions are met
- 🧠 Helps automate decision-making for crypto trading
- 🔑 Uses environment variables to protect sensitive credentials

---

## 🛠 Tech Stack

- **Python 3**
- **Twilio API** for WhatsApp messaging
- **CoinMarketCap API** for live crypto data
- **Sheety API** to access Google Sheets as JSON
- `requests`, `twilio`, `json`

---

## 📸 Screenshots

| CLI Output Example | WhatsApp Alert Example |
|--------------------|------------------------|
| ![CLI Output](screenshots/cli_output.png) | ![WhatsApp Message](screenshots/whatsapp_alert.png) |

---

## ⚙️ How It Works

1. Reads a list of cryptocurrency symbols and thresholds (`lowest`, `highest`) from a Google Sheet via Sheety.
2. Fetches current prices using CoinMarketCap API.
3. Compares each coin's price to its thresholds:
   - If above `lowest` → send **"ready to sell"** alert.
   - If below `highest` → send **"ready to buy"** alert.
4. Sends the alert message via Twilio to a WhatsApp number.

---

## 🧪 How to Use

> ⚠️ This repo uses placeholder values. You must use your own API keys and numbers to run it.
