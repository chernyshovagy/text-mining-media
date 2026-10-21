import csv


# Функция для преобразования тональности в число
def sentiment_to_num(sentiment):
    sentiment = sentiment.lower().strip()
    if sentiment == 'positive':
        return 1
    elif sentiment == 'negative':
        return -1
    else:  # neutral, positive/negative и другие случаи
        return 0


# Чтение исходного файла и запись в CSV
def convert_txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        writer = csv.writer(outfile)
        writer.writerow(['lemma', 'sentiment'])  # Заголовок CSV

        for line in infile:
            parts = line.strip().split(', ')
            if len(parts) >= 4:  # Проверяем, что строка содержит достаточно данных
                lemma = parts[2]  # Лемматизированная форма (3-й элемент)
                sentiment = parts[3]  # Тональность (4-й элемент)
                sentiment_num = sentiment_to_num(sentiment)
                writer.writerow([lemma, sentiment_num])


# Пример использования
input_file = 'rusentilex.txt'  # Ваш исходный файл
output_file = 'rusentilex.csv'  # Выходной CSV
convert_txt_to_csv(input_file, output_file)

print(f"Файл успешно преобразован: {output_file}")