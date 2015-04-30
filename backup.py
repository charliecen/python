
# more backup.py
#!/usr/bin/python
#encodeing:utf-8

import os
import time
import string

#需要备份的目录
source = ['/usr/local/nagios','/var/www/html/cacti']
#存放备份的路径
target_dir = '/data/backup/nagios&cacti'
#目录日期
today = target_dir + time.strftime('%Y%m%d')
#当前时间
now = time.strftime('%H%M%S')
#创建存放备份的目录
if not os.path.exists(today):
        os.mkdir(today)
        print 'Successful created directory', today
else:
        print 'Already Directory'
#停留5秒
time.sleep(5)
#备份名字
target = today + os.sep + now + '.zip'
#备份压缩命令
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
#检查备份是否成功
if os.system(zip_command) == 0:
        print 'Successful backup to', target
else:
        print 'Backup  failed'
#mysql备份
""" mysql-backup"""
#定义备份数据库名
databases = ['cacti','Syslog']
#数据库用户
sql_user = 'root'
#数据库密码
sql_pwd = 'root'
#定义存放备份的目录
mkdir_dir = "/data/backup/mysql/"
bak_dir = '/data/backup/*'
remote_ip = '1.0.0.1'
remote_dir = '/backup/mhfile/monitor'

#创建目录
if not os.path.exists(mkdir_dir):
        os.mkdir(mkdir_dir)
        print 'Successfully created directory', mkdir_dir
#使用for循环来备份数据库
for database_name in databases:
        os.chdir(mkdir_dir)
        today_sql = mkdir_dir+database_name+'_'+time.strftime('%Y%m%d')+'.sql'
        sql_comm = 'mysqldump -u %s -p%s %s > %s'%(sql_user,sql_pwd,database_name,today_sql)
        if os.system(sql_comm) == 0:
                print database_name,'was backup successful!'
        else:
                print database_name,'was backup failed!'


time.sleep(3)
scp_comm = "scp -r %s %s:%s" % (bak_dir,remote_ip,remote_dir)
if os.system(scp_comm) == 0:
        print "copy backup was successful!"
else:
        print "copy backup was failed!"
