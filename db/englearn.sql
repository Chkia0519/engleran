-- 建立資料庫
CREATE DATABASE IF NOT EXISTS `englearn` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `englearn`;

-- 建立 learnword 表
CREATE TABLE `learnword` (
  `en` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cn` text NOT NULL,
  `typ` text NOT NULL,
  `likeW` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `pracTimes` int(11) NOT NULL,
  `correctTimes` int(11) NOT NULL,
  `lotime` DATETIME NOT NULL,
  `note` text NOT NULL,
  UNIQUE KEY `en` (`en`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 建立 nword 表
CREATE TABLE `nword` (
  `en` text NOT NULL,
  `cn` text NOT NULL,
  `typ` text NOT NULL,
  `likeW` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 建立 user 表
CREATE TABLE `user` (
  `acc` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
