START TRANSACTION;

DELIMITER $$
DROP PROCEDURE IF EXISTS AutomovilGetAll $$
CREATE PROCEDURE AutomovilGetAll()
BEGIN

    SELECT  *
    FROM    automovil;

END $$
DELIMITER ;

COMMIT;
