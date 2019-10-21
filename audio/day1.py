import random

# 亂數出題
signs_ls = ['+', '-', '*', '/'] # 顯示及判斷時使用

# 產生隨機數字與運算符號
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)

sign1 = signs_ls[random.randint(0, 3)]

# 透過運算符號，產生答案
if sign1 == '+':
    ans = num1 + num2
elif sign1 == '-':
    ans = num1 - num2
elif sign1 == '*':
    ans = num1 * num2
elif sign1 == '/':
    ans = round(num1 / num2, 2)

print('題目: %d %s %d = ' % (num1, sign1, num2))
print(ans)