CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(20) UNIQUE NOT NULL,
  password VARCHAR(64) NOT NULL,
  email VARCHAR(30) UNIQUE NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users (username, password, email) values ('gorira', 'gorira', 'gorira@example.com');
INSERT INTO users (username, password, email) values ('panda', 'panda', 'panda@example.com');
INSERT INTO users (username, password, email) values ('rabbit', 'rabbit', 'rabbit@example.com');
INSERT INTO users (username, password, email) values ('dog', 'dog', 'dog@example.com');
INSERT INTO users (username, password, email) values ('cat', 'cat', 'cat@example.com');