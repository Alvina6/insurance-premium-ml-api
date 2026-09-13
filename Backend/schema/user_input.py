from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities,tier_2_cities

class UserInput(BaseModel):

    age: Annotated[
        int,
        Field(..., gt=0, lt=100, description="Age of the user in years")
    ]

    weight: Annotated[
        float,
        Field(..., gt=0, lt=300, description="Weight of the user in kg")
    ]

    height: Annotated[
        float,
        Field(..., gt=0, lt=2.5, description="Height of the user in meters")
    ]

    income_lpa: Annotated[
        float,
        Field(..., gt=0, description="Annual salary of the user in LPA")
    ]

    smoker: Annotated[
        bool,
        Field(..., description="Whether the user is a smoker")
    ]

    city: Annotated[
        str,
        Field(..., description="The city where the user lives")
    ]

    occupation: Annotated[
        Literal[
            'Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
            'Marketing Manager', 'Insurance Agent', 'HR Manager',
            'Pharmacist', 'Teacher', 'Software Engineer', 'Consultant',
            'Driver', 'Shop Owner', 'Nurse', 'Accountant',
            'Government Employee', 'Architect', 'Engineer',
            'Real Estate Agent', 'Civil Servant', 'Plumber',
            'Retail Manager', 'Chef', 'Electrician', 'Carpenter',
            'Doctor', 'Lab Technician', 'Data Analyst', 'Lawyer',
            'Content Writer'
        ],
        Field(..., description="The occupation of the user")
    ]

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v:str)-> str:
        v= v.strip().title()
        return v

    @computed_field
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    def lifestyle_risk(self) -> str:
        if self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    def age_group(self) -> str:

        if self.age < 25:
            return "young"

        elif self.age < 45:
            return "adult"

        elif self.age < 60:
            return "middle_aged"

        else:
            return "senior"

    @computed_field
    def city_tier(self) -> int:

        if self.city in tier_1_cities:
            return 1

        elif self.city in tier_2_cities:
            return 2

        else:
            return 3

