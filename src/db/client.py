from db.queries import PostgreSQLQueries
from config import PostgreSQLConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine # for sync pandas ops
from sqlalchemy import text
from functools import cached_property


class PostgreSQLClient():

    # In database/client.py __init__
    def __init__(self, config: PostgreSQLConfig, retry_count: int = 3):
        self.config = config
        self.connection_string = config.connection_string  # Use pre-built string
        self.retry_count = retry_count
        self.queries = PostgreSQLQueries()
        # Don't need individual host, user, etc.

    @cached_property
    def engine(self):
        """
        Starts async engine to connect to db

        Args:

        Returns:
            - A sqlalchemy engine
        """
        return create_async_engine(self.connection_string)

    async def get_result(self, query: str):
        """
        Merges engine and query to return result

        Args:
            - postgres query

        Returns:
            - result object from query
        """
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(text(query))
                return result
        except Exception as e:
            #LOG HERE
            print(f"Running query '{query}' failed -- {e}")

    async def ping(self):
        """
        Tests connection to db

        Args:

        Returns:
            - True or False
        """
        try:
            result = await self.get_result(self.queries.ping())
            row = result.fetchone()
            return row[0] == 2
        except Exception as e:
            print(f"exception: {e}")
            return False
        
    async def get_table_contents(self, table_name):
        """
        Tests connection to db

        Args:

        Returns:
            - True or False
        """
        try:
            result = await self.get_result(self.queries.get_table_contents(table_name))
            print(result)
            rows = result.fetchall()
            return rows
        except Exception as e:
            print(f"exception: {e}")
            return False