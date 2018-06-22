
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `dochandler_documentcategory`;
CREATE TABLE `dochandler_documentcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL COMMENT '分类名',
  `dev_group` varchar(64) DEFAULT NULL COMMENT '开发团队Leader',
  `desc` longtext COMMENT '项目分类说明',
  `add_user` varchar(64) DEFAULT NULL COMMENT '添加者',
  `add_time` datetime(6) NOT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
