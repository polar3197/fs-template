from fastapi import FastAPI, HTTPException
from db.client import PostgreSQLClient
from config import PostgreSQLConfig
from pydantic import BaseModel
from typing import List, Dict, Any

pgcli = PostgreSQLClient(PostgreSQLConfig())
app = FastAPI(title="Template", version="1.0.0")

class TableResponse(BaseModel):
    table: str
    rows: List[Dict[str, Any]]

@app.get("/")
async def health():
    return {"status": "Healthy"}

@app.get("/dbtables/{table_name}", response_model=TableResponse)
async def return_db_table_names(table_name: str):
    try:
        rows = await pgcli.get_table_contents(table_name)
        formatted_rows = [dict(row._mapping) for row in rows]
        return {"table": table_name, "rows": formatted_rows}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found or error: {str(e)}")