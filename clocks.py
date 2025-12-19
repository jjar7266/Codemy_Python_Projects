# Codemy.com - Instructor John Elder

# clocks.py

# Modified instructors code to be more Pythonic and readable

import os
import sys
import time
import threading
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_thread(stop_event):
    # Press Enter to stop
    try:
        input()
    except Exception as e:
        print(f"[input_thread] error: {e}")
    finally:
        stop_event.set()

def show_time(zone_name):
    try:
        tz = ZoneInfo(zone_name)
    except ZoneInfoNotFoundError as e:
        print(f"[show_time] Zone not found: {zone_name} -> {e}. Falling back to UTC.")
        tz = ZoneInfo("UTC")
    except Exception as e:
        print(f"[show_time] Unexpected error for {zone_name}: {e}. Falling back to UTC.")
        tz = ZoneInfo("UTC")

    now = datetime.now(tz)
    return now.strftime("%m-%d-%Y %I:%M:%S %p")

def main():
    zones = {
        "1": "America/New_York",
        "2": "America/Chicago",
        "3": "America/Denver",
        "4": "America/Los_Angeles",
        "5": "Europe/London",
        "6": "Asia/Tokyo"
    }

    clear_screen()
    print("Choose a time zone:")
    for key, val in zones.items():
        print(f"{key}. {val}")
    choice = input("Enter choice: ").strip()

    zone = zones.get(choice, "America/New_York")
    print(f"[debug] choice='{choice}', zone='{zone}'")
    print(f"[debug] python='{sys.version}', exe='{sys.executable}'")

    # Probe the zone once so we fail early with a clear message
    try:
        _ = ZoneInfo(zone)
        print(f"[debug] ZoneInfo('{zone}') created successfully")
    except Exception as e:
        print(f"[fatal] Could not load zone '{zone}': {e}")
        print("[hint] Ensure you are inside your venv and tzdata is installed there.")
        return

    stop_event = threading.Event()
    thread = threading.Thread(target=input_thread, args=(stop_event,), daemon=True)
    thread.start()

    try:
        while not stop_event.is_set():
            clear_screen()
            print(f"Time in {zone}: {show_time(zone)}")
            print("Press Enter to stop the clock...")
            time.sleep(1)
    except Exception as e:
        print(f"[loop] Unexpected error: {e}")
    finally:
        clear_screen()
        print("Clock Stopped...")

if __name__ == "__main__":
    main()