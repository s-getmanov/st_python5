#https://github.com/s-getmanov/st_python5.git

#Все исходные данные будем запрашивать у пользователя.

min_summ = int(input("Введите размер минимальной суммы инвестиций: "))
mike_summ = int(input("Введите количество денег у инвестора 'Майк': "))
ivan_summ = int(input("Введите количество денег у инвестора 'Иван': "))



if mike_summ >= min_summ and ivan_summ >= min_summ:
    print("2")
elif mike_summ >= min_summ and ivan_summ <= min_summ:
    print("Mike")
elif mike_summ <= min_summ and ivan_summ >= min_summ:
    print("Ivan")
elif mike_summ <= min_summ and ivan_summ <= min_summ and mike_summ + ivan_summ >= min_summ:
    print("1")
elif mike_summ <= min_summ and ivan_summ <= min_summ and mike_summ + ivan_summ <= min_summ:
    print("0")