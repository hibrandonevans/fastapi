def require_body_parameter_default(default: object | None) -> object:
    if default is None:
        raise ValueError("body parameter default must be explicit")
    return default
