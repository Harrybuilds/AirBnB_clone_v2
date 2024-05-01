-- script that prepares a MySQL server for the project(AirBnB_v2: hbnb_test)

-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant the required permissions to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privileges on performance.schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush privilege to start changes
FLUSH PRIVILEGES;
