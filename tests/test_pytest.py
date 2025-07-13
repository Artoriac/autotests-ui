def test_user_login():
    print('We are happy!')

class TestUserLogin:
    def test_1(self):
        assert True

    def test_2(self):
        ...

def test_assert_possitive_case():
    assert (2 + 2) == 4
    assert (3 + 3) == 6
    assert (4 + 4) == 8

def test_assert_negative_case():
    four = 2 + 2
    assert four == 5, 'Неверное значение, 2 + 2 не равно 5'