# order_parser.py

import re

async def parse_orders(message):
    crops_needed = {}
    available_crops = {}

    # Use regex to parse the order message
    orders = re.findall(r'(\S+)\s+(\d+)/(\d+)\s*[✅❌]', message)

    for crop, available, needed in orders:
        available_crops[crop] = int(available)
        crops_needed[crop] = int(needed)

    return crops_needed, available_crops
