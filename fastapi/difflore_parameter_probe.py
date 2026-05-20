def validate_difflore_parameter_name(name: str) -> None:
    if not name:
        raise ValueError("param name must not be empty")
