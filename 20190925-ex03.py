BMI = 0
height = int (input("請輸入身高 (Cm)："))
weight = int (input("請輸入體重 (Kg)："))
BMI = (weight) / ((height/100)*(height/100))
print ("BMI = %f\n" % (BMI))
if BMI < 18.5:
    print("過瘦")
if (BMI >=18.5 and BMI <24):
    print ("標準")
if BMI >= 24:
    print("過重")