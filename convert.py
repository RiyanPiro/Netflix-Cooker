import json, os

def boolToString(s):
    if s:
        return "TRUE"
    else:
        return "FALSE"

def checkTailMatch(s):
    if s[0] == ".":
        return "TRUE"
    return "FALSE"

cookies = os.listdir('convert')
for cookie in cookies:
    try:
        cookie_path = "convert/" + cookie

        data = json.loads(open(cookie_path, 'r', encoding='utf-8').read())
        write = open(f'converted/{cookie}', 'w', encoding='utf-8')

        for x in data:
            write.write(x["domain"] + '\t' + checkTailMatch(x["domain"]) + '\t' + x["path"] + '\t' + boolToString(x["secure"]) + '\t' + "0" + '\t' + x["name"] + '\t' + x["value"] + '\n')
    except Exception as e:
        print(f"Error: {e} with {cookie}")
        continue

print("Completed converting cookies")