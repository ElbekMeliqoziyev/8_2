from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

class Student(BaseModel):
    ismi: str | None = Field(max_length=30, min_length=4)
    email: str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    yoshi: int = Field(ge=18)
    guruhi: str
    baholari: list[int]
    fan_baholari: dict[str, int]
    oqigan_fanlari: set[str]
    price : float
    discount: float

    @field_validator("ismi")
    @classmethod
    def ismi_should_startwith_uppercase(cls, ismi: str):
        if ismi:
            if not ismi[0].isupper():
                raise ValueError("Ismi kata harf bilan boshlanishi kerak")
        return ismi

    @model_validator(mode='after')
    def validate_price_and_discount(self):
        if self.discount > self.price:
            raise ValueError("Price diskountdan katta bolishi mmkin emas")
        return self
    
    @model_validator(mode='before')
    @classmethod
    def validate_ismi(cls, data):
        if 'name' in data:
            data['ismi'] = data['name']
        return data
    
    
student = Student(
    name="Aliy",
    email='example123@gmail.com',
    yoshi="18", 
    guruhi='fn35', 
    baholari=[4,5,4],
    fan_baholari={
        "fizika": 4,
        "ona tili": 5
    },
    oqigan_fanlari={'matem', 'fizika', 'kimyo', 'fizika'},
    price=12,
    discount=12
)
print(student)
