import random
import string
import requests
from datetime import datetime

# Hàm tạo key ngẫu nhiên
def generate_key():
    prefix = "HappyHub_"
    random_string = ''.join(random.choices(string.ascii_letters + string.digits + "@#$%", k=16))
    return prefix + random_string

# Hàm cập nhật file trên GitHub
def update_key_on_github(key):
    url = "https://api.github.com/repos/3sut2z/HappyHub-Key/contents/HappyHubKey.txt"
    headers = {
        "Authorization": f"Bearer {os.getenv('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')}"
    }
    
    # Lấy SHA của file hiện tại (nếu có)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None
    
    # Cập nhật file với key mới
    data = {
        "message": f"Update key for {datetime.now().strftime('%Y-%m-%d')}",
        "content": key.encode("utf-8").hex(),
        "branch": "main"
    }
    if sha:
        data["sha"] = sha

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 201 or response.status_code == 200:
        print("Key updated successfully!")
    else:
        print("Failed to update key:", response.json())

if __name__ == "__main__":
    new_key = generate_key()
    update_key_on_github(new_key)
