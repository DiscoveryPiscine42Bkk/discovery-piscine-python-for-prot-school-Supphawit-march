def multiplication_table(number):
    print(f"multiplication {number}")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

# กำหนดแม่สูตรคูณที่ต้องการ
number = int(input("Enter the number: "))
multiplication_table(number)