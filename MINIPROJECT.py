laptop = 0
phone = 0
tablet = 0

while True:
    print("\n--- MENU ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát")

    choice = input("Chọn chức năng: ")

    
    if choice == "1":
        print("\n===== BÁO CÁO TỒN KHO =====")
        print("Laptop:", laptop)
        print("Phone :", phone)
        print("Tablet:", tablet)

    
    elif choice == "2":
        print("\n--- Chọn mặt hàng ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng: ")
        quantity = int(input("Nhập số lượng: "))

        if product == "1":
            laptop += quantity
        elif product == "2":
            phone += quantity
        elif product == "3":
            tablet += quantity
        else:
            print("Mặt hàng không hợp lệ!")

    
    elif choice == "3":
        print("\n--- Chọn mặt hàng ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        product = input("Chọn mặt hàng: ")
        quantity = int(input("Nhập số lượng xuất: "))

        if product == "1":
            laptop -= quantity
        elif product == "2":
            phone -= quantity
        elif product == "3":
            tablet -= quantity
        else:
            print("Mặt hàng không hợp lệ!")

    
    elif choice == "4":
        print("\n--- CẢNH BÁO TỒN KHO THẤP ---")
        if laptop < 5:
            print("Laptop sắp hết!")
        if phone < 5:
            print("Phone sắp hết!")
        if tablet < 5:
            print("Tablet sắp hết!")

    
    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Chức năng không hợp lệ!")