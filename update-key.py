import random
import requests
import string

# Tạo key ngẫu nhiên
def generate_random_key():
    prefix = "HappyHub_"
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=16))  # Tạo chuỗi ngẫu nhiên 16 ký tự
    return f"{prefix}{random_part}"

key = generate_random_key()

# Gửi key lên GitHub
url = "https://api.github.com/repos/username/repo/contents/HappyHubKey.txt"
headers = {"Authorization": "Bearer YOUR_GITHUB_ACCESS_TOKEN"}
data = {
    "message": "Update key",  # Lời nhắn commit
    "content": key.encode("utf-8").hex(),  # Mã hóa key
    "branch": "main"  # Nhánh repository
}

response = requests.put(url, headers=headers, json=data)
print(response.status_code, response.json())
