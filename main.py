import webbrowser
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def open_telegram():
    # Display the ASCII art in green
    print(Fore.GREEN + Style.BRIGHT + """
   /$$                                      /$$ /$$$$$$                                /$$   /$$ /$$      /$$
  | $$                                     /$$//$$__  $$                              | $$  / $$| $$  /$ | $$
 /$$$$$$      /$$$$$$/$$$$   /$$$$$$      /$$/| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$ |  $$/ $$/| $$ /$$$| $$
|_  $$_/     | $$_  $$_  $$ /$$__  $$    /$$/ | $$       /$$__  $$ /$$__  $$ /$$__  $$ \  $$$$/ | $$/$$ $$ $$
  | $$       | $$ \ $$ \ $$| $$$$$$$$   /$$/  | $$      | $$  \ $$| $$  \__/| $$  \ $$  >$$  $$ | $$$$_  $$$$
  | $$ /$$   | $$ | $$ | $$| $$_____/  /$$/   | $$    $$| $$  | $$| $$      | $$  | $$ /$$/\  $$| $$$/ \  $$$
  |  $$$$//$$| $$ | $$ | $$|  $$$$$$$ /$$/    |  $$$$$$/|  $$$$$$/| $$      | $$$$$$$/| $$  \ $$| $$/   \  $$
   \___/ |__/|__/ |__/ |__/ \_______/|__/      \______/  \______/ |__/      | $$____/ |__/  |__/|__/     \__/
                                                                            | $$                             
                                                                            | $$                             
                                                                            |__/                             
""")
    # Add a blank line for spacing
    print("\n")

    # Display styled and colored text with extra spacing
    print(Fore.CYAN + Style.BRIGHT + "🚀 Join our Telegram group to explore our products and place your orders!\n")
    print(Fore.YELLOW + "💡 For more information, please follow the instructions below.\n")
    
    # Wait for the user to press Enter
    input(Fore.GREEN + Style.BRIGHT + "👉 Press Enter to continue...\n")

    # Open the Telegram link
    telegram_link = "https://t.me/CorpXW"
    webbrowser.open(telegram_link)

if __name__ == "__main__":
    open_telegram()
