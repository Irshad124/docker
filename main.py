import psycopg2 as pg
import json
from fastapi import FastAPI

app= FastAPI()
@app.get("/emp/{emp_id}")
def read_item(emp_id: int):
    conn = pg.connect(database="postgres", user="mt24020", host="w3.training5.modak.com", password="mt24020@m04y24", port=5432)
    cur = conn.cursor()
    cur.execute(f'select * from emp_det where emp_id={emp_id}')
    rec = cur.fetchone()
    print(type(rec))
    if rec is None:
        return f"No Employee found with id {emp_id}"
    rec1 = {"emp_id": rec[0],"emp_name": rec[1],"dob": rec[2],"mobile_number": rec[3]
    }
    print(rec)
    rec_json=json.dumps(rec1)
    cur.close()
    return rec1

@app.get("/emp")
def read_item(emp_id: int):
    conn = pg.connect(database="postgres", user="mt24020", host="w3.training5.modak.com", password="mt24020@m04y24", port=5432)
    cur = conn.cursor()
    cur.execute(f'select * from emp_det where emp_id={emp_id}')
    rec = cur.fetchone()
    print(type(rec))
    if rec is None:
        return f"No Employee found with id {emp_id}"
    rec1 = {"emp_id": rec[0],"emp_name": rec[1],"dob": rec[2],"mobile_number": rec[3]
    }
    print(rec)
    rec_json=json.dumps(rec1)
    conn.close()
    return rec1
@app.get("/")
def read_root():
    return {"Message":"Employee Management System"}
