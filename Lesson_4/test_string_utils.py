# Импортирую библиотеку pytest
import pytest

# Импортирую класс StringUtils из файла string_utils
from string_utils import StringUtils

# Создаю экземпляр класса StringUtils
string_utils = StringUtils()

## Убираем пробелы перед словом
def test_trim():
    string_utils = StringUtils()
    res = string_utils.trim('  Anton')
    assert res == 'Anton'
def test_trim1():
    string_utils = StringUtils()
    res = string_utils.trim('  4 april 2023')
    assert res == '4 april 2023'

## Негативные тест кейсы
@pytest.mark.xfail(strict=True)
def test_trim_n1():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == '  Anton'

## Выводим слово с заглавной  
def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'Anton'

## Негативный тест кейс
@pytest.mark.xfail(strict=True)
def test_capitilize_n1():
    string_utils = StringUtils()
    res = string_utils.capitilize('')
    assert res == 'Anton'

## Превращаем значения в список
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list('Ark')
    assert res == ['Ark']
def test_to_list_two():
    string_utils = StringUtils()
    res = string_utils.to_list("")
    assert res == []
def test_to_list_three():
    string_utils = StringUtils()
    res = string_utils.to_list(" ")
    assert res == []

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_to_list_n1():
    string_utils = StringUtils()
    res = string_utils.to_list('Ark')
    assert res == 'Ark'

## Поиск буквы в слове
def test_contains():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "t")
    assert res == True
def test_contains2():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "o")
    assert res == True

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_contains_n1():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", 1)
    assert res == True
@pytest.mark.xfail(strict=True)
def test_contains_n2():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", None)
    assert res == True
@pytest.mark.xfail(strict=True)
def test_contains_n3():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", " ")
    assert res == True

## Удаление символов
def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "nton"

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_delete_symbol_n2():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", 1)
    assert res == "Anton"
@pytest.mark.xfail(strict=True)
def test_delete_symbol_n2():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", None)
    assert res == "Anton"


## Проверка буквы начала слова
def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "A")
    assert res == True

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_starts_with_n2():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_starts_with_n3():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", 1)
    assert res == True
@pytest.mark.xfail(strict=True)
def test_starts_with_n4():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", None)
    assert res == True


## Проверка буквы окончания слова
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "n")
    assert res == True

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_end_with_n2():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", " ")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_end_with_n3():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", 123)
    assert res == True
@pytest.mark.xfail(strict=True)
def test_end_with_n4():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", None)
    assert res == True

## Проверка пустой строки
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True
def test_is_empty_two():
    string_utils = StringUtils()
    res = string_utils.is_empty(" ")
    assert res == True

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_is_empty_n1():
    string_utils = StringUtils()
    res = string_utils.is_empty(123)
    assert res == True
@pytest.mark.xfail(strict=True)
def test_is_empty_n2():
    string_utils = StringUtils()
    res = string_utils.is_empty("Антон")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_is_empty_n3():
    string_utils = StringUtils()
    res = string_utils.is_empty(None)
    assert res == True

## Перевод списка в строку
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ("A, n, t, o, n")

## Негативные проверки
@pytest.mark.xfail(strict=True)
def test_list_to_string_n1():
    string_utils = StringUtils()
    res = string_utils.list_to_string([123])
    assert res == [123]
@pytest.mark.xfail(strict=True)
def test_list_to_string_n2():
    string_utils = StringUtils()
    res = string_utils.list_to_string([" "])
    assert res == []
@pytest.mark.xfail(strict=True)
def test_list_to_string_n3():
    string_utils = StringUtils()
    res = string_utils.list_to_string(("123"))
    assert res == ("123")
@pytest.mark.xfail(strict=True)
def test_list_to_string_n4():
    string_utils = StringUtils()
    res = string_utils.list_to_string([None])
    assert res == (" ")