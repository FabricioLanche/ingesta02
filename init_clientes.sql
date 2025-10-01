CREATE TABLE IF NOT EXISTS clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  edad INT
);

INSERT INTO clientes (id, nombre, apellido, edad) VALUES
  (1, 'geraldo', 'colchado', 20),
  (2, 'juan', 'salas', 15),
  (3, 'pedro', 'gamarra', 35);
