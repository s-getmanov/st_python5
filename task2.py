#https://github.com/s-getmanov/st_python5.git

#Создадим словарь с ключами из букв, которые считаем гласными по условиям задачи
#Будем использовать их и для определения гласных, и для хранения количества. 
vowel_letters = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}

kol_vowel_letters = 0

#Введем слово
word = input("Введите слово: ")

#Пройдем по строке циклом и посчитаем буквы
for lett in word:
    #Есть ключ, это гласная
    if lett in vowel_letters:
        vowel_letters[lett] = vowel_letters[lett] + 1
        kol_vowel_letters = kol_vowel_letters + 1    

print(f"Количество согласных: {len(word) - kol_vowel_letters}")
print(f"Количество гласных: {kol_vowel_letters}")
print("В том числе:")

for key in vowel_letters:
    print(f"{key}: {vowel_letters[key]}")
