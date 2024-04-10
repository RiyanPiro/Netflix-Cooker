import os

for cookie in os.listdir("convert"):
    cookie_path = f"convert/{cookie}"
    with open(cookie_path, 'r') as file:
        lines = file.readlines()

    modified_lines = lines[7:-1]

    with open(cookie_path, 'w') as file:
        file.writelines(modified_lines)