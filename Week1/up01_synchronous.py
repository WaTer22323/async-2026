import threading
from time import sleep, ctime, time
import os

def update_cup_number(customer_name):
    pid = os.getpid() # ดึง PID ของ Process ปัจจุบัน
    thread_id = threading.current_thread().native_id # ดึง Thread ID ของ Thread ปัจจุบัน
    thread_name = threading.current_thread().name # ดึงชื่อ Thread ปัจจุบัน

    pass

def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id #  ดึง Thread ID ของ Thread ปัจจุบัน
    thread_name = threading.current_thread().name # ดึงชื่อ Thread ปัจจุบัน

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...") 
    sleep(1)  # บล็อกการทำงานของ Thread นี้ไว้ 1 วินาที
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")
    pass

def main():
    queue = ['A', 'B', 'C'] # ลิสต์ลูกค้าที่เข้ามาในคิว (ทีละคน)
    main_pid = os.getpid() # ดึง PID ของ Process หลัก
    main_tid = threading.current_thread().native_id # ดึง Thread ID ของ Thread หลัก

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Synchronous ===")
    start_time = time() # บันทึกเวลาที่เริ่มทำงาน

    # ลูปทำงานตามลำดับคิวเดียว (ทีละคน)
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")
    pass

if __name__ == "__main__":
    main()