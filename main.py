from enum import Enum

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"Message": "Hello world"}


@app.get("/hello/john")
async def hello():
    return {"message": "I am extra-ordinary"}


@app.get("/hello/{item_id}")
async def hello(item_id: str | int):
    return {"Item-id": item_id}


@app.get("/user/me")
async def hello():
    return {"message": "I am groot"}


@app.get("/morn/we")
async def hello():
    return {"message": "We are groot."}


@app.post("/")
async def post():
    return {"Message": "Hello, I am from post request"}


@app.put("/")
async def put():
    return {"Message": "Hello, I am from put request"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/fruits/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You are healthy"}
    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "You are still healthy, keep eating fruits"
        }
    return {"food_name": food_name, "message": "I like the chocolate milk"}

fake_items_db = [{"items_name", "Foo"}, {
    "items_name", "Bar"}, {"items_name", "BAz"},
    {"items_name", "Fourz"}, {"items_name", "Fivez"},
    {"items_name", "Sixz"}, {"items_name", "Sevenz"},
    {"items_name", "Eightz"}, {"items_name", "Ninez"},
]


@ app.get("/items")
async def list_items(skip: int = 0, limit: int = 5):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def list_items(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
