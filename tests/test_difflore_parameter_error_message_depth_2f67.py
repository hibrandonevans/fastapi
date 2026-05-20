import pytest

from fastapi.difflore_parameter_probe_depth_2f67 import validate_depth_parameter_name


def test_depth_parameter_error_message_uses_full_word() -> None:
    with pytest.raises(ValueError, match="param name"):
        validate_depth_parameter_name("")
