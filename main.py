from fastapi import FastAPI
from pydantic import BaseModel
import random


class Fact(BaseModel):
    id: int
    fact: str


app = FastAPI()

facts_db = [
    Fact(id=0, fact="The Great Wall of China is not visible from space."),
    Fact(id=1, fact="A group of flamingos is called a 'flamboyance'."),
    Fact(id=2, fact="Bananas are berries, but strawberries are not.")
]

@app.get("/")
async def get_all():
    return facts_db


@app.get("/fact/random")
async def get_random_fact():
    return random.choice(facts_db)


@app.get("/fact/{fact_id}")
async def get_fact_by_id(fact_id: int):
    for fact in facts_db:
        if fact.id == fact_id:
            return fact


@app.post("/fact/add")
async def add_fact(fact: Fact):
    new_fact = Fact(id=len(facts_db), fact=fact.fact)
    facts_db.append(new_fact)
    return new_fact