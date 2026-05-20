def require_cookie_parameter_name(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise ValueError("cookie param name must not be empty")
    return normalized
