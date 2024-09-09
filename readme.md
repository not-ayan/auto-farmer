# Telegram Farming Bot

This bot automates the farming process for Telegram's garden-based game by handling crop orders, planting, boosting, and harvesting crops based on different modes. It also allows toggling between different features like boosting and "all crops mode."

## Features

- **Order Parsing:** The bot parses crop orders and calculates the number of each crop that needs to be planted.
- **Planting, Boosting, and Harvesting:** Automatically plants, boosts, and harvests crops in the garden based on orders and available slots.
- **Modes:**
  - **`.all` mode:** Automatically plants all the crops specified in the orders. Corn can be optionally added with `.con` or excluded with `.coff`.
  - **`.boost` mode:** Toggles boosting for Corn crops. When enabled, Corn gets planted with boosts and its harvest time is set to 0.
  - **`.start` and `.stop`:** Start and stop the automation processes without stopping the bot.
  
## Commands

- **`.start`**: Starts the automation process. The bot begins by parsing orders and managing the crop planting, boosting, and harvesting.
  
- **`.stop`**: Stops the automation process without shutting down the bot. The bot will stop planting, boosting, or harvesting until `.start` is issued again.
  
- **`.boost`**: Toggles boost mode for Corn. When enabled, Corn will be planted with boosts and its harvest time is reduced to 0. When disabled, Corn behaves normally.
  
- **`.all`**: Toggles "all crops mode." In this mode, the bot will plant all available crops from the order in bulk. Corn is excluded unless `.con` is enabled.
  
- **`.con`**: Enables Corn planting in "all crops mode." Corn will be included in the bulk planting process.
  
- **`.coff`**: Disables Corn planting in "all crops mode." Corn will be excluded from the bulk planting process.

## Project Structure

- **`bot.py`**: The main script that runs the bot and handles the commands.
  
- **`config.py`**: Contains your Telegram API credentials (`api_id`, `api_hash`, `phone_number`) and the garden owner's name (e.g., `"Ayan"` in `Ayan's Garden`).
  
- **`orders.py`**: Script responsible for parsing orders received from the bot and calculating how many crops need to be planted.
  
- **`planting.py`**: Script that handles the actual planting, boosting, and harvesting of crops. Includes the logic for managing slots and ensuring crops are planted in batches if needed.
  
- **`modes.py`**: Contains all the different modes (.all, .con, .coff, .boost) and their logic for toggling the bot's behavior.

## Setup

### Prerequisites

1. Python 3.x
2. Telegram API credentials (api_id, api_hash, phone number).

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/telegram-farming-bot.git
    ```
    
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your API credentials:
   - Open `config.py` and fill in your `api_id`, `api_hash`, `phone_number`, and the garden owner's name.

### Running the Bot

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Interact with the bot via Telegram and use the supported commands to control its behavior.

### Example Interaction

1. Start the bot with `.start`:
    - The bot will parse your crop orders and start planting and boosting crops automatically.

2. Toggle boosting for Corn with `.boost`:
    - Corn will be planted with boosts and harvested with a reduced time when this mode is on.

3. Use `.all` to plant all the crops specified in the orders:
    - You can choose to include or exclude Corn using `.con` or `.coff`.

4. Stop the automation with `.stop`:
    - The bot will pause planting, boosting, and harvesting but will remain running.

---

## Notes

- The bot is designed to work with a specific garden-based Telegram game. Ensure the commands and crop types align with the game's mechanics.
  
- The bot supports dynamic slot updates, so if your garden gets more slots, the bot will adapt accordingly.

## License

This project is licensed under the MIT License.

---

Feel free to modify the content as per your specific game or personal preferences.
