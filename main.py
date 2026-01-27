from pydantic import BaseModel, Field, field_validator

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

odam = Person(birth_year=1889)

class Product(BaseModel):
    price : int

    @field_validator("price")
    @classmethod
    def narxni_tekshirish(cls, narx: int):
        if narx > 1000:
            raise ValueError("price 1000 dan katta bo'lmasligi kerak")
        return narx




