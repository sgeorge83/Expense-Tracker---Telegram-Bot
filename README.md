# Expense Tracker Telegram Bot

AI-powered, voice-first expense tracking assistant on Telegram.

## Vision
Tracking money should feel like chatting.

## Features
- Text expense logging
- Voice note expense logging
- Receipt OCR ingestion
- AI categorization and insights
- Budget alerts and summaries
- Export to CSV/Excel/PDF

## Quick Start
1. Copy `.env.example` to `.env` and fill values.
2. Create virtual environment and install deps.
3. Run API and bot.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn api.main:app --reload
python bot/main.py
```

## Repository Layout
- `bot/`: Telegram handlers and command routing
- `api/`: FastAPI backend
- `ai/`: Whisper/NLP/OCR adapters
- `database/`: models, session, migrations scaffolding
- `services/`: domain logic
- `reports/`: summaries and insights generators
- `exports/`: export builders
- `tests/`: unit tests
- `docs/`: product and technical blueprints
