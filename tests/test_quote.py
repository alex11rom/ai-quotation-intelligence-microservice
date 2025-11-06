from app.models import Item
from app.logic import calc_line_total, build_quote

def test_calc_line_total():
    item = Item(sku="X", qty=2, unit_cost=10.0, margin_pct=10)
    lt = calc_line_total(item)
    assert float(lt) == 22.00  # 10*(1+0.1)*2

def test_build_quote():
    items = [
        Item(sku="A", qty=1, unit_cost=100, margin_pct=10),
        Item(sku="B", qty=2, unit_cost=50, margin_pct=0)
    ]
    out = build_quote(items)
    assert round(out["grand_total"], 2) == 210.00
