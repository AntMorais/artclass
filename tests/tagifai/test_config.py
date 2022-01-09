# tests/artclass/test_config.py
# Test artclass/config.py components.

from config import config


def test_config():
    assert config.logger.name == "root"
