# mode_manager.py

import logging
from config import chat_id

# State variables for modes
corn_boost_enabled = False
all_mode_enabled = False
corn_in_all_mode = False

async def toggle_all_mode(client):
    global all_mode_enabled
    all_mode_enabled = not all_mode_enabled
    status = "enabled" if all_mode_enabled else "disabled"
    await client.send_message(chat_id, f"All crops mode {status} for crops.")
    logging.info(f"All crops mode {status}.")

async def toggle_corn_boost(client):
    global corn_boost_enabled
    corn_boost_enabled = not corn_boost_enabled
    status = "enabled" if corn_boost_enabled else "disabled"
    await client.send_message(chat_id, f"Corn boost {status}.")
    logging.info(f"Corn boost {status}.")

async def add_corn_to_all(client):
    global corn_in_all_mode
    corn_in_all_mode = True
    await client.send_message(chat_id, "Corn has been added to all mode.")
    logging.info("Corn has been added to all mode.")

async def remove_corn_from_all(client):
    global corn_in_all_mode
    corn_in_all_mode = False
    await client.send_message(chat_id, "Corn has been removed from all mode.")
    logging.info("Corn has been removed from all mode.")
