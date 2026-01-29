-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 
-- 伺服器版本： 8.0.17
-- PHP 版本： 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `englearn`
--

-- --------------------------------------------------------

--
-- 資料表結構 `learnword`
--

CREATE TABLE `learnword` (
  `en` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cn` text NOT NULL,
  `typ` text NOT NULL,
  `likeW` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `pracTimes` int(11) NOT NULL,
  `correctTimes` int(11) NOT NULL,
  `lotime` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `learnword`
--

INSERT INTO `learnword` (`en`, `cn`, `typ`, `likeW`, `pracTimes`,'correctTimes', `lotime`) VALUES
('None', 'None', 'None', '0', 0, 0,'2026-01-20');

-- --------------------------------------------------------

--
-- 資料表結構 `nword`
--

CREATE TABLE `nword` (
  `en` text NOT NULL,
  `cn` text NOT NULL,
  `typ` text NOT NULL,
  `likeW` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `nword`
--

INSERT INTO `nword` (`en`, `cn`, `typ`, `likeW`) VALUES
('audience', '觀眾', '名詞（人物）', 'viewers, spectators'),
('gym', '體育館；健身房', '名詞（地點）', 'arena, stadium, sports center'),
('prime', '巔峰', '形容詞', 'peak / pinnacle'),
('sequel', '續集', '名詞', 'following work, subsequent development'),
('competitive', '競爭的', '修飾詞（狀態）', 'competing, striving'),
('stadium', '競技場', '名詞（地點）', 'arena'),
('serious', '嚴重的', '修飾詞（狀態）', 'severe'),
('pharmacist', '藥劑師；藥商', '名詞（人物）', 'druggist'),
('pharmacy', '藥局', '名詞（地點）', 'drugstore'),
('gallery', '藝廊', '名詞（地點）', 'corridor');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `acc` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `learnword`
--
ALTER TABLE `learnword`
  ADD UNIQUE KEY `en` (`en`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
