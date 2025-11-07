# open_wc_results_pyautogui.py
import webbrowser
import pyautogui
import time
import sys

# ---- Configuration ----
# URL to open (change if you want a different site)
url = "https://www.cricbuzz.com/cricket-series/10009/icc-womens-world-cup-2025/matches"

# How long to wait for pages to load (increase if your network is slow)
initial_wait = 6
page_wait = 3

# ---- Script starts ----
def main():
    try:
        print("Opening browser to:", url)
        webbrowser.open(url)          # open the URL in the default browser
        time.sleep(initial_wait)      # wait for browser to open and page to load

        # Bring the browser window to the front (Windows)
        # If you're on Mac / Linux you can remove or modify these hotkeys
        try:
            pyautogui.hotkey('alt', 'tab')   # switch to the browser (may require repeating)
            time.sleep(0.5)
        except Exception:
            pass

        # Optional: maximize window (Windows)
        # pyautogui.hotkey('win', 'up')

        # If you want to open the "first link" on the search results page:
        # - If you opened a search results URL instead of direct page, you can press TAB a few times then ENTER.
        # Example (uncomment if you need it):
        # pyautogui.press('tab', presses=6, interval=0.25)
        # pyautogui.press('enter')

        print("Done — page should be open in your default browser.")
    except KeyboardInterrupt:
        print("Cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
