-- Creates the database hbtn_0d_2 and the user user_0d_2
-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd
DB_NAME="hbtn_0d_2"
DB_USER="user_0d_2"
DB_PASSWORD="user_0d_2_pwd"

mysql -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

mysqsl -e "GRANT SELECT ON $DB_NAME. * TO '$DB_USER'@'localhost' IDENTIFIED BY '@DB_PASSWORD';"
