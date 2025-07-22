import  pytest

@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест не проходит")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Баг уже исправлено, но до сих пор на тесте висит xfail")
def test_without_bug():
    ...