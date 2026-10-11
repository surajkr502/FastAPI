from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Teacher(BaseModel):
    name: Annotated[str, Field(
        max_length=50,
        title='Name of the teacher',
        description='Give the name of the teacher in less than 50 chars',
        examples=['Nitish', 'Amit']
    )]

    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[Optional[bool], Field(
        default=None,
        description='Is the teacher married or not'
    )]
    allergies: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=5)
    ]

    contact_details: Dict[str, str]


def update_teacher_data(teacher: Teacher):
    print(teacher.name)
    print(teacher.age)
    print(teacher.allergies)
    print(teacher.married)
    print('updated')