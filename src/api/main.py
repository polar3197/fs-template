from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from db.client import PostgreSQLClient
from config import PostgreSQLConfig
from typing import Annotated
from pydantic import BaseModel
from typing import List, Dict, Any

pgcli = PostgreSQLClient(PostgreSQLConfig())
app = FastAPI(title="Template", version="1.0.0")

class TableResponse(BaseModel):
    table: str
    rows: List[Dict[str, Any]]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def health():
    return {"status": "Healthy"}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get("/dbtables/{table_name}", response_model=TableResponse)
async def return_db_table_contents(table_name: str):
    try:
        rows = await pgcli.get_table_contents(table_name)
        formatted_rows = [dict(row._mapping) for row in rows]
        return {"table": table_name, "rows": formatted_rows}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found or error: {str(e)}")
    
@app.put("/register")
async def register_new_user(username: str, password: str):
    try:
        results = await pgcli.get_username()
        valid_username = username.fetchone()
        if not valid_username:
            raise HTTPException(status_code=400, detail=f"Username already exists")
        return valid_username
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error in register: {str(e)}")
    
@app.put("/login")
async def register_new_user(username: str, password: str):
    try:
        results = await pgcli.get_username()
        valid_username = username.fetchone()
        return valid_username
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found or error: {str(e)}")