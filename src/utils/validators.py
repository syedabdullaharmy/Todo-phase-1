"""Input validation utilities."""

from typing import Optional

def validate_non_empty(value: str, field_name: str) -> str:
    """
    Ensures a string is not empty or just whitespace.
    
    Args:
        value: The user input.
        field_name: Name of field for error message.
        
    Returns:
        The stripped string.
        
    Raises:
        ValueError: If value is empty.
    """
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")
    return cleaned

def parse_int(value: str) -> int:
    """
    Parses a string to an integer.
    
    Raises:
        ValueError: If value is not a valid integer.
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid number.")
