# from core.application.user.services import UserService
# from core.application.user.dtos import RegisterUserDTO

def register_user(service: UserService, email: str):
    dto = RegisterUserDTO(email=email)
    return service.register(dto)
