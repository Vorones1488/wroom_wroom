from pydantic import BaseModel, Field, EmailStr


class RegistrationForm_In(BaseModel):
    user_name: str = Field(..., title='Имя пользователя', max_lenght= 10)
    email: EmailStr = Field(..., title="проверка почты")
    password: str
    confirm_password: str


