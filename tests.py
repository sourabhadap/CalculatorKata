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
