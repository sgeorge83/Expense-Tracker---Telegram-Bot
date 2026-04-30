from datetime import datetime

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    telegram_id: str
    text: str


class ExpenseResponse(BaseModel):
    message: str
    amount: float
    category: str
    currency: str = "AED"
    created_at: datetime
