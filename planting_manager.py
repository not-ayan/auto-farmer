# planting_manager.py

import asyncio
import logging

# Crop information
crops = {
    '🌽': {'name': 'corn', 'boosts': 0, 'harvest_time': 300},
    '🍅': {'name': 'tomato', 'boosts': 1, 'harvest_time': 0},
    '🌶': {'name': 'pepper', 'boosts': 1, 'harvest_time': 60},
    '🥔': {'name': 'potato', 'boosts': 3, 'harvest_time': 60},
    '🍆': {'name': 'eggplant', 'boosts': 6, 'harvest_time': 60},
    '🥕': {'name': 'carrot', 'boosts': 8, 'harvest_time': 60}
}

async def plant_crops(client, crop, amount, max_slots, corn_boost_enabled):
    # Determine the number of slots to plant
    slots_to_use = min(amount, max_slots)

    planting_command = f'/plant {crops[crop]["name"]} {slots_to_use}'
    await client.send_message('fam_tree_bot', planting_command)
    logging.info(f"Planted {slots_to_use} {crop}")

    # Special handling for corn boost
    if crop == '🌽' and corn_boost_enabled:
        await asyncio.sleep(1)
        await client.send_message('fam_tree_bot', f'/boost {crops[crop]["name"]}')
        logging.info(f"Boosted {slots_to_use} {crop}")

    # Boost other crops
    if crop != '🌽':
        await asyncio.sleep(1)
        for _ in range(crops[crop]['boosts']):
            await client.send_message('fam_tree_bot', f'/boost {crops[crop]["name"]}')
            logging.info(f"Boosted {slots_to_use} {crop}")
            await asyncio.sleep(0.1)

    await asyncio.sleep(crops[crop]['harvest_time'])
    await client.send_message('fam_tree_bot', f'/harvest {crops[crop]["name"]}')
    logging.info(f"Sent harvest command for {slots_to_use} {crop}")
