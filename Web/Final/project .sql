-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 11, 2018 at 09:37 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `mc`
--

CREATE TABLE `mc` (
  `mc_id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `days` int(11) NOT NULL,
  `requester` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `approve_status` varchar(11) NOT NULL,
  `mc_img` varchar(50000) NOT NULL,
  `approver` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `msg_date` date NOT NULL,
  `to_super` varchar(500) NOT NULL,
  `from_name` varchar(50) NOT NULL,
  `from_id` int(11) NOT NULL,
  `msg` varchar(500) NOT NULL,
  `acknowledge` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `type` int(11) NOT NULL COMMENT '1 = supervisor, 0 = employee',
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(500) NOT NULL,
  `dept` varchar(100) NOT NULL,
  `leave_taken` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `type`, `username`, `password`, `name`, `dept`, `leave_taken`) VALUES
(1, 1, 'kenny', '123', 'KENNY', 'HUMAN RESOURCES', 0),
(2, 0, 'BETTY', '123', 'Betty', 'ACCOUNTING', 0),
(3, 0, 'kennedy', '123', 'KENNEDY', 'ACCOUNTING', 5),
(4, 1, 'bob', '123', 'BOB', 'PRODUCTION', 0),
(5, 0, 'kumar', '123', 'KUMAR', 'OTHER', 0),
(6, 0, 'ben', '123', 'BEN', 'RESEARCH AND DEVELOPMENT', 0),
(7, 1, 'benny', '123', 'BENNY', 'ACCOUNTING', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mc`
--
ALTER TABLE `mc`
  ADD PRIMARY KEY (`mc_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mc`
--
ALTER TABLE `mc`
  MODIFY `mc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
