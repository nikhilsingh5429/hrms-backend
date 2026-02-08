from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = []

@app.get("/api/employees")
def get_employees():
    return employees

@app.post("/api/employees")
def add_employee(emp: dict):
    emp["id"] = len(employees) + 1
    employees.append(emp)
    return emp
