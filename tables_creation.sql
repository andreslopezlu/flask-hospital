-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`especialidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`especialidades` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE,
  UNIQUE INDEX `descripcion_UNIQUE` (`descripcion` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`identificaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`identificaciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_tipo_identificacion_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviacion_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`sexos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sexos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`grupos_sanguineos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`grupos_sanguineos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`roles` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  `descipcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE,
  UNIQUE INDEX `descipcion_UNIQUE` (`descipcion` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(200) NOT NULL,
  `username` VARCHAR(200) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `roles_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE,
  INDEX `fk_usuarios_roles1_idx` (`roles_id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_roles1`
    FOREIGN KEY (`roles_id`)
    REFERENCES `mydb`.`roles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`medicos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `identificacion` INT UNSIGNED NOT NULL,
  `identificaciones_id` INT UNSIGNED NOT NULL,
  `fecha_nacimiento` DATETIME NOT NULL,
  `sexos_id` INT UNSIGNED NOT NULL,
  `grupos_sanguineos_id` INT UNSIGNED NOT NULL,
  `registro_medico` INT UNSIGNED NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(100) NOT NULL,
  `contacto_emergencia` JSON NOT NULL,
  `salario` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_diurna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_nocturna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `usuarios_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `identificacion_UNIQUE` (`identificacion` ASC) VISIBLE,
  UNIQUE INDEX `registro_medico_UNIQUE` (`registro_medico` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefono_UNIQUE` (`telefono` ASC) VISIBLE,
  INDEX `fk_medicos_identificaciones1_idx` (`identificaciones_id` ASC) VISIBLE,
  INDEX `fk_medicos_sexos1_idx` (`sexos_id` ASC) VISIBLE,
  INDEX `fk_medicos_grupos_sanguineos1_idx` (`grupos_sanguineos_id` ASC) VISIBLE,
  INDEX `fk_medicos_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_medicos_identificaciones1`
    FOREIGN KEY (`identificaciones_id`)
    REFERENCES `mydb`.`identificaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_sexos1`
    FOREIGN KEY (`sexos_id`)
    REFERENCES `mydb`.`sexos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_grupos_sanguineos1`
    FOREIGN KEY (`grupos_sanguineos_id`)
    REFERENCES `mydb`.`grupos_sanguineos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicos_especialidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`medicos_especialidades` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `medicos_id` INT UNSIGNED NOT NULL,
  `especialidades_id` INT UNSIGNED NOT NULL,
  `fecha_vinculacion` DATETIME NOT NULL,
  `registro_medico_especialidad` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idmedicos_especialidades_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_medicos_especialidades_medicos_idx` (`medicos_id` ASC) VISIBLE,
  INDEX `fk_medicos_especialidades_especialidades1_idx` (`especialidades_id` ASC) VISIBLE,
  UNIQUE INDEX `registro_medico_especialidad_UNIQUE` (`registro_medico_especialidad` ASC) VISIBLE,
  CONSTRAINT `fk_medicos_especialidades_medicos`
    FOREIGN KEY (`medicos_id`)
    REFERENCES `mydb`.`medicos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_especialidades_especialidades1`
    FOREIGN KEY (`especialidades_id`)
    REFERENCES `mydb`.`especialidades` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`administrativos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`administrativos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `identificacion` INT UNSIGNED NOT NULL,
  `identificaciones_id` INT UNSIGNED NOT NULL,
  `fecha_nacimiento` DATETIME NOT NULL,
  `sexos_id` INT UNSIGNED NOT NULL,
  `grupos_sanguineos_id` INT UNSIGNED NOT NULL,
  `registro_profesional` INT UNSIGNED NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(100) NOT NULL,
  `contacto_emergencia` JSON NOT NULL,
  `salario` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_diurna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_nocturna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `usuarios_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `identificacion_UNIQUE` (`identificacion` ASC) VISIBLE,
  UNIQUE INDEX `registro_medico_UNIQUE` (`registro_profesional` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefono_UNIQUE` (`telefono` ASC) VISIBLE,
  INDEX `fk_medicos_identificaciones1_idx` (`identificaciones_id` ASC) VISIBLE,
  INDEX `fk_medicos_sexos1_idx` (`sexos_id` ASC) VISIBLE,
  INDEX `fk_medicos_grupos_sanguineos1_idx` (`grupos_sanguineos_id` ASC) VISIBLE,
  INDEX `fk_medicos_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_medicos_identificaciones100`
    FOREIGN KEY (`identificaciones_id`)
    REFERENCES `mydb`.`identificaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_sexos100`
    FOREIGN KEY (`sexos_id`)
    REFERENCES `mydb`.`sexos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_grupos_sanguineos100`
    FOREIGN KEY (`grupos_sanguineos_id`)
    REFERENCES `mydb`.`grupos_sanguineos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_usuarios100`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pacientes` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `identificacion` INT UNSIGNED NOT NULL,
  `identificaciones_id` INT UNSIGNED NOT NULL,
  `fecha_nacimiento` DATETIME NOT NULL,
  `sexos_id` INT UNSIGNED NOT NULL,
  `grupos_sanguineos_id` INT UNSIGNED NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(100) NOT NULL,
  `contacto_emergencia` JSON NOT NULL,
  `preferencia_notificacion` JSON NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `administrativos_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_pacientes_identificaciones1_idx` (`identificaciones_id` ASC) VISIBLE,
  UNIQUE INDEX `identificacion_UNIQUE` (`identificacion` ASC) VISIBLE,
  INDEX `fk_pacientes_sexos1_idx` (`sexos_id` ASC) VISIBLE,
  INDEX `fk_pacientes_grupos_sanguineos1_idx` (`grupos_sanguineos_id` ASC) VISIBLE,
  INDEX `fk_pacientes_administrativos1_idx` (`administrativos_id` ASC) VISIBLE,
  CONSTRAINT `fk_pacientes_identificaciones1`
    FOREIGN KEY (`identificaciones_id`)
    REFERENCES `mydb`.`identificaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pacientes_sexos1`
    FOREIGN KEY (`sexos_id`)
    REFERENCES `mydb`.`sexos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pacientes_grupos_sanguineos1`
    FOREIGN KEY (`grupos_sanguineos_id`)
    REFERENCES `mydb`.`grupos_sanguineos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pacientes_administrativos1`
    FOREIGN KEY (`administrativos_id`)
    REFERENCES `mydb`.`administrativos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`historiales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`historiales` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pacientes_id` INT UNSIGNED NOT NULL,
  `fecha_hora_apertura` DATETIME NOT NULL,
  `antecedentes` JSON NOT NULL,
  `observaciones` JSON NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_historiales_pacientes1_idx` (`pacientes_id` ASC) VISIBLE,
  CONSTRAINT `fk_historiales_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`niveles_prioridad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`niveles_prioridad` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`enfermeros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`enfermeros` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `identificacion` INT UNSIGNED NOT NULL,
  `identificaciones_id` INT UNSIGNED NOT NULL,
  `fecha_nacimiento` DATETIME NOT NULL,
  `sexos_id` INT UNSIGNED NOT NULL,
  `grupos_sanguineos_id` INT UNSIGNED NOT NULL,
  `registro_enfermeria` INT UNSIGNED NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(100) NOT NULL,
  `contacto_emergencia` JSON NOT NULL,
  `salario` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_diurna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `valor_hora_nocturna` DECIMAL(10,2) UNSIGNED NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `usuarios_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `identificacion_UNIQUE` (`identificacion` ASC) VISIBLE,
  UNIQUE INDEX `registro_medico_UNIQUE` (`registro_enfermeria` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefono_UNIQUE` (`telefono` ASC) VISIBLE,
  INDEX `fk_medicos_identificaciones1_idx` (`identificaciones_id` ASC) VISIBLE,
  INDEX `fk_medicos_sexos1_idx` (`sexos_id` ASC) VISIBLE,
  INDEX `fk_medicos_grupos_sanguineos1_idx` (`grupos_sanguineos_id` ASC) VISIBLE,
  INDEX `fk_medicos_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_medicos_identificaciones10`
    FOREIGN KEY (`identificaciones_id`)
    REFERENCES `mydb`.`identificaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_sexos10`
    FOREIGN KEY (`sexos_id`)
    REFERENCES `mydb`.`sexos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_grupos_sanguineos10`
    FOREIGN KEY (`grupos_sanguineos_id`)
    REFERENCES `mydb`.`grupos_sanguineos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicos_usuarios10`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`estados_turnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`estados_turnos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`turnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`turnos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha_hora_llegada` DATETIME NOT NULL,
  `estados_turnos_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_turnos_estados_turnos1_idx` (`estados_turnos_id` ASC) VISIBLE,
  CONSTRAINT `fk_turnos_estados_turnos1`
    FOREIGN KEY (`estados_turnos_id`)
    REFERENCES `mydb`.`estados_turnos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`admisiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admisiones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha_hora_inicio` DATETIME NOT NULL,
  `fecha_hora_fin` DATETIME NOT NULL,
  `motivo` JSON NOT NULL,
  `administrativos_id` INT UNSIGNED NOT NULL,
  `turnos_id` INT UNSIGNED NOT NULL,
  `pacientes_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_admisiones_turnos1_idx` (`turnos_id` ASC) VISIBLE,
  INDEX `fk_admisiones_pacientes1_idx` (`pacientes_id` ASC) VISIBLE,
  INDEX `fk_admisiones_administrativos1_idx` (`administrativos_id` ASC) VISIBLE,
  CONSTRAINT `fk_admisiones_turnos1`
    FOREIGN KEY (`turnos_id`)
    REFERENCES `mydb`.`turnos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_admisiones_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_admisiones_administrativos1`
    FOREIGN KEY (`administrativos_id`)
    REFERENCES `mydb`.`administrativos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`triages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`triages` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pacientes_id` INT UNSIGNED NOT NULL,
  `enfermeros_id` INT UNSIGNED NOT NULL,
  `niveles_prioridad_id` INT UNSIGNED NOT NULL,
  `signos_vitales` JSON NOT NULL,
  `fecha_hora_inicio` DATETIME NOT NULL,
  `fecha_hora_fin` DATETIME NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  `admisiones_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_triages_niveles_prioridad1_idx` (`niveles_prioridad_id` ASC) VISIBLE,
  INDEX `fk_triages_pacientes1_idx` (`pacientes_id` ASC) VISIBLE,
  INDEX `fk_triages_enfermeros1_idx` (`enfermeros_id` ASC) VISIBLE,
  INDEX `fk_triages_admisiones1_idx` (`admisiones_id` ASC) VISIBLE,
  CONSTRAINT `fk_triages_niveles_prioridad1`
    FOREIGN KEY (`niveles_prioridad_id`)
    REFERENCES `mydb`.`niveles_prioridad` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_triages_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_triages_enfermeros1`
    FOREIGN KEY (`enfermeros_id`)
    REFERENCES `mydb`.`enfermeros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_triages_admisiones1`
    FOREIGN KEY (`admisiones_id`)
    REFERENCES `mydb`.`admisiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`atenciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`atenciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pacientes_id` INT UNSIGNED NOT NULL,
  `historiales_id` INT UNSIGNED NOT NULL,
  `triages_id` INT UNSIGNED NOT NULL,
  `medicos_id` INT UNSIGNED NOT NULL,
  `fecha_hora_inicio` DATETIME NOT NULL,
  `fecha_hora_fin` DATETIME NOT NULL,
  `motivo_consulta` JSON NOT NULL,
  `evolucion` JSON NOT NULL,
  `diagnostico` JSON NOT NULL,
  `plan_manejo` JSON NOT NULL,
  `examen_fisico` JSON NOT NULL,
  `observacion` JSON NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_atenciones_medicos1_idx` (`medicos_id` ASC) VISIBLE,
  INDEX `fk_atenciones_pacientes1_idx` (`pacientes_id` ASC) VISIBLE,
  INDEX `fk_atenciones_triages1_idx` (`triages_id` ASC) VISIBLE,
  INDEX `fk_atenciones_historiales1_idx` (`historiales_id` ASC) VISIBLE,
  CONSTRAINT `fk_atenciones_medicos1`
    FOREIGN KEY (`medicos_id`)
    REFERENCES `mydb`.`medicos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atenciones_pacientes1`
    FOREIGN KEY (`pacientes_id`)
    REFERENCES `mydb`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atenciones_triages1`
    FOREIGN KEY (`triages_id`)
    REFERENCES `mydb`.`triages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atenciones_historiales1`
    FOREIGN KEY (`historiales_id`)
    REFERENCES `mydb`.`historiales` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`procedimientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`procedimientos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  `costo_historico` JSON NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicamentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`medicamentos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(500) NOT NULL,
  `abreviatura` VARCHAR(500) NOT NULL,
  `concentracion` VARCHAR(500) NOT NULL,
  `lote` VARCHAR(100) NOT NULL,
  `existencias` INT UNSIGNED NOT NULL,
  `costo_historico` JSON NOT NULL,
  `especificacion_tecnica` JSON NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`dispensaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dispensaciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `atenciones_id` INT UNSIGNED NOT NULL,
  `medicamentos_id` INT UNSIGNED NOT NULL,
  `cantidad_suministrada` INT UNSIGNED NOT NULL,
  `fecha_hora_entrega` DATETIME NOT NULL,
  `costo` INT UNSIGNED NOT NULL,
  `observacion` JSON NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_dispensaciones_medicamentos1_idx` (`medicamentos_id` ASC) VISIBLE,
  INDEX `fk_dispensaciones_atenciones1_idx` (`atenciones_id` ASC) VISIBLE,
  CONSTRAINT `fk_dispensaciones_medicamentos1`
    FOREIGN KEY (`medicamentos_id`)
    REFERENCES `mydb`.`medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dispensaciones_atenciones1`
    FOREIGN KEY (`atenciones_id`)
    REFERENCES `mydb`.`atenciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`metodos_pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`metodos_pago` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`estados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`estados` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`facturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`facturas` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `atenciones_id` INT UNSIGNED NOT NULL,
  `fecha_hora_facturacion` DATETIME NOT NULL,
  `subtotal` DECIMAL(10,2) UNSIGNED NOT NULL,
  `impuestos` INT UNSIGNED NOT NULL,
  `descuento` INT UNSIGNED NOT NULL,
  `total` DECIMAL(10,2) UNSIGNED NOT NULL,
  `metodos_pago_id` INT UNSIGNED NOT NULL,
  `estados_id` INT UNSIGNED NOT NULL,
  `metadata` JSON NOT NULL,
  `observacion` JSON NOT NULL,
  `administrativos_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_facturas_metodos_pago1_idx` (`metodos_pago_id` ASC) VISIBLE,
  INDEX `fk_facturas_estados1_idx` (`estados_id` ASC) VISIBLE,
  INDEX `fk_facturas_atenciones1_idx` (`atenciones_id` ASC) VISIBLE,
  INDEX `fk_facturas_administrativos1_idx` (`administrativos_id` ASC) VISIBLE,
  CONSTRAINT `fk_facturas_metodos_pago1`
    FOREIGN KEY (`metodos_pago_id`)
    REFERENCES `mydb`.`metodos_pago` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_estados1`
    FOREIGN KEY (`estados_id`)
    REFERENCES `mydb`.`estados` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_atenciones1`
    FOREIGN KEY (`atenciones_id`)
    REFERENCES `mydb`.`atenciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_administrativos1`
    FOREIGN KEY (`administrativos_id`)
    REFERENCES `mydb`.`administrativos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`presentaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`presentaciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `abreviatura` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `abreviatura_UNIQUE` (`abreviatura` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicamentos_presentaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`medicamentos_presentaciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `medicamentos_id` INT UNSIGNED NOT NULL,
  `presentaciones_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_medicamentos_presentaciones_medicamentos1_idx` (`medicamentos_id` ASC) VISIBLE,
  INDEX `fk_medicamentos_presentaciones_presentaciones1_idx` (`presentaciones_id` ASC) VISIBLE,
  CONSTRAINT `fk_medicamentos_presentaciones_medicamentos1`
    FOREIGN KEY (`medicamentos_id`)
    REFERENCES `mydb`.`medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicamentos_presentaciones_presentaciones1`
    FOREIGN KEY (`presentaciones_id`)
    REFERENCES `mydb`.`presentaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`procedimientos_atenciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`procedimientos_atenciones` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `atenciones_id` INT UNSIGNED NOT NULL,
  `procedimientos_id` INT UNSIGNED NOT NULL,
  `cantidad` INT UNSIGNED NOT NULL,
  `observacion` JSON NOT NULL,
  `costo` INT UNSIGNED NOT NULL,
  `medicos_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_procedimientos_atenciones_atenciones1_idx` (`atenciones_id` ASC) VISIBLE,
  INDEX `fk_procedimientos_atenciones_procedimientos1_idx` (`procedimientos_id` ASC) VISIBLE,
  INDEX `fk_procedimientos_atenciones_medicos1_idx` (`medicos_id` ASC) VISIBLE,
  CONSTRAINT `fk_procedimientos_atenciones_atenciones1`
    FOREIGN KEY (`atenciones_id`)
    REFERENCES `mydb`.`atenciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_procedimientos_atenciones_procedimientos1`
    FOREIGN KEY (`procedimientos_id`)
    REFERENCES `mydb`.`procedimientos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_procedimientos_atenciones_medicos1`
    FOREIGN KEY (`medicos_id`)
    REFERENCES `mydb`.`medicos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
