import random
import string

# Tạo key ngẫu nhiên
def generate_random_key():
    prefix = "HappyHub_"
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"{prefix}{random_part}"

# Sinh key mới
key = generate_random_key()

# Cập nhật nội dung file HappyHubKey.txt
with open("HappyHubKey.txt", "w") as file:
    file.write(key)

print(f"New key generated and saved: {key}")
