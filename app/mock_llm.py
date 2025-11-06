def generate_email_draft_en(client_name: str, grand_total: float, currency: str, delivery_terms: str, notes: str) -> str:
    return (
        f"Dear {client_name},\n\n"
        f"Our quotation total is {currency} {grand_total:,.2f}.\n"
        f"Delivery terms: {delivery_terms}.\n"
        f"Notes: {notes}\n\n"
        f"Best regards,\nAlrouf Sales Team"
    )

def generate_email_draft_ar(client_name: str, grand_total: float, currency: str, delivery_terms: str, notes: str) -> str:
    return (
        f"السيد/ة {client_name} المحترم/ة،\n\n"
        f"إجمالي عرض السعر: {currency} {grand_total:,.2f}.\n"
        f"شروط التسليم: {delivery_terms}.\n"
        f"ملاحظات: {notes}\n\n"
        f"مع التحية،\nفريق مبيعات الروف"
    )
