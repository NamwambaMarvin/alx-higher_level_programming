-- Changes the character set of the database
-- utf8 to some thing else

USE htbn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4_unicode_ci;
