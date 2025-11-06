from fastapi import FastAPI
from app.models import QuoteRequest
from app.logic import build_quote
from app import mock_llm
import os

app = FastAPI(title="Quotation Microservice")

MOCK_LLM = os.getenv("MOCK_LLM", "true").lower() in ("1", "true", "yes")

@app.post("/quote")
def create_quote(req: QuoteRequest):
    result = build_quote(req.items)
    grand = result["grand_total"]

    if MOCK_LLM:
        en = mock_llm.generate_email_draft_en(req.client.name, grand, req.currency, req.delivery_terms, req.notes)
        ar = mock_llm.generate_email_draft_ar(req.client.name, grand, req.currency, req.delivery_terms, req.notes)
    else:
        en = "Real LLM not configured."
        ar = "Real LLM not configured."

    return {
        "line_totals": result["line_totals"],
        "grand_total": grand,
        "email_draft": {"en": en, "ar": ar}
    }
