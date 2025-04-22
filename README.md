# Telegram Trading Signal Bot

Bot ini mengirimkan sinyal trading ke Telegram menggunakan API.

## Setup
1. Isi variabel environment:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
2. Deploy ke Railway atau platform lainnya.

## Kirim Sinyal
POST ke endpoint `/send` dengan JSON seperti:
```json
{ "message": "Buy BTC now!" }
```