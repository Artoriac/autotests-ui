import pytest

SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(SYSTEM_VERSION == 'v1.3.0', reason='Тест не может запущен на версии системы v1.3.0')
def test_system_version_valid():
    ...
@pytest.mark.skipif(SYSTEM_VERSION == 'v1.2.0', reason='Тест не может запущен на версии системы v1.2.0')
def test_sysytem_version_invalid():
    ...

