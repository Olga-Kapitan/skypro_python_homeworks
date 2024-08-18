import pytest
from string_utils import StringUtils

utils = StringUtils()

print('start')


@pytest.mark.parametrize('string, result', [
    ('skypro', 'Skypro'),
    ('i love you', 'I love you'),
    ('123456', '123456'),
    ('привет2024год', 'Привет2024год')
    ])
def test_capitilize_positive(string, result):
    utils = StringUtils()
    res = utils.capitilize(string)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [
    (123456, '123456'),
    ('', ''),
    ('  ', ''),
    ('@#$', '@#$')
    ])
def test_capitilize_negative(string, result):
    utils = StringUtils()
    res = utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ('   skypro', 'skypro'),
    ('   Hi, teacher!', 'Hi, teacher!'),
    ('  778899', '778899'),
    ('hello', 'hello')
    ])
def test_trim_positive(string, result):
    utils = StringUtils()
    res = utils.trim(string)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [
    (778899, '778899'),
    ('  Hello  ', 'Hello'),
    ('', '')
    ])
def test_trim_negative(string, result):
    utils = StringUtils()
    res = utils.trim(string)
    assert res == result


# условный парамерт delimeter не срабатывает
@pytest.mark.defect_utils
@pytest.mark.parametrize('string, delimeter, result', [
    ("a,b,c,d", ',', ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ('алгебра,история,литература', ',', ['алгебра', 'история', 'литература']),
    ('@/#/&', '/', ['@', '#', '&']),
    ('num 1,num 2', ',', ['num 1', 'num 2'])
    ])
def test_to_list_positive(string, delimeter, result):
    utils = StringUtils()
    res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.defect_utils
@pytest.mark.xfail
@pytest.mark.parametrize('string, delimeter, result', [
    ('', '-', []),
    ('', None, []),
    (None, '-', []),
    ('h,e,l,l,o', None, ['h', 'e', 'l', 'l', 'o']),
    ('1,2,3', ':', ['1', '2', '3'])
    ])
def test_to_list_negative(string, delimeter, result):
    utils = StringUtils()
    res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("Привет", "и", True),
    ("Привет и пока", "и", True),
    ("test@mail.ru", "@", True),
    ("123", "3", True),
    ("@#$$%", "G", False)
    ])
def test_contains_positive(string, symbol, result):
    utils = StringUtils()
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.defect_utils
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    (" ", "o", False),
    ("", "", True),
    ("Hello", " ", False),
    ("Hello", None, False),
    (None, '', False)
    ])
def test_contains_negative(string, symbol, result):
    utils = StringUtils()
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ('Здравствуйте', 'З', 'дравствуйте'),
    ('Привет, мир!', 'и', 'Првет, мр!'),
    ('Кото-пес', '-', 'Котопес'),
    ('Маши@на', '@', 'Машина'),
    ('789', '9', '78')
    ])
def test_delete_symbol_positive(string, symbol, result):
    utils = StringUtils()
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.defect_utils
@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", None, "SkyPro"),
    ('', '', ''),
    ('Солнце', '', 'Солнце'),
    ('', None, ''),
    ('  ', 'l', '')
    ])
def test_delete_symbol_negative(string, symbol, result):
    utils = StringUtils()
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("Sky Pro", "S", True),
    ('Привет', 'П', True),
    ('789', 'G', False),
    ('123456', '1', True)
    ])
def test_starts_with_positive(string, symbol, result):
    utils = StringUtils()
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    (123456, 5, True),
    ('hello', '', False),
    (None, 'X', False),
    ('', None, False)
    ])
def test_starts_with_negative(string, symbol, result):
    utils = StringUtils()
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("Sky Pro", "o", True),
    ('Привет', 'т', True),
    ('789', 'к', False),
    ('123456', '6', True)
    ])
def test_end_with_positive(string, symbol, result):
    utils = StringUtils()
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    (123456, 6, True),
    ('hello', '', False),
    (None, 'X', False),
    ('', None, False)
    ])
def test_end_with_negative(string, symbol, result):
    utils = StringUtils()
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("SkyPro", False),
    ('123456', False),
    ('@#$&', False),
    ('--', False),
    ('  Привет', False),
    # (None, False)
    ])
def test_is_empty(string, result):
    utils = StringUtils()
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.defect_utils
@pytest.mark.parametrize('lst, joiner, result', [
    ([1, 2, 3, 4], ', ', "1, 2, 3, 4"),
    (["Sky", "Pro"], ', ', "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (['!', '@', '#'], '/', '!/@/#')
    ])
def test_list_to_string_positive(lst, joiner, result):
    utils = StringUtils()
    res = utils.list_to_string(lst, joiner)
    assert res == result


@pytest.mark.xfail
@pytest.mark.defect_utils
@pytest.mark.parametrize('lst, joiner, result', [
    ([], None, ''),
    ([], '1', ''),
    ([1, 2, 3, 4], '', "1234")
    ])
def test_list_to_string_negative(lst, joiner, result):
    utils = StringUtils()
    res = utils.list_to_string(lst, joiner)
    assert res == result


print('finish')
