def reverse(string):
    return string[::-1]

def test_reverse():
    # Чтение исходного текста из фикстуры
    with open('tests/fixtures/input.txt', encoding='utf8') as f:
        input_data = f.read().strip()  # Удаляем лишние символы новой строки
    
    # Чтение перевёрнутого текста из фикстуры
    with open('tests/fixtures/reversed.txt', encoding='utf8') as f:
        expected_output = f.read().strip()  # Удаляем лишние символы новой строки
    
    # Проверка, что функция `reverse` возвращает ожидаемый результат
    assert reverse(input_data) == expected_output
