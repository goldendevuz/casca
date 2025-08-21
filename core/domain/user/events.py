from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class UserRegistered:
    user_id: int
    email: str
