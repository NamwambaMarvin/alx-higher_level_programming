-- Creates a user user_0d_1 and grants all privilages
-- Gives a password user_0d_1_pwd
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
