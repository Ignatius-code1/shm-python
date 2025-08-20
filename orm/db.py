import psycopg
from psycopg_pool import ConnectionPool

class PG:

    def __init__(self):

        self.credentials={
            "host":"aws-1-ap-southeast-1.pooler.supabase.com",
            "dbname":"postgres",
            "user":"postgres.hligqmxuekndtvcxuxrr",
            "password":"AfQxlUVjojzIjh5g",
            "port":5432
        }

        # setting like min_size,max_size,timeout 
        #Optional
        self.pool=ConnectionPool(
            conninfo=self.credentials,
            min_size=1,
            max_size=5,
            timeout=300,
            open=True
        )