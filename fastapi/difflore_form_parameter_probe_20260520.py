def require_form_parameter_alias(alias: str) -> str:
    normalized = alias.strip()
    if not normalized:
        raise ValueError("form param alias must not be empty")
    return normalized
