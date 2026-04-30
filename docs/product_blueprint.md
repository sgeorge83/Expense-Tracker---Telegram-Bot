# Expense Tracker Telegram Bot — Complete Product Blueprint

## Product Vision
Build an AI-powered voice-first expense tracking assistant on Telegram where tracking money feels like chatting.

## Core Capabilities
- Text expense logging
- Voice expense logging with transcription and parsing
- Receipt OCR ingestion
- AI insights and spending predictions
- Budget setup and threshold alerts
- Reporting, exports, and dashboards
- Shared wallets and group expense modes

## System Architecture
Telegram -> Bot API Layer -> Backend API -> AI Layer -> Database.

## MVP Roadmap
1. **Phase 1 (2–3 weeks):** Telegram bot, text + voice, categories, monthly summary.
2. **Phase 2:** Budgets, OCR, AI categorization, charts.
3. **Phase 3:** Subscription + premium insights + exports.
4. **Phase 4:** Mini app, shared wallets, SME package.

## Recommended Stack
- Bot: `python-telegram-bot`
- API: `FastAPI`
- DB: SQLite (MVP), PostgreSQL (prod)
- AI speech: Whisper
- NLP: OpenAI API
- OCR: Tesseract or Google Vision
- Hosting: Railway/Render/AWS
