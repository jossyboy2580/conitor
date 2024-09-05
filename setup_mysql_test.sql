-- prepare a mysql server for the project

CREATE DATABASE IF NOT EXISTS conitor_test_db;
CREATE USER IF NOT EXISTS 'conitor_test'@'localhost' IDENTIFIED BY 'conitor_test_pwd';
GRANT ALL PRIVILEGES ON `conitor_test_db`.* TO 'conitor_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'conitor_test'@'localhost';
FLUSH PRIVILEGES;
