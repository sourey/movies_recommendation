import pandas as pd
md=pd.read_csv("final_movies.csv")
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:sujan@localhost:5432/postgres')
md.to_sql("movies", engine)
