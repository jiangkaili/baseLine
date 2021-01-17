##### 一、配置文件分成3级
1.  config.ini 外部配置文件
2.  BaseLine/common/core/setting.py 主要是用来读取外部的配置文件
3.  BaseLine/settings.py 核心配置文件
##### 二、启动脚本
- cd到manage.py的同级目录下

`pip install -r requirements.txt`
`python manage.py runserver 0.0.0.0:8000` 即可简单调试

- 如果需要服务器稳定可以自己pip一个uwsgi或者daphne服务器

##### 三、具体测试的时候
只需要修改 config.ini文件即可（目前只支持mysql配置）
如果需要其他的 需要config.ini <--> BaseLine/common/core/setting.py 需要联动

##### 四、目前的数据脱敏功能（功能比较单一）
创建一个checkinfo表

`CREATE TABLE `tb_check_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mobile` varchar(11) NOT NULL,
  `username` varchar(11) NOT NULL,
  `id_card` varchar(54) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `id_card` (`id_card`)
) ENGINE=InnoDB AUTO_INCREMENT=3`

敏感数据测试，如果需要其他字段需要在 mysql表 <--> models联动：

`BaseLine/BaseLine/apps/checkinfo/models.py`

##### 五、脱库操作适用所有场景