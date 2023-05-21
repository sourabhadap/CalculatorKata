from main import add


def test_add_empty_string():
    assert add("") == 0


def test_add_single_number():
    assert add("6") == 6


def test_add_two_number_separated_by_commas():
    assert add("10,2") == 12


def test_add_unknown_amount_of_numbers_separated_by_commas():
    assert add("1,2,3,4,5") == 15


def test_add_new_line_delimiter():
    assert add("1\n2,3") == 6


def test_negative_numbers_without_delimiter():
    try:
        add("-1,2,-3")
    except Exception as e:
        assert str(e) == "Negatives not allowed: [-1, -3]"


def test_negative_numbers_with_delimiter():
    try:
        add("//;\n-1;2;-3")
    except Exception as e:
        assert str(e) == "Negatives not allowed: [-1, -3]"


def test_add_custom_delimiter():
    assert add("//;\n1;2;4;5;7") == 19


def test_add_bigger_numbers_without_delimiter():
    assert add("2,1001,6") == 8


def test_add_bigger_numbers_with_delimiter():
    assert add("//;\n2;1001;6") == 8
