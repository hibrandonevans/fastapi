def require_query_parameter_name(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise ValueError("query parameter name must not be empty")
    return normalized
