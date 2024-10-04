# Discord Call Bot

A Discord bot that allows users to initiate and receive voice calls in a Discord server.

## Description

This bot provides functionality to make voice calls between users in a Discord server. It uses the `py-cord` library to interact with the Discord API.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/laptaka/ServerCallBot.git
    cd ServerCallBot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv

    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Linux or MacOS
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Discord bot token:
    ```env
    TOKEN=your_discord_bot_token
    ```

## Usage

1. Run the bot:
    ```sh
    python main.py
    ```

2. Use the `/call` command to initiate a call to another user:
    ```sh
    /call @username
    ```

## License

This project is licensed under the GNU General Public License. See the [LICENSE](LICENSE) file for details.