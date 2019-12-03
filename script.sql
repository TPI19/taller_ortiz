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
INSERT INTO taller_proceso(nombre,caracter,descripcion) VALUES('Ajuste de Motor','Reparación','Se realiza Ajuste de Anillos de Motor');			/*Proceso 4*/

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
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Pablo','Pablo','Díaz','PabloDiaz@gmail.com',1,1,1,'70187106','Reparto Metropolitano #6A');

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Edwin','Edwin','Amaya','EdwinAmaya@gmail.com',1,1,1,'70187110','Reparto Escalon #45A');

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Kike','Kike','Menjivar','KikeMenjivar@gmail.com',1,1,1,'70187107','Reparto Metropolitano #9A');

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Ricardo','Ricardo','Estupinián','RicardoEstupinian@gmail.com',1,1,1,'70187108','Reparto Metropolitano #6B');

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Diego','Diego','Ochoa','DiegOchoa@gmail.com',1,1,1,'70187111','Reparto Metropolitano #5W');

INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(1,2);
INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(1,3);
INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(1,4);
INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(2,5);
INSERT INTO taller_tecnico (especializacion_id, user_id) VALUES(3,6);

/*Inserción de Clientes*/

		/*Cliente #1 - 1 Vehiculos - 0 Visitas */
INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Gustavo','Gustavo','Carranza','GustavoCarranza@gmail.com',1,1,2,'70187107','Reparto Nica #7B');
INSERT INTO taller_cliente (user_id) VALUES(7);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)	/*Vehiculo 1*/
VALUES('P474-742','PickUp','Nissan', 'Frontier',1998,1);

INSERT INTO taller_expediente (vehiculo_id,detalle_mecanico,detalle_pintura,detalle_electrico,detalle_suspension,detalle_direccion) VALUES(1,'','','','','');	/*Expediente de Vehiculo 1*/

		/*Cliente #2 - 3 Vehiculos - 2 Visitas (1 a los primeros dos) */
INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Marina','Marina','Serrano','MarinaSerrano@gmail.com',1,1,2,'70187108','Reparto Zacate #8C');
INSERT INTO taller_cliente (user_id) VALUES(8);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)	/*Vehiculo 2*/
VALUES('P788-556','PickUp','Toyota', 'Hilux',1997,2);
INSERT INTO taller_expediente (vehiculo_id,detalle_mecanico,detalle_pintura,detalle_electrico,detalle_suspension,detalle_direccion) VALUES(2,'','','','','');	/*Expediente de Vehiculo 2*/
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)	/*Vehiculo 3*/
VALUES('P788-789','Sedan','Nissan', 'Versa',2015,2);
INSERT INTO taller_expediente (vehiculo_id,detalle_mecanico,detalle_pintura,detalle_electrico,detalle_suspension,detalle_direccion) VALUES(3,'','','','','');	/*Expediente de Vehiculo 3*/
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)	/*Vehiculo 4*/
VALUES('P788-235','Camioneta','Toyota', '4Runner',2018,2);
INSERT INTO taller_expediente (vehiculo_id,detalle_mecanico,detalle_pintura,detalle_electrico,detalle_suspension,detalle_direccion) VALUES(4,'','','','','');	/*Expediente de Vehiculo 4*/

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 1*/
VALUES('2019-11-24 00:00:00.000000','Mantenimiento','Se le realizó un cambio de frenos', 1, 1, 2, 1);
UPDATE taller_slot SET disponible = 1 WHERE id = 1;

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 2*/
VALUES('2019-11-24 00:00:00.000000','Mantenimiento','Se le realizó un cambio de aceite', 3, 1, 4, 1);
UPDATE taller_slot SET disponible = 1 WHERE id = 3;

	/*Cliente 3 - 0 Vehiculos - 0 Visitas */

INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Daniela','Daniela','Contreras','DanielaContreras@gmail.com',1,1,2,'70187109','Reparto Habana #9C');
INSERT INTO taller_cliente (user_id) VALUES(9);

	/*Cliente #4 - 1 Vehiculos - 3 Visitas - 1 Activa */
INSERT INTO users_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, rol, telefono, direccion)
VALUES('pbkdf2_sha256$150000$RYnHHjE3icRe$1WiEfMWWJp+WOYDMAcMEw4qU3Hk6fkH31ArWWkVobrQ=',0,'Oscar','Oscar','Rodriguez','OscarRodriguez@gmail.com',1,1,2,'70187125','Reparto Metropolitano #5D');
INSERT INTO taller_cliente (user_id) VALUES(10);
INSERT INTO taller_vehiculo (placa, tipo, marca, modelo, anio, cliente_id)	/*Vehiculo 5*/
VALUES('P788-571','PickUp','Toyota', 'Hilux',2000,4);
INSERT INTO taller_expediente (vehiculo_id,detalle_mecanico,detalle_pintura,detalle_electrico,detalle_suspension,detalle_direccion) VALUES(5,' ',' ',' ',' ',' ');	/*Expediente de Vehiculo 5*/

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 3*/
VALUES('2019-11-27 00:00:00.000000','Mantenimiento','Se le realizó un cambio de aceite', 12, 1, 5, 1);
UPDATE taller_slot SET disponible = 1 WHERE id = 1;

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 4*/
VALUES('2019-11-27 00:00:00.000000','Mantenimiento','Se le realizó un cambio de frenos', 3, 1, 5, 1);
UPDATE taller_slot SET disponible = 1 WHERE id = 3;

INSERT INTO taller_visita (fecha, caracter, comentarios, slot_id, tecnico_id, vehiculo_id,finalizada)	/*Visita 5*/
VALUES('2019-11-27 00:00:00.000000','Reparación','Ajuste de Motor', 11, 1, 5, 0);
UPDATE taller_slot SET disponible = 0 WHERE id = 11;

	/*Agregando Procesos a las visitas*/

INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(3,1);	/*Proceso 1 en visita 1 - proceso_visita 1*/
INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(1,2);	/*Proceso 3 en visita 2 - proceso_visita 2*/

INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(1,3);	/*Proceso 1 en visita 3 - proceso_visita 3*/
INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(3,4);	/*Proceso 3 en visita 4 - proceso_visita 4*/

INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(5,5);	/*Proceso 5 en visita 5 - proceso_visita 5*/
INSERT INTO taller_procesovisita (proceso_id,visita_id) VALUES(4,5);	/*Proceso 5 en visita 5 - proceso_visita 6*/

	/*Agregando Piezas o Materias a los Procesos de las visitas*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(2,5,1);	/*Pieza 2 usada en proceso_visita 1*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,9,1);	/*Pieza 1 usada en proceso_visita 1*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(4,1,2);	/*Pieza 4 usada en proceso_visita 2*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,2,2);	/*Pieza 1 usada en proceso_visita 2*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(4,1,3);	/*Pieza 1 usada en proceso_visita 3*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,2,3);	/*Pieza 2 usada en proceso_visita 3*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(2,5,4);	/*Pieza 5 usada en proceso_visita 4*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,9,4);	/*Pieza 9 usada en proceso_visita 4*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,10,4);	/*Pieza 10 usada en proceso_visita 4*/

INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(5,3,5);	/*Pieza 3 usada en proceso_visita 5*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(4,6,5);	/*Pieza 6 usada en proceso_visita 5*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,8,5);	/*Pieza 8 usada en proceso_visita 5*/
INSERT INTO taller_procesopieza(cantidad, pieza_id, proceso_visita_id) VALUES(1,9,5);	/*Pieza 9 usada en proceso_visita 5*/