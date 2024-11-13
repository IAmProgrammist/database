from tabulate import tabulate
from os import getenv
import psycopg2

def main():
    connection = psycopg2.connect(database=getenv("DATABASE"),
                                  user=getenv("USERNAME"),
                                  password=getenv("PASSWORD"),
                                  host=getenv("HOST"),
                                  port=int(getenv("PORT")),
                                  options=f"-c search_path={getenv('SCHEMA')}"
                                  )

    cur = connection.cursor()
    cur.execute("SELECT * FROM contract")
    print(cur.fetchall())


if __name__ == "__main__":
    main()
