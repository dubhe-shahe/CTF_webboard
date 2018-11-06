-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 28, 2018 at 07:19 PM
-- Server version: 5.7.21
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS CTF;
USE CTF;
--
-- Database: `CTF`
--

-- --------------------------------------------------------

--
-- Table structure for table `Problems`
--

CREATE TABLE `Problems` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '题目名称',
  `tag` varchar(255) NOT NULL COMMENT '题目分类',
  `flag` varchar(255) NOT NULL,
  `content` text NOT NULL COMMENT '题目描述',
  `points` float(11,2) NOT NULL COMMENT '题目分数（两位小数)',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Problems`
--

INSERT INTO `Problems` (`id`, `name`, `tag`, `flag`, `content`, `points`, `create_time`, `update_time`) VALUES
(1, 'Web Puzzle 01', 'web', 'flag{dubhe_best}', 'dubhe@dubehe.com', 10.00, '2018-10-26 21:58:38', '2018-10-26 21:58:38');

-- --------------------------------------------------------

--
-- Table structure for table `Record`
--

CREATE TABLE `Record` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL COMMENT '提交用户',
  `pid` int(11) NOT NULL COMMENT '提交问题',
  `state` int(11) NOT NULL COMMENT '提交结果',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Record`
--

INSERT INTO `Record` (`id`, `uid`, `pid`, `state`, `create_time`, `update_time`) VALUES
(1, 0, 0, 0, '2018-10-26 21:58:38', '2018-10-26 21:58:38');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL COMMENT '用户名',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `email` varchar(255) NOT NULL COMMENT '电子邮箱',
  `points` float(11,2) NOT NULL COMMENT '获得分数（两位小数）',
  `gender` varchar(255) NOT NULL COMMENT '性别',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `username`, `password`, `email`, `points`, `gender`, `create_time`, `update_time`) VALUES
(1, 'duhbe', '85b2f42582a1606d79a8741d3f26e595', 'dubhe@dubehe.com', 10.00, 'M', '2018-10-26 21:58:38', '2018-10-26 21:58:38'),
(2, 'a', 'a', 'a', 123.00, 'a', '2018-10-26 00:00:00', '2018-10-26 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `WriteUp`
--

CREATE TABLE `WriteUp` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL COMMENT '所属用户',
  `pid` int(11) NOT NULL COMMENT '所属题目',
  `title` text NOT NULL COMMENT '题解标题',
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `WriteUp`
--

INSERT INTO `WriteUp` (`id`, `uid`, `pid`, `title`,`content`, `create_time`, `update_time`) VALUES
(1, 0, 0, 'this is a title','this is a WriteUp', '2018-10-26 21:58:38', '2018-10-26 21:58:38');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Problems`
--
ALTER TABLE `Problems`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Record`
--
ALTER TABLE `Record`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `WriteUp`
--
ALTER TABLE `WriteUp`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Problems`
--
ALTER TABLE `Problems`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Record`
--
ALTER TABLE `Record`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `WriteUp`
--
ALTER TABLE `WriteUp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
