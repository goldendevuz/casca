from dataclasses import dataclass

@dataclass(slots=True)
class RegisterUserDTO:
    email: str
