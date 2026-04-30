from datetime import datetime

from fastapi import FastAPI, HTTPException

from api.schemas import ExpenseCreate, ExpenseResponse
from database.init_db import init_db
from services.parser import parse_text_expense

app = FastAPI(title="Expense Tracker API", version="0.1.0")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/expenses/text", response_model=ExpenseResponse)
def add_text_expense(payload: ExpenseCreate) -> ExpenseResponse:
    parsed = parse_text_expense(payload.text)
    if not parsed:
        raise HTTPException(status_code=400, detail="Could not parse expense")
    return ExpenseResponse(
        message="Expense parsed successfully",
        amount=parsed.amount,
        category=parsed.category,
        currency=parsed.currency,
        created_at=datetime.utcnow(),
    )
