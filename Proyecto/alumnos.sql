CREATE DATABASE alumnos_db;
USE alumnos_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE alumnos (
    matricula VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    ap_pat VARCHAR(50),
    ap_mat VARCHAR(50),
    curp CHAR(18),
    telefono CHAR(10),
    especialidad VARCHAR(100),
    ciudad VARCHAR(100),
    estado VARCHAR(50)
);

-- Usuario de prueba
INSERT INTO usuarios (usuario, password) VALUES ('admin', '$2b$12$EjemploHashBcrypt...');
