from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr

# problem 1 

class Book(BaseModel):
    title : str
    author : str
    year : int

book = Book(title="Atomic habits", author="James Clear", year=2018)

class Movie(BaseModel):
    name : str
    director : str
    duration_minutes : int

movie = Movie(name="1942", director="Ali", duration_minutes="120")

# problem 2

class User(BaseModel):
    name : str
    age : int 

user = User(name="Ali", age="35")

class Product(BaseModel):
    price : float

product = Product(price="199.00")

# problem 3

class ShoppingCart(BaseModel):
    items: list[str]

cart = ShoppingCart(items=["olma","anor","uzum"])

class Inventory(BaseModel):
    stock: dict[str, int]

inventory = Inventory(stock={
    "Iphone": 4,
    "Apple watch": 2,
    "Air Pods": 1
})

class UniqueTags(BaseModel):
    tags: set[str]

uniquetags = UniqueTags(tags={"badiiy","ilmiy","badiiy","roman","tarixiy","bestseller","roman","rivojlanish"})

# problem 4

class Person(BaseModel):
    name : str
    nickname : str | None = None

person = Person(name="Ali")

class Car(BaseModel):
    make : str
    model : str
    color : str = "black"

car = Car(make="BMW", model="M8")

# problem 5

class Customer(BaseModel):
    email : str

customer = Customer(email="Ali")

class Employee(BaseModel):
    email: str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    work_email: str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@gmail\.com$')

employee = Employee(email="ali@gmail.com", work_email="ali2@gmail.com")

# problem 6

class Product(BaseModel):
    price : int = Field(gt=0)

product = Product(price=1)

class User(BaseModel):
    username : str = Field(pattern=r'^[a-zA-Z0-9_]+$')

user = User(username="Ali")

class Review(BaseModel):
    rating : int = Field(ge=1, le=5)

rating = Review(rating=1)

# problem 7

class Profile(BaseModel):
    name : str
    bio : str | None = None
    age : int = Field(gt=18)

profile = Profile(name="Ali",age="25")

class Order(BaseModel):
    id : int
    status : str = "pending"
    total : int = Field(gt=0)

order = Order(id=1,total=1)

# problem 8

class Person(BaseModel):
    birth_year : int

    @field_validator("birth_year")
    @classmethod
    def yilni_tekshirish(cls, year: int):
        if year <= 1900:
            raise ValueError("Yil 1900 dan katta bo'lishi zarur")
        return year

odam = Person(birth_year=1901)

class Product(BaseModel):
    price : int

    @field_validator("price")
    @classmethod
    def narxni_tekshirish(cls, narx: int):
        if narx > 1000:
            raise ValueError("price 1000 dan katta bo'lmasligi kerak")
        return narx

product = Product(price=999)

# problem 9

from datetime import datetime

class Event(BaseModel):
    purpose : str
    theme : str
    start_date : datetime
    end_date : datetime

    @model_validator(mode='before')
    @classmethod
    def vaqtni_tekshirish(cls, data):
        if data.get("end_date") <= data.get("start_date"):
            raise ValueError("Vaqt noto'g'ri o'rnatilgan ")
        return data

event = Event(
    purpose="Bilim va ko'nikma berish",
    theme="Mustaqil o'rganish",
    start_date="2026-02-20 14:00:00",
    end_date="2026-02-20 17:00:00"
)

class Transaction(BaseModel):
    amount : int
    currency : str

    @model_validator(mode='after')
    def qiymatni_tekshirish(self):
        if self.amount < 0:
            raise ValueError("amount 0 dan kichik bo'lishi mumkin emas")
        return self

t = Transaction(amount=100, currency="USD")

# problem 10

class Address(BaseModel):
    street : str
    city : str
    zipcode : str

class User(BaseModel):
    name : str
    email : str
    address : Address


user = User(
    name="Ali",
    email="ali@gmail.com",
    address=Address(
        street="Navoiy ko'chasi",
        city="Farg'ona",
        zipcode="abc123"
    )
)


class Item(BaseModel):
    name : str
    price : float

class Order(BaseModel):
    user : User
    items : list[Item]

item = Item(name="book", price=6.00)
item2 = Item(name="phone", price=350.00)

order = Order(user=user, items=[item,item2])

# problem 11

# class User(BaseModel):
#     name : str
#     email : str = Field(pattern=r'^[a-zA-Z0-9._]+$')
#     password : 


