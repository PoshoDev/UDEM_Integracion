START TRANSACTION;

DELIMITER $$
DROP PROCEDURE IF EXISTS AutomovilGetMarca $$
CREATE PROCEDURE AutomovilGetMarca(_marca CHAR(32))
BEGIN

    SELECT  automovil.id,
            automovil.modelo,
            automovil.color,
            automovil.precio,
            automovil.unidades
    FROM    automovil, marca
    WHERE   automovil.marca=marca.id
            AND marca.nombre=_marca;

END $$
DELIMITER ;

COMMIT;
