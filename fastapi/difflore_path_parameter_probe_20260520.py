def require_path_parameter_name(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise ValueError("path param name must not be empty")
    return normalized
