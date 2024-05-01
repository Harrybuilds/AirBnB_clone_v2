-- script that prepares a MySQL server for the project(AirBnB_clone_v2)

-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user hbnb_dev already exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'hbnb_dev' AND host = 'localhost';

-- create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant necessary privileges on this database only
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges to start the changes
FLUSH PRIVILEGES;
