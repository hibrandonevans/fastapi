import pytest

from fastapi.difflore_cookie_parameter_probe_20260520 import (
    require_cookie_parameter_name,
)
from fastapi.difflore_body_parameter_probe_20260520 import (
    require_body_parameter_default,
)
from fastapi.difflore_form_parameter_probe_20260520 import (
    require_form_parameter_alias,
)
from fastapi.difflore_header_parameter_probe_20260520 import (
    require_header_parameter_alias,
)
from fastapi.difflore_path_parameter_probe_20260520 import (
    require_path_parameter_name,
)
from fastapi.difflore_query_parameter_probe_20260520 import (
    require_query_parameter_name,
)


def test_query_parameter_name_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="query parameter name"):
        require_query_parameter_name(" ")


def test_header_parameter_alias_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="header parameter alias"):
        require_header_parameter_alias(" ")


def test_cookie_parameter_name_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="cookie parameter name"):
        require_cookie_parameter_name(" ")


def test_path_parameter_name_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="path parameter name"):
        require_path_parameter_name(" ")


def test_form_parameter_alias_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="form parameter alias"):
        require_form_parameter_alias(" ")


def test_body_parameter_default_error_mentions_parameter() -> None:
    with pytest.raises(ValueError, match="body parameter default"):
        require_body_parameter_default(None)
