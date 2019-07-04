

### crontab 

###### [online](https://crontab.guru/)
* 在线测试 crontab 定时
* minute hour day month day

##### check crontab log
* `` sudo less /var/log/syslog | grep CRON``



##### 查看与添加任务
* 添加定时任务
crontab -e
* 任务列表
crontab -l
* 状态与重启
```
sudo /usr/sbin/service cron start
sudo /usr/sbin/service cron status
sudo /usr/sbin/service cron restart
 
```



#### demo


```
# 每天早上6点 
0 6 * * * echo "Good morning." >> /tmp/test.txt //注意单纯echo，从屏幕上看不到任何输出，因为cron把任何输出都email到root的信箱了。

# 每两个小时 
0 */2 * * * echo "Have a break now." >> /tmp/test.txt  

# 晚上11点到早上8点之间每两个小时和早上八点 
0 23-7/2，8 * * * echo "Have a good dream" >> /tmp/test.txt

# 每个月的4号和每个礼拜的礼拜一到礼拜三的早上11点 
0 11 4 * 1-3 command line

# 1月1日早上4点 
0 4 1 1 * command line SHELL=/bin/bash PATH=/sbin:/bin:/usr/sbin:/usr/bin MAILTO=root //如果出现错误，或者有数据输出，数据作为邮件发给这个帐号 HOME=/ 

# 每小时（第一分钟）执行/etc/cron.hourly内的脚本
01 * * * * root run-parts /etc/cron.hourly

# 每天（凌晨4：02）执行/etc/cron.daily内的脚本
02 4 * * * root run-parts /etc/cron.daily 

# 每星期（周日凌晨4：22）执行/etc/cron.weekly内的脚本
22 4 * * 0 root run-parts /etc/cron.weekly 

# 每月（1号凌晨4：42）去执行/etc/cron.monthly内的脚本 
42 4 1 * * root run-parts /etc/cron.monthly 

# 注意:  "run-parts"这个参数了，如果去掉这个参数的话，后面就可以写要运行的某个脚本名，而不是文件夹名。 　 

# 每天的下午4点、5点、6点的5 min、15 min、25 min、35 min、45 min、55 min时执行命令。 
5，15，25，35，45，55 16，17，18 * * * command

# 每周一，三，五的下午3：00系统进入维护状态，重新启动系统。
00 15 * *1，3，5 shutdown -r +5

# 每小时的10分，40分执行用户目录下的innd/bbslin这个指令： 
10，40 * * * * innd/bbslink 

# 每小时的1分执行用户目录下的bin/account这个指令： 
1 * * * * bin/account

# 每天早晨三点二十分执行用户目录下如下所示的两个指令（每个指令以;分隔）： 
203 * * * （/bin/rm -f expire.ls logins.bad;bin/expire$#@62;expire.1st）
```

