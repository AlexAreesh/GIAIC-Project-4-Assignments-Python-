import random
import string

length = 8
all_chars = string.ascii_letters + string.digits
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Password:", password)
