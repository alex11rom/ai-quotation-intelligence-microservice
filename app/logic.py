from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List
from .models import Item

def calc_line_total(item: Item) -> Decimal:
    unit = Decimal(str(item.unit_cost))
    margin = Decimal(str(item.margin_pct)) / Decimal("100")
    qty = Decimal(item.qty)
    total = unit * (Decimal("1") + margin) * qty
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def build_quote(items: List[Item]) -> Dict:
    line_totals = []
    grand = Decimal("0")
    for it in items:
        lt = calc_line_total(it)
        line_totals.append({"sku": it.sku, "line_total": float(lt)})
        grand += lt
    grand = grand.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {"line_totals": line_totals, "grand_total": float(grand)}
