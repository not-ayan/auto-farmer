# bot.py

from telethon import TelegramClient, events
import logging
import asyncio
import re

# Import other modules
from config import api_id, api_hash, phone_number, chat_id, garden_name
from order_parser import parse_orders
from planting_manager import plant_crops
from mode_manager import toggle_all_mode, toggle_corn_boost, add_corn_to_all, remove_corn_from_all

# Setup logging
logging.basicConfig(level=logging.INFO)

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

# Global flag for running status
running = False
corn_boost_enabled = False
all_mode_enabled = False
corn_in_all_mode = False

# Maximum slots available
max_slots = 1000

async def update_slots(client):
    global max_slots
    await client.send_message('fam_tree_bot', '/gn')
    await asyncio.sleep(5)
    async for message in client.iter_messages('fam_tree_bot', limit=1):
        match = re.search(rf"{garden_name}\s*\((\d+)\)", message.message)
        if match:
            max_slots = int(match.group(1))
            logging.info(f"Updated max_slots to {max_slots}")

async def main_task(event):
    global running
    if event.raw_text == '.start':
        running = True
        await client.send_message(chat_id, "Processes started.")
        logging.info("Processes started.")

        # Main loop for planting tasks
        while running:
            await client.send_message('fam_tree_bot', '/orders')
            await asyncio.sleep(5)
            async for message in client.iter_messages('fam_tree_bot', limit=1):
                if 'Orders' in message.message:
                    crops_needed, available_crops = await parse_orders(message.message)
                    logging.info(f"Crops needed: {crops_needed}")
                    logging.info(f"Available crops: {available_crops}")

                    for crop, needed in crops_needed.items():
                        if crop in available_crops:
                            available = available_crops[crop]
                            needed -= available
                        if needed > 0:
                            await plant_crops(client, crop, needed, max_slots, corn_boost_enabled)

            await update_slots(client)

    elif event.raw_text == '.stop':
        running = False
        await client.send_message(chat_id, "Processes stopped. Use .start to resume.")
        logging.info("Processes stopped.")

    elif event.raw_text == '.all':
        await toggle_all_mode(client)

    elif event.raw_text == '.boost':
        await toggle_corn_boost(client)

    elif event.raw_text == '.con':
        await add_corn_to_all(client)

    elif event.raw_text == '.coff':
        await remove_corn_from_all(client)

# Event handlers
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.start'))
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.stop'))
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.all'))
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.boost'))
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.con'))
client.add_event_handler(main_task, events.NewMessage(chats=chat_id, pattern=r'\.coff'))

# Start the client
client.start(phone=phone_number)
client.run_until_disconnected()
