/*Inserción de Slots del Taller*/

INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,0);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,1);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,1);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,1);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,1);
INSERT INTO taller_slot (disponible,reservacion) VALUES(1,1);

INSERT INTO taller_pieza (nombre, descripcion) VALUES('1/4 Aceite','Lubricante');				/*Pieza 1*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Filtro','Aceite');						/*Pieza 2*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Baleros','Rodamientos');					/*Pieza 3*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Amortiguadores','Suspensión');			/*Pieza 4*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Pastillas de Freno','Pastillas Tokiko');	/*Pieza 5*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Bujias','NGK');							/*Pieza 6*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Llantas','Firestone');					/*Pieza 7*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Gasolina','Limpiador');					/*Pieza 8*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Engrasante','Lubricante');				/*Pieza 9*/
INSERT INTO taller_pieza (nombre, descripcion) VALUES('Pintura','Galón');						/*Pieza 10*/

/*Inserción de Procesos*/

INSERT INTO taller_proceso(nombre,caracter,descripcion) VALUES('Cambio de Aceite','Mantenimiento','Se realiza cambio de filtro y de aceite');	/*Proceso 1*/
INSERT INTO taller_proceso(nombre,caracter,descripcion) VALUES('Cambio de Llantas','Mantenimiento','Se realiza cambio de llanta');				/*Proceso 2*/
INSERT INTO taller_proceso(nombre,caracter,descripcion) VALUES('Cambio de Frenos','Mantenimiento','Se realiza cambio de pastillas');			/*Proceso 3*/
INSERT INTO taller_proceso(nombre,caracter,descripcion) VALUES('Enderezado de Culata','Reparación','Se realiza Enderezado de Culata');			/*Proceso 4*/

/*Inserción de Especializaciones para los técnicos*/

INSERT INTO taller_especializacion (nombre,descripcion) VALUES('Mecánico','Experto en mecánica automotriz');
INSERT INTO taller_especializacion (nombre,descripcion) VALUES('Pintor','Experto en pintura');
INSERT INTO taller_especializacion (nombre,descripcion) VALUES('Electricista','Experto en sistemas eléctricos');

/*Inserción de Administrador*/

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',1,'RMartinez','René','Martínez','ReneMarvera@gmail.com',1,1,0,'70187105','Reparto Metropolitano #5A');
INSERT INTO taller_administrador (user_id) VALUES(1);

/*Inserción de Técnico*/

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Paco','Paco','Flores','PacoFlores@gmail.com',1,1,1,'70187106','Reparto Metropolitano #6A');

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Calderon','Calderon','Sol','CalderonSol@gmail.com',1,1,1,'70187110','Reparto Escalon #45A');

INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(3,2);
INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(2,3);

/*Inserción de Clientes*/

		/*Cliente #1 - 1 Vehiculos - 0 Visitas */
INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Wicho','Wicho','Cartagena','WichoCartagena@gmail.com',1,1,2,'70187107','Reparto Nica #7B');
INSERT INTO taller_cliente (user_id) VALUES(4);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)
VALUES('P474-742','PickUp','Nissan', 'Frontier',1998,1);

		/*Cliente #2 - 2 Vehiculos - 2 Visitas (Una a cada vehiculo) */
INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Elias','Elias','Saca','EliaSaca@gmail.com',1,1,2,'70187108','Reparto Zacate #8C');
INSERT INTO taller_cliente (user_id) VALUES(5);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)
VALUES('P788-556','PickUp','Toyota', 'Hilux',1997,2);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)
VALUES('P788-789','Sedan','Nissan', 'Versa',2015,2);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)
VALUES('P788-235','Camioneta','Toyota', '4Runner',2018,2);

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 1*/
VALUES('2019-11-24 00:00:00.000000','Mantenimiento','Se le realizó un cambio de aceite', 1, 1, 2, 0);
UPDATE taller_slot SET disponible = 0 WHERE id = 1;

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 2*/
VALUES('2019-11-24 00:00:00.000000','Mantenimiento','Se le realizó un cambio de aceite', 3, 1, 4, 1);
UPDATE taller_slot SET disponible = 0 WHERE id = 3;

	/*Cliente 3 - 0 Vehiculos - 0 Visitas */

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Chamba','Chamba','Cerén','ChambaCeren@gmail.com',1,1,2,'70187109','Reparto Habana #9C');
INSERT INTO taller_cliente (user_id) VALUES(6);

INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(1,1);	/*Proceso 1 en visita 1*/
INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(3,2);	/*Proceso 3 en visita 2*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,2,1);	/*Pieza 2 usada en proceso_visita 1*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,1,1);	/*Pieza 1 usada en proceso_visita 1*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,5,2);	/*Pieza 5 usada en proceso_visita 2*/

