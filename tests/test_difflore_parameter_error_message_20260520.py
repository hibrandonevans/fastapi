import pytest

from fastapi.difflore_parameter_probe import validate_difflore_parameter_name


def test_difflore_parameter_error_uses_complete_word() -> None:
    with pytest.raises(ValueError, match="param name"):
        validate_difflore_parameter_name("")
