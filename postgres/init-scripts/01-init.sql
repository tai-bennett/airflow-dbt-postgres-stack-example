-- ---------- Create Roles/Users ----------
CREATE USER myuser WITH PASSWORD 'mypassword';

-- ----------- Create Database ------------
CREATE DATABASE mydb;

-- ---------- Grant permissions -----------
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

