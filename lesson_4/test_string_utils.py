import pytest
from string_utils import StringUtils


@pytest.mark.positive_test
@pytest.mark.parametrize('string, new_string', [('word', 'Word'), ('WORD', 'WORD'), ('123', '123'), ('w', 'W'),
                                                ('text text', 'Text text')])
def test_capitilize_pos(string, new_string):
    assert StringUtils().capitilize(string) == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize('string, new_string', [(122, ''), ('', ''), (' ', ' '), (True, '')])
def test_capitilize_neg(string, new_string):
    if type(string) == str:
        assert StringUtils().capitilize(string) == new_string
    else:
        with pytest.raises(AttributeError):
            StringUtils().capitilize(string)
        print(f'{string} is not a string')


@pytest.mark.positive_test
@pytest.mark.parametrize('string, new_string', [('   word', 'word'), ('WORD  ', 'WORD  '), ('  123', '123'), ('  ', ''),
                                                ('  w', 'w'), ('   text text', 'text text'), (' word   ', 'word   ')])
def test_trim_pos(string, new_string):
    assert StringUtils().trim(string) == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize('string, new_string', [(122, ''), ('', ''), (True, '')])
def test_trim_neg(string, new_string):
    if type(string) == str:
        assert StringUtils().trim(string) == new_string
    else:
        with pytest.raises(AttributeError):
            StringUtils().trim(string)
        print(f'{string} is not a string')


@pytest.mark.positive_test
@pytest.mark.parametrize('string, new_string, delimiter', [("1:2:3", ["1", "2", "3"], ':'),
                                                           ("a b c d", ["a", "b", "c", "d"], " ")])
def test_to_list_pos(string, new_string, delimiter):
    assert StringUtils().to_list(string, delimiter) == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize('string, new_string', [("1,2,3", ["1", "2", "3"]), (123, '')])
def test_to_list_neg(string, new_string):
    if type(string) == str:
        assert StringUtils().to_list(string) == new_string
    else:
        with pytest.raises(AttributeError):
            StringUtils().to_list(string)
        print(f'{string} is not a string')


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol', [('word', 'w'), ('Word', 'W'), ('123', '2'), (' text', ' '), ('', ''),
                                            ('just text', 'x')])
def test_contains_pos(string, symbol):
    assert StringUtils().contains(string, symbol) is True


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol', [(123, '2'), ('123', 2), ('word', 'W'), ('Word', 'w')])
def test_contains_neg(string, symbol):

    if type(string) != str:
        with pytest.raises(AttributeError):
            StringUtils().contains(string, symbol)
        print(f'{string} is not a string')
    elif type(symbol) != str:
        with pytest.raises(TypeError):
            StringUtils().contains(string, symbol)
        print(f'{symbol} is not a string')
    else:
        assert StringUtils().contains(string, symbol) is False


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, new_string', [('word', 'w', 'ord'), ('WORD', 'W', 'ORD'),
                                                        ('word123', '123', 'word'), (' word ', ' ', 'word'),
                                                        (' ', ' ', '')])
def test_delete_symbol_pos(string, symbol, new_string):
    assert StringUtils().delete_symbol(string, symbol) == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, new_string', [('word', 'W', 'word'), ('WORD', 'w', 'WORD'),
                                                        ('word', '', 'word'), ('123', 123, '123'), (456, '123', 456)])
def test_delete_symbol_neg(string, symbol, new_string):
    if type(string) != str:
        with pytest.raises(AttributeError):
            StringUtils().delete_symbol(string, symbol)
        print(f'{string} is not a string')
    elif type(symbol) != str:
        with pytest.raises(TypeError):
            StringUtils().delete_symbol(string, symbol)
        print(f'{symbol} is not a string')
    else:
        assert StringUtils().delete_symbol(string, symbol) == new_string


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [('word', 'w', True), ('WORD', 'W', True), ('123', '1', True),
                                                    (' word', ' ', True), ('word', 'r', False), ('WORD', 'w', False),
                                                    ('word', '', True)])
def test_starts_with_pos(string, symbol, result):
    assert StringUtils().starts_with(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [('123', 1, False), (123, 1, False), (123, '1', False)])
def test_starts_with_neg(string, symbol, result):
    if type(string) != str:
        with pytest.raises(AttributeError):
            StringUtils().starts_with(string, symbol)
        print(f'{string} is not a string')
    elif type(symbol) != str:
        with pytest.raises(TypeError):
            StringUtils().starts_with(string, symbol)
        print(f'{symbol} is not a string')
    else:
        assert StringUtils().starts_with(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [('word', 'd', True), ('WORD', 'D', True), ('123', '3', True),
                                                    ('word', '', True), ('word', 's', False), ('WORD', 'd', False),
                                                    ('word', ' ', False), ('word', 'D', False), ('w ', ' ', True)])
def test_end_with_pos(string, symbol, result):
    assert StringUtils().end_with(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [(123, '3', False), ('123', 3, False), (123, 3, False)])
def test_end_with_neg(string, symbol, result):
    if type(string) != str:
        with pytest.raises(AttributeError):
            StringUtils().end_with(string, symbol)
        print(f'{string} is not a string')
    elif type(symbol) != str:
        with pytest.raises(TypeError):
            StringUtils().end_with(string, symbol)
        print(f'{symbol} is not a string')
    else:
        assert StringUtils().end_with(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [('w', False), ('W', False), ('123', False), ('   ', False), ('', True)])
def test_is_empty_pos(string, result):
    assert StringUtils().is_empty(string) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [(123, False)])
def test_is_empty_neg(string, result):
    if type(string) != str:
        with pytest.raises(AttributeError):
            StringUtils().is_empty(string)
        print(f'{string} is not a string')
    else:
        assert StringUtils().is_empty(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('lst, join, string', [([1, 2, 3], ', ', '1, 2, 3'), (['a', 'b', 'c'], '-', 'a-b-c'),
                                               ([1, 2, 3], ' ', '1 2 3'),  ([1, 2, 3], '', '123')])
def test_list_to_string_pos(lst, join, string):
    assert StringUtils().list_to_string(lst, join) == string


@pytest.mark.negative_test
@pytest.mark.parametrize('lst, join, string', [('1, 2, 3', ' ', '1 2 3')])
def test_list_to_string_neg(lst, join, string):
    assert StringUtils().list_to_string(lst, join) == string
