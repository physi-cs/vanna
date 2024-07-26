from langchain.vectorstores.pgvector import PGVector

CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver="psycopg2",
    host="121.199.37.52",
    port="5432",
    database="postgres",
    user="username",
    password="password",
)

print(CONNECTION_STRING)