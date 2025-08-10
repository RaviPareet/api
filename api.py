from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

@app.get("/add")
def add(a:int, b:int):
    return a + b

class validate(BaseModel):
    a: int
    b: int

def addition(a:int, b:int):
    return a+b

@app.post("/addtion")
def add_number(model: validate):
    return addition(model.a, model.b)

def substract(a:int, b:int):
    return a-b

@app.post("/substract")
def substract_number(model:validate):
    return substract(model.a, model.b)

def multiplication(a:int, b:int):
    return a*b

@app.post("/multiplication")
def multiply_number(model:validate):
    return multiplication(model.a, model.b)

def division(a:int,b:int) -> float:
    try:
        return a/b
    except ZeroDivisionError as err:
        raise ValueError("Cann't divide by zero. Ensure that denominator is not zero.") from None

@app.post("/division")
def devision_number(model: validate):
    return division(model.a, model.b)




class CalculationRequest(BaseModel):
    operation: Literal['add', 'sub', 'mult','div']
    a: float
    b: float


@app.post('/calculator')
def calculate(req: CalculationRequest):
    if req.operation == 'add':
        result = req.a + req.b
    elif req.operation == 'sub':
        result = req.a - req.b
    elif req.operation == 'mult':
        result = req.a * req.b
    elif req.operation == 'div':
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        result = req.a / req.b
    else:
        raise HTTPException(status_code=400, detail='Invalid Operation')
    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1'", port=8000, reload=True)