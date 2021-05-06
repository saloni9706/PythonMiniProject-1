CREATE DATABASE IF NOT EXISTS `python_search_engine`;
USE `python_search_engine`;

--
-- Table structure for Employee
--
DROP TABLE IF EXISTS `crawler`;
CREATE TABLE `crawler`(
	`Title` varchar(500) default NULL,
    `Keywords` varchar(500) default NULL,
    `Url` varchar(500) default NULL,
    `Content` varchar(5000) default null
);


select * from crawler;
