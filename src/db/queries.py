

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
    
    def get_username(self, username):
        return f"SELECT count(*) FROM users WHERE username = {username};"
    
    def check_password(self, username, hashed_pass):
        return f"SELECT password FROM users WHERE username = {username};"
    
    def create_new_user(self, username, hashed_pass):
        return f"INSERT INTO users (username, password) VALUES ({username}, {hashed_pass});"