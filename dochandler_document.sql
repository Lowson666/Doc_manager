
SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `dochandler_document`;
CREATE TABLE `dochandler_document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL COMMENT '文档名',
  `content` longtext NOT NULL COMMENT '文章正文',
  `desc` longtext COMMENT '文档说明',
  `add_user` varchar(64) DEFAULT NULL COMMENT'所属分类',
  `add_time` datetime(6) NOT NULL COMMENT '添加时间',
  `is_del` tinyint(1) NOT NULL COMMENT '逻辑删除',
  `cate_id` int(11) NOT NULL COMMENT '添加者',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `dochandler_document_cate_id_2fc13265_fk_dochandle` (`cate_id`),
  CONSTRAINT `dochandler_document_cate_id_2fc13265_fk_dochandle` FOREIGN KEY (`cate_id`) REFERENCES `dochandler_documentcategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

