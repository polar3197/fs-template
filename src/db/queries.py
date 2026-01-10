

class PostgreSQLQueries():
    """
    Defines commonly used queries and returns them as strings
    """

    def ping(self):
        return "SELECT 1+1"
    
    def get_tables_list(self):
        return f"SELECT table_name FROM information_schema.tables;"

    def get_table_contents(self, table_name):
        return f"SELECT * FROM {table_name};"