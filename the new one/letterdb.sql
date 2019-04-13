# Host: 127.0.0.1  (Version 5.7.25-log)
# Date: 2019-04-13 19:27:12
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "auth_group"
#

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "auth_group"
#


#
# Structure for table "auth_user"
#

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "auth_user"
#


#
# Structure for table "auth_user_groups"
#

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "auth_user_groups"
#


#
# Structure for table "django_content_type"
#

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'Letter','content'),(8,'Letter','fileinfo'),(9,'Letter','student'),(10,'Letter','teacher');

#
# Structure for table "django_admin_log"
#

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "django_admin_log"
#


#
# Structure for table "auth_permission"
#

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add content',7,'add_content'),(26,'Can change content',7,'change_content'),(27,'Can delete content',7,'delete_content'),(28,'Can view content',7,'view_content'),(29,'Can add fileinfo',8,'add_fileinfo'),(30,'Can change fileinfo',8,'change_fileinfo'),(31,'Can delete fileinfo',8,'delete_fileinfo'),(32,'Can view fileinfo',8,'view_fileinfo'),(33,'Can add student',9,'add_student'),(34,'Can change student',9,'change_student'),(35,'Can delete student',9,'delete_student'),(36,'Can view student',9,'view_student'),(37,'Can add teacher',10,'add_teacher'),(38,'Can change teacher',10,'change_teacher'),(39,'Can delete teacher',10,'delete_teacher'),(40,'Can view teacher',10,'view_teacher');

#
# Structure for table "auth_user_user_permissions"
#

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "auth_user_user_permissions"
#


#
# Structure for table "auth_group_permissions"
#

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "auth_group_permissions"
#


#
# Structure for table "django_migrations"
#

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` VALUES (1,'Letter','0001_initial',X'323031392D30342D31322032333A35373A35342E373131313032'),(2,'contenttypes','0001_initial',X'323031392D30342D31322032333A35373A35342E373439313032'),(3,'auth','0001_initial',X'323031392D30342D31322032333A35373A35342E383635313032'),(4,'admin','0001_initial',X'323031392D30342D31322032333A35373A35352E323438313032'),(5,'admin','0002_logentry_remove_auto_add',X'323031392D30342D31322032333A35373A35352E333334313032'),(6,'admin','0003_logentry_add_action_flag_choices',X'323031392D30342D31322032333A35373A35352E333431313032'),(7,'contenttypes','0002_remove_content_type_name',X'323031392D30342D31322032333A35373A35352E343234313032'),(8,'auth','0002_alter_permission_name_max_length',X'323031392D30342D31322032333A35373A35352E343337313032'),(9,'auth','0003_alter_user_email_max_length',X'323031392D30342D31322032333A35373A35352E343537313032'),(10,'auth','0004_alter_user_username_opts',X'323031392D30342D31322032333A35373A35352E343637313032'),(11,'auth','0005_alter_user_last_login_null',X'323031392D30342D31322032333A35373A35352E353035313032'),(12,'auth','0006_require_contenttypes_0002',X'323031392D30342D31322032333A35373A35352E353038313032'),(13,'auth','0007_alter_validators_add_error_messages',X'323031392D30342D31322032333A35373A35352E353136313032'),(14,'auth','0008_alter_user_username_max_length',X'323031392D30342D31322032333A35373A35352E353332313032'),(15,'auth','0009_alter_user_last_name_max_length',X'323031392D30342D31322032333A35373A35352E353438313032'),(16,'auth','0010_alter_group_name_max_length',X'323031392D30342D31322032333A35373A35352E353634313032'),(17,'auth','0011_update_proxy_permissions',X'323031392D30342D31322032333A35373A35352E353734313032'),(18,'sessions','0001_initial',X'323031392D30342D31322032333A35373A35352E353933313032'),(19,'Letter','0002_content_feedback',X'323031392D30342D31332030323A31353A35382E363535313032'),(20,'Letter','0003_auto_20190413_1208',X'323031392D30342D31332030343A30383A30352E303639363032'),(21,'Letter','0004_teacher_department',X'323031392D30342D31332030343A32323A35332E343535363032');

#
# Structure for table "django_session"
#

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "django_session"
#

INSERT INTO `django_session` VALUES ('6dtyjjeunylvky9v5diacr2j7vs7dpfa','MjBkZTM5NWUxZWY5OTRkYzE4MzM0NTNjZTEzYzlkOTA3NTdlNzQyMTp7ImlkIjoyLCJuYW1lIjoic3R1ZGVudDEifQ==',X'323031392D30342D32372031313A31303A35302E343532313032');

#
# Structure for table "letter_content"
#

DROP TABLE IF EXISTS `letter_content`;
CREATE TABLE `letter_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stufileid` int(11) NOT NULL,
  `stuid` int(11) NOT NULL,
  `requirement` varchar(100) NOT NULL,
  `teafileid` int(11) NOT NULL,
  `teaid` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "letter_content"
#

INSERT INTO `letter_content` VALUES (1,1,1,'i want to die ',17,2,'very well'),(2,1,1,'adfadf',19,1,NULL),(3,11,1,'12121',21,3,'very good'),(4,1,1,'kity',NULL,5,NULL),(5,1,1,'',18,1,NULL),(6,11,1,'fdf',NULL,1,'aaaa'),(7,12,1,'please give me five',NULL,8,NULL),(8,13,2,'please give me 100',NULL,3,NULL);

#
# Structure for table "letter_fileinfo"
#

DROP TABLE IF EXISTS `letter_fileinfo`;
CREATE TABLE `letter_fileinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `format` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "letter_fileinfo"
#

INSERT INTO `letter_fileinfo` VALUES (1,'txt','/etc/hosts',1),(11,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\media',1),(12,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_kn7O3u0.txt',1),(13,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_loTXbcM.txt',2),(14,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_mqJgQl4.txt',2),(15,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_ewUSFAY.txt',2),(16,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_GbVmNBN.txt',2),(17,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_cETyZ7E.txt',2),(18,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_dLFbBcS.txt',1),(19,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_PZHfskn.txt',1),(20,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_d9Y0egY.txt',2),(21,'txt','C:\\Users\\HH\\Desktop\\LetterWebsite\\mediaPotter_MXoLfwg.txt',3);

#
# Structure for table "letter_student"
#

DROP TABLE IF EXISTS `letter_student`;
CREATE TABLE `letter_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(100) NOT NULL,
  `psw` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

#
# Data for table "letter_student"
#

INSERT INTO `letter_student` VALUES (1,'aaa','aaa'),(2,'student1','123');

#
# Structure for table "letter_teacher"
#

DROP TABLE IF EXISTS `letter_teacher`;
CREATE TABLE `letter_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(100) NOT NULL,
  `psw` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

#
# Data for table "letter_teacher"
#

INSERT INTO `letter_teacher` VALUES (1,'wiliam','123','Applied Arts and Sciences'),(2,'bob','123','Applied Arts and Sciences'),(3,'alice','123','Computer Science'),(4,'tom','123','Earth and Space Sciences'),(5,'kitty','123','History'),(7,'bob','123','aaa'),(8,'worth','123','History'),(9,'teacher1','123','Computer Science');
