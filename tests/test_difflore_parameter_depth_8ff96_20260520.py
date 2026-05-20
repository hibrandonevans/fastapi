import pytest

from fastapi.difflore_cookie_parameter_probe_20260520 import (
    require_cookie_parameter_name,
)
from fastapi.difflore_header_parameter_probe_20260520 import (
    require_header_parameter_alias,
)
from fastapi.difflore_query_parameter_probe_20260520 import (
    require_query_parameter_name,
)


def test_query_parameter_name_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="query param name"):
        require_query_parameter_name(" ")


def test_header_parameter_alias_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="header param alias"):
        require_header_parameter_alias(" ")


def test_cookie_parameter_name_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="cookie param name"):
        require_cookie_parameter_name(" ")
