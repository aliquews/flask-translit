import pandas as pd
from sqlalchemy import text
from src.db.database import engine



def migrate_db_xls():
    df = pd.read_sql_query(sql = text("SELECT * from translations"), con=engine.connect())
    writer = pd.ExcelWriter("src/files/data.xlsx")
    df.to_excel(writer, index=False)
    writer.save()