-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (1, 1, 1, 0, '2019-07-14 13:44:19.661327', '2019-07-14 13:46:54.246271', 'Alex', 1, '老男孩Python教学总监', '金角大王', 'teacher/alex_icon.png', '老男孩教育CTO & CO-FOUNDER 国内知名PYTHON语言推广者 51CTO学院2016\2017年度最受学员喜爱10大讲师之一 多款开源软件作者 曾任职公安部、飞信、中金公司、NOKIA中国研究院、华尔街英语、ADVENT、汽车之家等公司');
-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (2, 2, 1, 0, '2019-07-14 13:45:25.092902', '2019-07-14 13:45:25.092936', 'Mjj', 0, '前美团前端项目组架构师', NULL, 'teacher/mjj_icon.png', '是马JJ老师, 一个集美貌与才华于一身的男人，搞过几年IOS，又转了前端开发几年，曾就职于美团网任高级前端开发，后来因为不同意王兴(美团老板)的战略布局而出家做老师去了，有丰富的教学经验，开起车来也毫不含糊。一直专注在前端的前沿技术领域。同时，爱好抽烟、喝酒、烫头(锡纸烫)。 我的最爱是前端，因为前端妹子多。');
-- INSERT INTO luffy_teacher(id, orders, is_show, is_delete, created_time, updated_time, name, role, title, signature, image, brief) VALUES (3, 3, 1, 0, '2019-07-14 13:46:21.997846', '2019-07-14 13:46:21.997880', 'Lyy', 0, '老男孩Linux学科带头人', NULL, 'teacher/lyy_icon.png', 'Linux运维技术专家，老男孩Linux金牌讲师，讲课风趣幽默、深入浅出、声音洪亮到爆炸');



-- INSERT INTO luffy_course_category(id, orders, is_show, is_delete, created_time, updated_time, name) VALUES (1, 1, 1, 0, '2019-07-14 13:40:58.690413', '2019-07-14 13:40:58.690477', 'Python');
-- INSERT INTO luffy_course_category(id, orders, is_show, is_delete, created_time, updated_time, name) VALUES (2, 2, 1, 0, '2019-07-14 13:41:08.249735', '2019-07-14 13:41:08.249817', 'Linux');



-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_image, course_type, brief, level, publish_date, period, attachment_path, status, students, sections, publish_sections, price, course_category_id, teacher_id) VALUES (1, 1, 1, 0, '2019-07-14 13:54:33.095201', '2019-07-14 13:54:33.095238', 'Python开发21天入门', 'courses/alex_python.png', 0, 'Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土', 0, '2019-07-14', 21, '', 0, 231, 120, 120, 0.00, 1, 1);
-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_image, course_type, brief, level, publish_date, period, attachment_path, status, students, sections, publish_sections, price, course_category_id, teacher_id) VALUES (2, 2, 1, 0, '2019-07-14 13:56:05.051103', '2019-07-14 13:56:05.051142', 'Python项目实战', 'courses/mjj_python.png', 0, '', 1, '2019-07-14', 30, '', 0, 340, 120, 120, 99.00, 1, 2);
-- INSERT INTO luffy_course(id, orders, is_show, is_delete, created_time, updated_time, name, course_image, course_type, brief, level, publish_date, period, attachment_path, status, students, sections, publish_sections, price, course_category_id, teacher_id) VALUES (3, 3, 1, 0, '2019-07-14 13:57:21.190053', '2019-07-14 13:57:21.190095', 'Linux系统基础5周入门精讲', 'courses/lyy_linux.png', 0, '', 0, '2019-07-14', 25, '', 0, 219, 100, 100, 39.00, 2, 3);



-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, publish_date, course_id) VALUES (1, 1, 1, 0, '2019-07-14 13:58:34.867005', '2019-07-14 14:00:58.276541', 1, '计算机原理', '', '2019-07-14', 1);
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, publish_date, course_id) VALUES (2, 2, 1, 0, '2019-07-14 13:58:48.051543', '2019-07-14 14:01:22.024206', 2, '环境搭建', '', '2019-07-14', 1);
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, publish_date, course_id) VALUES (3, 3, 1, 0, '2019-07-14 13:59:09.878183', '2019-07-14 14:01:40.048608', 1, '项目创建', '', '2019-07-14', 2);
-- INSERT INTO luffy_course_chapter(id, orders, is_show, is_delete, created_time, updated_time, chapter, name, summary, publish_date, course_id) VALUES (4, 4, 1, 0, '2019-07-14 13:59:37.448626', '2019-07-14 14:01:58.709652', 1, 'Linux环境创建', '', '2019-07-14', 3);



-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (1, 1, 0, '2019-07-14 14:02:33.779098', '2019-07-14 14:02:33.779135', '计算机原理上', 1, 2, NULL, NULL, '2019-07-14 14:02:33.779193', 1, 1);
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (2, 1, 0, '2019-07-14 14:02:56.657134', '2019-07-14 14:02:56.657173', '计算机原理下', 2, 2, NULL, NULL, '2019-07-14 14:02:56.657227', 1, 1);
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (3, 1, 0, '2019-07-14 14:03:20.493324', '2019-07-14 14:03:52.329394', '环境搭建上', 1, 2, NULL, NULL, '2019-07-14 14:03:20.493420', 0, 2);
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (4, 1, 0, '2019-07-14 14:03:36.472742', '2019-07-14 14:03:36.472779', '环境搭建下', 2, 2, NULL, NULL, '2019-07-14 14:03:36.472831', 0, 2);
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (5, 1, 0, '2019-07-14 14:04:19.338153', '2019-07-14 14:04:19.338192', 'web项目的创建', 1, 2, NULL, NULL, '2019-07-14 14:04:19.338252', 1, 3);
-- INSERT INTO luffy_course_Section(id, is_show, is_delete, created_time, updated_time, name, orders, section_type, section_link, duration, publish_date, free_trail, chapter_id) VALUES (6, 1, 0, '2019-07-14 14:04:52.895855', '2019-07-14 14:04:52.895890', 'Linux的环境搭建', 1, 2, NULL, NULL, '2019-07-14 14:04:52.895942', 1, 4);

