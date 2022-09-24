# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'мы неабв очень любим питон иабв джавуабв '.split()
text2 = 'абв'
list = [text[i] for i in range(len(text)) if not text2 in text[i] ]
print(list)