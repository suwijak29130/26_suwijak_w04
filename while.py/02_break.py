numbers = [12,15,69,21.24,30]
divisor = 6 

print(f"ตัวหาร {divisor} ลงตัว")
found = 0

for i in numbers:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} หารได้ลงตัว(={i // divisor})")
        found += 1 
        
        if found ==3:
            break