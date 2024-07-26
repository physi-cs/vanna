from vanna.openai import OpenAI_Chat
from openai import OpenAI
from vanna.pgvector import PG_VectorStore

# TODO 与pg_vector中的环境变量统一
client = OpenAI(
    api_key="sk-fastgpt",
    base_url="http://20.3.245.57:3001/v1/"
)

config = {"connection_string": "postgresql+psycopg2://username:password@121.199.37.52:5432/postgres",
          "model": "qwen"}

class MyVanna(PG_VectorStore, OpenAI_Chat):
    def __init__(self,client=None,config=None):
        OpenAI_Chat.__init__(self,client=client,config=config)
        PG_VectorStore.__init__(self,config=config)
        
    def generate_query_explanation(self, sql: str):
        my_prompt = [
            self.system_message("You are a helpful assistant that will explain a SQL query"),
            self.user_message("Explain this SQL query: " + sql),
        ]

        return self.submit_prompt(prompt=my_prompt)

vn = MyVanna(client=client,config=config) 
vn.connect_to_postgres(host='121.199.37.52', dbname='postgres', user='username', password='password', port=5432)
vn.max_tokens = 800
vn.temperature = 0.5

from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run()


