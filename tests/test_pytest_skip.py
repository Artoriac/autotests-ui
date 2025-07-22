import  pytest

@pytest.mark.skip(reason="Feature is in development")
def test_feature_in_development():
    ...
@pytest.mark.skip(reason="Feature is in development")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...