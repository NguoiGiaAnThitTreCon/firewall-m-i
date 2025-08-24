from pypresence import Presence
import time

CLIENT_ID = "1409023112242139247"  # Application ID bạn tạo
RPC = Presence(CLIENT_ID)
RPC.connect()

# Fake giờ = bắt đầu từ năm 1970 (epoch = 1 giây)
fake_start = 1  

RPC.update(

    large_image="default",    
    large_text="Fake activity",
    start=fake_start   # truyền timestamp giả
)

print("Đang fake giờ xanh siêu to")
while True:
    time.sleep(15)
