CREATE DATABASE recipes_db;

CREATE USER recipes_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE recipes_db TO recipes_admin;

