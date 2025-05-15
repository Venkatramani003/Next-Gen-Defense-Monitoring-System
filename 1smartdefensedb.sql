-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 23, 2024 at 07:35 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1smartdefensedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `activitytb`
--

CREATE TABLE `activitytb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Time` varchar(250) NOT NULL,
  `ActivityInfo` varchar(500) NOT NULL,
  `Hash1` varchar(500) NOT NULL,
  `Hash2` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `activitytb`
--

INSERT INTO `activitytb` (`id`, `UserName`, `Date`, `Time`, `ActivityInfo`, `Hash1`, `Hash2`) VALUES
(1, 'san123', '2024-11-23', '10:42:33', 'Login', '0', '7A971AEA315BBF0E1568A016D3B7750FA80318F5BEC93F81CB15448A3F9BE581'),
(2, 'san123', '2024-11-23', '10:43:19', 'File Upload FileName:2091 (1).jpg', '7A971AEA315BBF0E1568A016D3B7750FA80318F5BEC93F81CB15448A3F9BE581', '97DAA45F4991B96EF38A54D4BCC2044C91C9BF92C1B20674602BF265F63A8CA5'),
(3, 'san123', '2024-11-23', '10:51:06', 'Login', '97DAA45F4991B96EF38A54D4BCC2044C91C9BF92C1B20674602BF265F63A8CA5', '5BCFFD19054D492CB8B6B8D08CE9684F44CE2F4D14E8EC3A3E7A21C2F03451FC'),
(4, 'san', '2024-11-23', '10:51:08', 'Logout', '5BCFFD19054D492CB8B6B8D08CE9684F44CE2F4D14E8EC3A3E7A21C2F03451FC', '0641AED1C10C2108A0590AB37B65C6ADC0073FAAFAEFF31A59847755F6045294'),
(5, 'san123', '2024-11-23', '12:26:59', 'File Share tosan123FileName:2091 (1).jpg', '0641AED1C10C2108A0590AB37B65C6ADC0073FAAFAEFF31A59847755F6045294', '9D4A9872A784E4551D01A1BB6251E169D91B312BF662FB2E6D2AD9B604DE2B9E');

-- --------------------------------------------------------

--
-- Table structure for table `filetb`
--

CREATE TABLE `filetb` (
  `id` bigint(20) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `FileInfo` varchar(500) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `shareName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `filetb`
--

INSERT INTO `filetb` (`id`, `UserName`, `FileInfo`, `FileName`, `shareName`) VALUES
(1, 'san123', 'my file', '2091 (1).jpg', 'san123'),
(2, 'san123', '2091 (1).jpg', '2091 (1).jpg', 'san123');

-- --------------------------------------------------------

--
-- Table structure for table `officertb`
--

CREATE TABLE `officertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `officertb`
--

INSERT INTO `officertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '09486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  `ImageName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `LoginKey`, `ImageName`) VALUES
(1, 'sangeeth Kumar', '09486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san123', 'san123', 'Active', '8016', 'static/user/san123.jpg'),
(2, 'viji', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'viji', 'viji', 'Active', '9764', 'static/user/viji.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `temptb`
--

