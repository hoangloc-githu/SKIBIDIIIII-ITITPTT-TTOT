import pyautogui
import time

# Nhập dữ liệu
so_lan = int(input("Nhập số lần cần gõ: "))
phut = int(input("Nhập khoảng bao nhiêu phút mỗi lần gõ: "))
noidung = input("Nhập nội dung cần gõ: ")

delay = phut * 60  # chuyển phút sang giây

print(f"Bắt đầu, sẽ gõ '{noidung}' {so_lan} lần, mỗi lần cách nhau {phut} phút.")
time.sleep(2)

for i in range(so_lan):
    print(f"Gõ lần {i+1}/{so_lan}...")
    pyautogui.write(noidung)
    pyautogui.press("enter")

    if i < so_lan - 1:
        print(f"Chờ {phut} phút để gõ lần tiếp theo...")
        time.sleep(delay)

print("Hoàn thành.")
