from typing import Dict

def multiply_numbers(data: Dict) -> Dict:
    """
    Multiplies two numbers. Input schema:
    {
        "a": int,
        "b": int
    }
    """
    a = data.get('a')
    b = data.get('b')
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both 'a' and 'b' must be integers.")
    return {"result": a * b}

def get_user_input(data: Dict) -> Dict:
    """
    Mock function to simulate user input. Input schema:
    {
        "message": str
    }
    """
    message = data.get("message", "Default message")
    print(f"Asking user for input: {message}")
    return {"response": "test user input"}
