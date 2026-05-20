def require_header_parameter_alias(alias: str) -> str:
    normalized = alias.strip()
    if not normalized:
        raise ValueError("header param alias must not be empty")
    return normalized
