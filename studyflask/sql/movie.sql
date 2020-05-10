CREATE TABLE `movie` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `classify` varchar(100) NOT NULL,
  `actors` varchar(200) NOT NULL,
  `cover_pic` varchar(300) NOT NULL,
  `pics` varchar(1000) NOT NULL,
  `url` varchar(300) NOT NULL,
  `description` text,
  `magnet_url` varchar(5000) NOT NULL,
  `hash_value` varchar(32) NOT NULL,
  `pub_date` datetime DEFAULT NULL,
  `source` varchar(20) NOT NULL,
  `view_counter` int(11) DEFAULT '0',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4