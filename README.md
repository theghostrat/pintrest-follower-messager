# Pintrest-follower-messager
Automatically messages the users from a follower list this is the part of a big automatic markiting tool which i am creating

Welcome to the Pinterest Follower Message Bot repository! This Python script automates sending welcome messages to new followers on Pinterest using the Pinterest API.

## How It Works

1. The script authenticates with your Pinterest account using your username and password.
2. It retrieves the list of your followers from Pinterest.
3. If a follower is not present in the `followers.json` file (indicating that they are a new follower), the script sends them a personalized welcome message using the Pinterest API.
4. The follower's username is then added to the `followers.json` file to keep track of sent messages.

## Usage

Follow these steps to start using the Pinterest Follower Message Bot:

1. Usage:

   ```bash
   pip install pinterest-api
   git clone https://github.com/theghostrat/pintrest-follower-messager.git
   cd pintrest-follower-messager
   python main.py


