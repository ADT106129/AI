sum = 0
n = int (input("請輸入正整數："))
for i in range(1, n+1):#運算公式
    sum += i
    print("1到 %d 的整數和為 %d" % (n, sum))
    print("執行次數：%d" % (i))#顯示執行次數