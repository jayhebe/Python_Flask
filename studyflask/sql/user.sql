CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nickname` varchar(30) NOT NULL,
  `login_name` varchar(20) NOT NULL,
  `login_pwd` varchar(32) NOT NULL,
  `login_salt` varchar(32) NOT NULL,
  `status` tinyint(3) NOT NULL DEFAULT '1',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_login_name` (`login_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4