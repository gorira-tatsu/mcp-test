CREATE TABLE users (
  num int NOT NULL AUTO_INCREMENT,
  username varchar(20) UNIQUE NOT NULL,
  password varchar(64) NOT NULL,
  email varchar(30) UNIQUE NOT NULL,
  primary key (num)
);
