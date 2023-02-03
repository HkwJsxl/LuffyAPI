/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80032
 Source Host           : localhost:3306
 Source Schema         : luffyapi

 Target Server Type    : MySQL
 Target Server Version : 80032
 File Encoding         : 65001

 Date: 03/02/2023 10:13:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 用户表', 6, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (22, 'Can change 用户表', 6, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 用户表', 6, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (24, 'Can view 用户表', 6, 'view_userinfo');
INSERT INTO `auth_permission` VALUES (25, 'Can add 轮播表', 7, 'add_banner');
INSERT INTO `auth_permission` VALUES (26, 'Can change 轮播表', 7, 'change_banner');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 轮播表', 7, 'delete_banner');
INSERT INTO `auth_permission` VALUES (28, 'Can view 轮播表', 7, 'view_banner');
INSERT INTO `auth_permission` VALUES (29, 'Can add 课程', 8, 'add_course');
INSERT INTO `auth_permission` VALUES (30, 'Can change 课程', 8, 'change_course');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 课程', 8, 'delete_course');
INSERT INTO `auth_permission` VALUES (32, 'Can view 课程', 8, 'view_course');
INSERT INTO `auth_permission` VALUES (33, 'Can add 分类', 9, 'add_coursecategory');
INSERT INTO `auth_permission` VALUES (34, 'Can change 分类', 9, 'change_coursecategory');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 分类', 9, 'delete_coursecategory');
INSERT INTO `auth_permission` VALUES (36, 'Can view 分类', 9, 'view_coursecategory');
INSERT INTO `auth_permission` VALUES (37, 'Can add 章节', 10, 'add_coursechapter');
INSERT INTO `auth_permission` VALUES (38, 'Can change 章节', 10, 'change_coursechapter');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 章节', 10, 'delete_coursechapter');
INSERT INTO `auth_permission` VALUES (40, 'Can view 章节', 10, 'view_coursechapter');
INSERT INTO `auth_permission` VALUES (41, 'Can add 导师', 11, 'add_teacher');
INSERT INTO `auth_permission` VALUES (42, 'Can change 导师', 11, 'change_teacher');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 导师', 11, 'delete_teacher');
INSERT INTO `auth_permission` VALUES (44, 'Can view 导师', 11, 'view_teacher');
INSERT INTO `auth_permission` VALUES (45, 'Can add 课时', 12, 'add_coursesection');
INSERT INTO `auth_permission` VALUES (46, 'Can change 课时', 12, 'change_coursesection');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 课时', 12, 'delete_coursesection');
INSERT INTO `auth_permission` VALUES (48, 'Can view 课时', 12, 'view_coursesection');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_luffy_userinfo_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_luffy_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `luffy_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2023-01-30 19:50:20.083897', '1', 'banner1', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2023-01-30 19:51:32.485799', '2', 'banner2', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (3, '2023-01-30 19:51:44.315255', '3', '/midea/static/banner/banner3.png', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (4, '2023-01-30 19:52:03.778661', '4', 'banner4', 1, '[{\"added\": {}}]', 7, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (8, 'course', 'course');
INSERT INTO `django_content_type` VALUES (9, 'course', 'coursecategory');
INSERT INTO `django_content_type` VALUES (10, 'course', 'coursechapter');
INSERT INTO `django_content_type` VALUES (12, 'course', 'coursesection');
INSERT INTO `django_content_type` VALUES (11, 'course', 'teacher');
INSERT INTO `django_content_type` VALUES (7, 'home', 'banner');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'user', 'userinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2023-01-30 19:45:37.989528');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2023-01-30 19:45:38.027435');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2023-01-30 19:45:38.133356');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2023-01-30 19:45:38.160462');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2023-01-30 19:45:38.166896');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2023-01-30 19:45:38.173875');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2023-01-30 19:45:38.181853');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2023-01-30 19:45:38.184845');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2023-01-30 19:45:38.191827');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2023-01-30 19:45:38.197630');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2023-01-30 19:45:38.205628');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2023-01-30 19:45:38.217577');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2023-01-30 19:45:38.223561');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2023-01-30 19:45:38.230543');
INSERT INTO `django_migrations` VALUES (15, 'user', '0001_initial', '2023-01-30 19:45:38.400747');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2023-01-30 19:45:38.474493');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2023-01-30 19:45:38.482471');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2023-01-30 19:45:38.490661');
INSERT INTO `django_migrations` VALUES (19, 'home', '0001_initial', '2023-01-30 19:45:38.513289');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2023-01-30 19:45:38.535263');
INSERT INTO `django_migrations` VALUES (21, 'course', '0001_initial', '2023-02-03 10:05:32.604851');
INSERT INTO `django_migrations` VALUES (22, 'home', '0002_auto_20230203_1005', '2023-02-03 10:05:32.624249');
INSERT INTO `django_migrations` VALUES (23, 'course', '0002_rename_pub_date_course_publish_date', '2023-02-03 10:12:11.119481');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('k4tm7j8iyjri8l9xx0c889tr0r9gb9ay', '.eJxVjDsOwjAQBe_iGln-7JKYkj5nsDbeNQ4gR4qTCnF3iJQC2jcz76UibWuJW5MlTqwuyqrT7zZSekjdAd-p3mad5rou06h3RR-06WFmeV4P9--gUCvfmnJ2AazJDAGlMy4kNISUEyB04nsQ7wkDn51n68R6Z4NB8iA9ZUPq_QHYCjdk:1pMSeU:Qbb8YFD4fZ2MI8SStFs4Vo-mM0Kazhsw_hYQUD5IFaI', '2023-02-13 19:48:46.673226');

-- ----------------------------
-- Table structure for luffy_banner
-- ----------------------------
DROP TABLE IF EXISTS `luffy_banner`;
CREATE TABLE `luffy_banner`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` int NOT NULL,
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `link` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `introduction` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_banner
-- ----------------------------
INSERT INTO `luffy_banner` VALUES (1, 0, 1, '2023-01-30 19:50:20.079930', '2023-01-30 19:50:20.079930', 1, 'banner1', '/static/banner/banner1.png', 'free-course/', 'banner1');
INSERT INTO `luffy_banner` VALUES (2, 0, 1, '2023-01-30 19:51:32.481779', '2023-01-30 19:51:32.481779', 1, 'banner2', '/static/banner/banner2.png', 'light-course/', 'banner2');
INSERT INTO `luffy_banner` VALUES (3, 0, 1, '2023-01-30 19:51:44.312263', '2023-01-30 19:51:44.312263', 1, 'banner3', '/static/banner/banner3.png', 'actual-course/', 'banner3');
INSERT INTO `luffy_banner` VALUES (4, 0, 1, '2023-01-30 19:52:03.776081', '2023-01-30 19:52:03.776081', 1, 'banner4', '/static/banner/banner4.png', 'free-course/', 'banner4');

-- ----------------------------
-- Table structure for luffy_course
-- ----------------------------
DROP TABLE IF EXISTS `luffy_course`;
CREATE TABLE `luffy_course`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` int NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `course_type` smallint NOT NULL,
  `brief` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `level` smallint NOT NULL,
  `publish_date` date NOT NULL,
  `period` int NOT NULL,
  `attachment_path` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` smallint NOT NULL,
  `price` decimal(8, 2) NOT NULL,
  `students` int NOT NULL,
  `sections` int NOT NULL,
  `publish_sections` int NOT NULL,
  `course_category_id` bigint NULL DEFAULT NULL,
  `teacher_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `luffy_course_course_category_id_ae7376a3`(`course_category_id` ASC) USING BTREE,
  INDEX `luffy_course_teacher_id_0202c7b2`(`teacher_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_course
-- ----------------------------
INSERT INTO `luffy_course` VALUES (1, 0, 1, '2019-07-14 13:54:33.095201', '2019-07-14 13:54:33.095238', 1, 'Python开发21天入门', 'courses/alex_python.png', 0, 'Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土', 0, '2019-07-14', 21, '', 0, 0.00, 231, 120, 120, 1, 1);
INSERT INTO `luffy_course` VALUES (2, 0, 1, '2019-07-14 13:56:05.051103', '2019-07-14 13:56:05.051142', 2, 'Python项目实战', 'courses/mjj_python.png', 0, '', 1, '2019-07-14', 30, '', 0, 99.00, 340, 120, 120, 1, 2);
INSERT INTO `luffy_course` VALUES (3, 0, 1, '2019-07-14 13:57:21.190053', '2019-07-14 13:57:21.190095', 3, 'Linux系统基础5周入门精讲', 'courses/lyy_linux.png', 0, '', 0, '2019-07-14', 25, '', 0, 39.00, 219, 100, 100, 2, 3);

-- ----------------------------
-- Table structure for luffy_course_category
-- ----------------------------
DROP TABLE IF EXISTS `luffy_course_category`;
CREATE TABLE `luffy_course_category`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` int NOT NULL,
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_course_category
-- ----------------------------
INSERT INTO `luffy_course_category` VALUES (1, 0, 1, '2019-07-14 13:40:58.690413', '2019-07-14 13:40:58.690477', 1, 'Python');
INSERT INTO `luffy_course_category` VALUES (2, 0, 1, '2019-07-14 13:41:08.249735', '2019-07-14 13:41:08.249817', 2, 'Linux');

-- ----------------------------
-- Table structure for luffy_course_chapter
-- ----------------------------
DROP TABLE IF EXISTS `luffy_course_chapter`;
CREATE TABLE `luffy_course_chapter`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` int NOT NULL,
  `chapter` smallint NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `summary` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `publish_date` date NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `luffy_course_chapter_course_id_fa245b81`(`course_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_course_chapter
-- ----------------------------
INSERT INTO `luffy_course_chapter` VALUES (1, 0, 1, '2019-07-14 13:58:34.867005', '2019-07-14 14:00:58.276541', 1, 1, '计算机原理', '', '2019-07-14', 1);
INSERT INTO `luffy_course_chapter` VALUES (2, 0, 1, '2019-07-14 13:58:48.051543', '2019-07-14 14:01:22.024206', 2, 2, '环境搭建', '', '2019-07-14', 1);
INSERT INTO `luffy_course_chapter` VALUES (3, 0, 1, '2019-07-14 13:59:09.878183', '2019-07-14 14:01:40.048608', 3, 1, '项目创建', '', '2019-07-14', 2);
INSERT INTO `luffy_course_chapter` VALUES (4, 0, 1, '2019-07-14 13:59:37.448626', '2019-07-14 14:01:58.709652', 4, 1, 'Linux环境创建', '', '2019-07-14', 3);

-- ----------------------------
-- Table structure for luffy_course_section
-- ----------------------------
DROP TABLE IF EXISTS `luffy_course_section`;
CREATE TABLE `luffy_course_section`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `orders` smallint UNSIGNED NOT NULL,
  `section_type` smallint NOT NULL,
  `section_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `duration` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `publish_date` datetime(6) NOT NULL,
  `free_trail` tinyint(1) NOT NULL,
  `chapter_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `luffy_course_Section_chapter_id_4517c0af`(`chapter_id` ASC) USING BTREE,
  CONSTRAINT `luffy_course_section_chk_1` CHECK (`orders` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_course_section
-- ----------------------------
INSERT INTO `luffy_course_section` VALUES (1, 0, 1, '2019-07-14 14:02:33.779098', '2019-07-14 14:02:33.779135', '计算机原理上', 1, 2, NULL, NULL, '2019-07-14 14:02:33.779193', 1, 1);
INSERT INTO `luffy_course_section` VALUES (2, 0, 1, '2019-07-14 14:02:56.657134', '2019-07-14 14:02:56.657173', '计算机原理下', 2, 2, NULL, NULL, '2019-07-14 14:02:56.657227', 1, 1);
INSERT INTO `luffy_course_section` VALUES (3, 0, 1, '2019-07-14 14:03:20.493324', '2019-07-14 14:03:52.329394', '环境搭建上', 1, 2, NULL, NULL, '2019-07-14 14:03:20.493420', 0, 2);
INSERT INTO `luffy_course_section` VALUES (4, 0, 1, '2019-07-14 14:03:36.472742', '2019-07-14 14:03:36.472779', '环境搭建下', 2, 2, NULL, NULL, '2019-07-14 14:03:36.472831', 0, 2);
INSERT INTO `luffy_course_section` VALUES (5, 0, 1, '2019-07-14 14:04:19.338153', '2019-07-14 14:04:19.338192', 'web项目的创建', 1, 2, NULL, NULL, '2019-07-14 14:04:19.338252', 1, 3);
INSERT INTO `luffy_course_section` VALUES (6, 0, 1, '2019-07-14 14:04:52.895855', '2019-07-14 14:04:52.895890', 'Linux的环境搭建', 1, 2, NULL, NULL, '2019-07-14 14:04:52.895942', 1, 4);

-- ----------------------------
-- Table structure for luffy_teacher
-- ----------------------------
DROP TABLE IF EXISTS `luffy_teacher`;
CREATE TABLE `luffy_teacher`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` int NOT NULL,
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role` smallint NOT NULL,
  `title` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `signature` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `brief` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_teacher
-- ----------------------------
INSERT INTO `luffy_teacher` VALUES (1, 0, 1, '2019-07-14 13:44:19.661327', '2019-07-14 13:46:54.246271', 1, 'Alex', 1, '老男孩Python教学总监', '金角大王', 'teacher/alex_icon.png', '老男孩教育CTO & CO-FOUNDER 国内知名PYTHON语言推广者 51CTO学院20162017年度最受学员喜爱10大讲师之一 多款开源软件作者 曾任职公安部、飞信、中金公司、NOKIA中国研究院、华尔街英语、ADVENT、汽车之家等公司');
INSERT INTO `luffy_teacher` VALUES (2, 0, 1, '2019-07-14 13:45:25.092902', '2019-07-14 13:45:25.092936', 2, 'Mjj', 0, '前美团前端项目组架构师', NULL, 'teacher/mjj_icon.png', '是马JJ老师, 一个集美貌与才华于一身的男人，搞过几年IOS，又转了前端开发几年，曾就职于美团网任高级前端开发，后来因为不同意王兴(美团老板)的战略布局而出家做老师去了，有丰富的教学经验，开起车来也毫不含糊。一直专注在前端的前沿技术领域。同时，爱好抽烟、喝酒、烫头(锡纸烫)。 我的最爱是前端，因为前端妹子多。');
INSERT INTO `luffy_teacher` VALUES (3, 0, 1, '2019-07-14 13:46:21.997846', '2019-07-14 13:46:21.997880', 3, 'Lyy', 0, '老男孩Linux学科带头人', NULL, 'teacher/lyy_icon.png', 'Linux运维技术专家，老男孩Linux金牌讲师，讲课风趣幽默、深入浅出、声音洪亮到爆炸');

-- ----------------------------
-- Table structure for luffy_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `luffy_userinfo`;
CREATE TABLE `luffy_userinfo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE,
  UNIQUE INDEX `mobile`(`mobile` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_userinfo
-- ----------------------------
INSERT INTO `luffy_userinfo` VALUES (1, 'pbkdf2_sha256$260000$KkonLJpWS1nlP5fIaExUhe$FeFrMTlQMLqgiUGup9tLkCti3lhAeb4ecYd7QDc60us=', '2023-01-30 19:48:46.670934', 1, 'root', '', '', 'hkwJsxl@gmail.com', 1, 1, '2023-01-30 19:48:39.179164', '', 'avatars/default.png');

-- ----------------------------
-- Table structure for luffy_userinfo_groups
-- ----------------------------
DROP TABLE IF EXISTS `luffy_userinfo_groups`;
CREATE TABLE `luffy_userinfo_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userinfo_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `luffy_userinfo_groups_userinfo_id_group_id_cd0db8aa_uniq`(`userinfo_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `luffy_userinfo_groups_group_id_f3b2ce50_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `luffy_userinfo_groups_group_id_f3b2ce50_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `luffy_userinfo_groups_userinfo_id_52d0d0f7_fk_luffy_userinfo_id` FOREIGN KEY (`userinfo_id`) REFERENCES `luffy_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_userinfo_groups
-- ----------------------------

-- ----------------------------
-- Table structure for luffy_userinfo_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `luffy_userinfo_user_permissions`;
CREATE TABLE `luffy_userinfo_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userinfo_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `luffy_userinfo_user_perm_userinfo_id_permission_i_e196abf7_uniq`(`userinfo_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `luffy_userinfo_user__permission_id_973f52c0_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `luffy_userinfo_user__permission_id_973f52c0_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `luffy_userinfo_user__userinfo_id_30dc40fb_fk_luffy_use` FOREIGN KEY (`userinfo_id`) REFERENCES `luffy_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of luffy_userinfo_user_permissions
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
