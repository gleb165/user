# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine

#This line ensures that the models are imported and available for Alembic to work with
from app.api.db_model import metadata, users
# Replace 'your_module' with your actual module

#Use the your_module.metadata instead of Base.metadata
target_metadata = metadata

# Specify the database URL from the alembic.ini file
config = context.config
config.set_main_option('sqlalchemy.url', str(metadata.bind.url))

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Setup async engine
config_section = config.config_ini_section
async_engine = AsyncEngine(create_engine(config.get_section_option(config_section, "sqlalchemy.url"), poolclass=pool.NullPool))

# Attach the async engine to the metadata, which allows Alembic to interact with the database
with async_engine.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True  # Enable type comparison for PostgreSQL
    )

    # Run the migrations
    with context.begin_transaction():
        context.run_migrations()