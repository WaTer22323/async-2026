from time import sleep, ctime, time
import threading
import os

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid() # ดึง PID ของ Process ปัจจุบัน
    thread_id = threading.current_thread().native_id # ดึง Thread ID ของ Thread ปัจจุบัน
    thread_name = threading.current_thread().name # ดึงชื่อ Thread ปัจจุบัน

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sleep(5)  # บล็อกการทำงานของ Thread นี้ไว้ 5 วินาทีเต็ม
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")
    pass

def main():
    queue = ['A', 'B', 'C'] # ลิสต์ลูกค้าที่เข้ามาในคิว (ทีละคน)
    main_pid = os.getpid() # ดึง PID ของ Process หลัก
    main_tid = threading.current_thread().native_id # ดึง Thread ID ของ Thread หลัก

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Multi-Thread ===")
    start_time = time() # บันทึกเวลาที่เริ่มทำงาน
    
    threads = [] # สร้างลิสต์เก็บ Thread ที่สร้างขึ้น
    # ลูปสร้าง Thread สำหรับลูกค้าแต่ละคนในคิว

    for customer in queue:
        t = threading.Thread(target=make_coffee, args=(customer,), name=f"Thread-{customer}") # สร้าง Thread ใหม่
        threads.append(t) # เก็บ Thread ที่สร้างขึ้นในลิสต์
        t.start() # เริ่มทำงาน Thread ที่สร้างขึ้น

        for t in threads:
            t.join() # รอให้ Thread ทำงานเสร็จสิ้นก่อนที่จะไปทำงานต่อ

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")
    pass

if __name__ == "__main__":
    main()