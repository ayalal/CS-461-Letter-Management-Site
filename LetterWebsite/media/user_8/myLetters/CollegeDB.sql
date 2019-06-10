-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: classmysql.engr.oregonstate.edu:3306
-- Generation Time: Apr 25, 2019 at 12:07 AM
-- Server version: 10.3.13-MariaDB-log
-- PHP Version: 7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `persist_cs340_schutfoj`
--

-- --------------------------------------------------------

--
-- Table structure for table `Apply`
--

CREATE TABLE `Apply` (
  `sID` char(6) NOT NULL,
  `cName` char(20) NOT NULL,
  `major` char(20) NOT NULL,
  `decision` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Apply`
--

INSERT INTO `Apply` (`sID`, `cName`, `major`, `decision`) VALUES
('123', 'Cornell', 'EE', 'Y'),
('123', 'MIT', 'CS', 'N'),
('123', 'OSU', 'CS', 'Y'),
('123', 'OSU', 'EE', 'N'),
('123', 'U of O', 'CS', 'Y'),
('234', 'U of O', 'biology', 'N'),
('345', 'Cornell', 'bioengineering', 'N'),
('345', 'Cornell', 'CS', 'Y'),
('345', 'Cornell', 'EE', 'N'),
('345', 'MIT', 'bioengineering', 'Y'),
('543', 'MIT', 'CS', 'N'),
('678', 'Cornell', 'history', 'N'),
('678', 'Cornell', 'psychology', 'Y'),
('678', 'OSU', 'history', 'Y'),
('765', 'OSU', 'history', 'Y'),
('876', 'MIT', 'biology', 'Y'),
('876', 'MIT', 'marine biology', 'N'),
('876', 'OSU', 'CS', 'N'),
('987', 'OSU', 'CS', 'Y'),
('987', 'U of O', 'CS', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `College`
--

CREATE TABLE `College` (
  `cName` char(20) NOT NULL,
  `state` char(2) DEFAULT NULL,
  `enrollment` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `College`
--

INSERT INTO `College` (`cName`, `state`, `enrollment`) VALUES
('Cornell', 'NY', 21000),
('MIT', 'MA', 10000),
('OSU', 'OR', 28000),
('U of O', 'OR', 25000);

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE `Student` (
  `sID` char(6) NOT NULL,
  `sName` char(20) NOT NULL,
  `GPA` decimal(3,2) DEFAULT NULL,
  `sizeHS` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`sID`, `sName`, `GPA`, `sizeHS`) VALUES
('123', 'Amy', '3.90', 1000),
('234', 'Bob', '3.60', 1500),
('345', 'Craig', '3.50', 500),
('456', 'Doris', '3.90', 1000),
('543', 'Craig', '3.40', 2000),
('567', 'Edward', '2.90', 2000),
('654', 'Amy', '3.90', 1000),
('678', 'Fay', '3.80', 200),
('765', 'Jay', '2.90', 1500),
('789', 'Gary', '3.40', 800),
('876', 'Irene', '3.90', 400),
('987', 'Helen', '4.00', 800);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Apply`
--
ALTER TABLE `Apply`
  ADD PRIMARY KEY (`sID`,`cName`,`major`);

--
-- Indexes for table `College`
--
ALTER TABLE `College`
  ADD PRIMARY KEY (`cName`);

--
-- Indexes for table `Student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`sID`),
  ADD UNIQUE KEY `student_PK` (`sID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
