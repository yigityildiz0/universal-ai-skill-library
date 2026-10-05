#!/usr/bin/env python3
"""Normalize landed prices and transparent value scores from JSON offers."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("offers", type=Path)
    parser.add_argument("--base-currency", required=True)
    args = parser.parse_args()
    offers = json.loads(args.offers.read_text(encoding="utf-8"))
    if not isinstance(offers, list) or not offers:
        raise SystemExit("offers must be a non-empty JSON array")

    rows = []
    for offer in offers:
        required = {"name", "price", "currency", "fx_to_base", "quantity", "quantity_unit"}
        missing = required - offer.keys()
        if missing:
            raise SystemExit(f"{offer.get('name', 'offer')} missing {sorted(missing)}")
        price = float(offer["price"])
        tax = float(offer.get("tax", 0))
        shipping = float(offer.get("shipping", 0))
        mandatory_fees = float(offer.get("mandatory_fees", 0))
        discount = float(offer.get("discount", 0))
        quantity = float(offer["quantity"])
        fx = float(offer["fx_to_base"])
        if price < 0 or quantity <= 0 or fx <= 0:
            raise SystemExit("price must be non-negative; quantity and fx_to_base positive")
        landed = (price + tax + shipping + mandatory_fees - discount) * fx
        unit_price = landed / quantity
        quality = offer.get("quality_score")
        value = float(quality) / unit_price if quality is not None and unit_price > 0 else None
        rows.append({
            "name": offer["name"],
            "base_currency": args.base_currency,
            "landed_price": landed,
            "normalized_unit_price": unit_price,
            "quantity_unit": offer["quantity_unit"],
            "quality_score": quality,
            "value_score": value,
            "fx_timestamp": offer.get("fx_timestamp"),
            "observed_at": offer.get("observed_at"),
        })
    price_rank = sorted(rows, key=lambda row: row["normalized_unit_price"])
    value_rank = sorted([row for row in rows if row["value_score"] is not None], key=lambda row: row["value_score"], reverse=True)
    print(json.dumps({
        "offers": rows,
        "cheapest_normalized": [row["name"] for row in price_rank],
        "best_value_when_scored": [row["name"] for row in value_rank],
        "warning": "Value ranking is only as valid as the explicit quality scores and weights.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
