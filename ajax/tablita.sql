-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 22-06-2023 a las 20:06:06
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tablita`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblprod`
--

DROP TABLE IF EXISTS `tblprod`;
CREATE TABLE IF NOT EXISTS `tblprod` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `prod_code` varchar(20) NOT NULL,
  `prod_name` varchar(50) NOT NULL,
  `prod_ctry` varchar(50) NOT NULL,
  `prod_qty` int NOT NULL,
  `price` decimal(12,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `book_id` (`prod_code`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblprod`
--

INSERT INTO `tblprod` (`id`, `prod_code`, `prod_name`, `prod_ctry`, `prod_qty`, `price`) VALUES
(22, '0016', 'pc gamer', 'tecnologia', 10, '6000.00'),
(37, '0001', 'manzana', 'Frutas', 50, '1.50'),
(40, '0002', 'Lechuga', 'Verduras', 10, '1.50'),
(41, '0003', 'Zanahoria', 'Verduras', 15, '2.50'),
(43, '0005', 'Pollo a la Brasa', 'Comida', 5, '52.50'),
(44, '0006', 'Atún', 'Enlatados', 50, '4.55'),
(46, '0008', 'Oveja', 'comida', 20, '30.00'),
(47, '0009', 'Fideos', 'Pastas', 60, '2.00'),
(48, '0011', 'Huevo', 'Comida', 60, '9.00'),
(49, '0012', 'Leche', 'Lacteos', 80, '4.00'),
(50, '00141', 'YukiRito2', 'tecnologia', 41, '25.30'),
(51, '0052', 'asado', 'comida', 520, '51.50');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
