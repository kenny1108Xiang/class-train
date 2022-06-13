if __name__ == "__main__":
    print("1.計算數字\n2.抽數字\n3.離開")
    op = input('請輸入：')
    if op == "1":
        from computer_use import computer
        num1, num2 = map(int, input("輸入兩數字，並用'+'隔開：").split("+"))
        print(computer.num_add(num1, num2))
    elif op == "2":
        from random_use import random_use
        how_many = int(input("請輸入數量："))
        start, end = map(int,input("請輸入範圍，並用'~'隔開：").split("~"))
        random_use.random_int(how_many, start, end)
