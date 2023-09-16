# tickethub-server
Tickethub app backend

## Backend requirements/tools

1. First you need to have the python3 installed on your machine
2. For the database you need to have the postgres database
3. Install flask, sqlalchemy, psyco2, dotenv, alembic
4. Generate a new migration: alembic revision --autogenerate -m "Migration name"
5. Run migrations: alembic upgrade head
