#https://github.com/s-getmanov/st_python5.git

num = int(input("Введите целое число: "))

if num%2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

if num > 0:
    sign = "положительное"
elif num < 0:
    sign = "отрицательное"

digits = str(len(str(num)))

if num == 0:
    print("Это ноль! Больше тут сказать нечего.")
else:
    print(f"Это {digits}-разрядное {sign} {parity} число.")