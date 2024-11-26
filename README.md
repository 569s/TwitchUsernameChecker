# TWITCH USERNAME CHECKER

This Python script helps you check the availability of Twitch usernames. It generates random usernames and checks them using the Twitch API.

## Features
- Checks username availability in real-time.
- Multithreaded for faster checks.
- Saves available usernames to a file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/569s/TwitchUsernameChecker.git
   cd TwitchUserCheck
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

  # Usage

  1. Run the script:
 ```bash
  python main.py
```
 Input the required details when prompted:

 - Choose the type of username (letters, numbers, or mixed).
 - Enter the number of threads for multi-threaded execution.
 - Set the username length.

 Available usernames will be printed in green and saved in available.txt.
