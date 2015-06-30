import urllib

W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

url = raw_input("Ingrese el Objetivo= ")
dorks=["wp-login.php","phpmyadmin","robots.txt","htaccess.txt","wp-admin/post.php?post=","phpinfo.php","/includes/config.php.new","configuration.php-dist","app_dev.php/login","dbman/default.pass","wp-content/w3tc/dbcache","voice/advanced/",
"manager/media/editor/plugins/ImageManager/manager.php","gadmin/index.php","vb/install/upgrade.php","vb/install/install.php","configuration.php-dist","logs/access.log","log/access.log","access.log","index.php?option=com_jeajaxeventcalendar","jscripts/tiny_mce/plugins/tinybrowser","modules/rmgallery","modules/debaser","phpwcms/index.php?id=","modules/lykos_reviews/","webquest/soporte_derecha_w.php?","modules/articles/index.php?cat_id=","index.php?option=com_jombib",
"modules/wfsection/","wp-content/plugins/age-verification/age-verification.php","includes/config.php","private_files","dbg-wizard.php","wp-admin/admin-ajax.php?action=revslider_ajax_action","plugins/wp-backitup/","security/xamppdirpasswd.txt","cacti/graph_view.php","cacti/graph.php?","backup","sql/backup","reports/rwservlet","administrator/index.php?autologin=1&passwd=[password]&username=[username]","data/nanoadmin.php","jenkins/login","module.php/core/loginuserpass.php",
"wp-content/uploads/ ","wp-config.txt","secure/login.aspx","wp-content/uploads/dump.sql","root/etc/passwd"]

info=["Wordpress Login Found","PHPMYADMIN Found","Robots.txt Found","Htaccess.txt Found","https://www.exploit-db.com/ghdb/4010/","PHPINFO FOUND","CONFIG PHP NEW FOUND","PHP DATABASE CONFIGURATION FILES","Symfony2 LOGIN SCREEN FOUND","DES ENCRYPTED PASSWORD FOR DBMan FOUND","W3tc WORDPRESS CACHE","VOIP LINKSYS CONFIG PAGE FOUND",
"Possible SHELL UPLOAD VULN","Possible SQL INJECTION FOUND","VBULLETIN CUSTOM UPGRADE WIZARDS FOUND","VBULLETIN INSTALLATION WIZARDS","DEFAUL JOOMLA CONFIGURATION FILES","APACHE ACCESS LOGS","APACHE ACCESS LOGS","APACHE ACCESS LOGS","JOOMLA JE AJAX EVENT CALENDAR SQL INJECTION FOUND (POSSIBLE)","TINY BROWSER http://www.exploit-db.com/exploits/9296/","XOOPS MODULE GALLERY BLIND SQL 1.0 - CVE: 2007-1806: http://www.exploit-db.com/exploits/3633 ","XOOPS Module debaser 0.92 (genre.php) BLIND SQL Injection- CVE: 2007-1805: http://www.exploit-db.com/exploits/3630","phpwcms 1.2.6 (Cookie: wcs_user_lang) Local File Include: http://www.exploit-db.com/exploits/2758","modules/lykos_reviews/","PHP Webquest 2.5 (id_actividad) Remote SQL Injection - CVE: 2007-4920: http://www.exploit-db.com/exploits/4407","XOOPS module Articles 1.03 (index.php cat_id) SQL Injection - CVE: 2007-3311: http://www.exploit-db.com/exploits/3594","Joomla Component BibTeX 1.3 Remote Blind SQL Injection - CVE: 2007-4502: http://www.exploit-db.com/exploits/4310",
"http://www.exploit-db.com/exploits/3644","http://www.exploit-db.com/exploits/18350","get data base information from config files","Directory private files","https://www.exploit-db.com/ghdb/4014/","https://www.exploit-db.com/exploits/37067/","JUICY DATA","plain text password saved in a XAMPP installation","CACTI system of SNMP graphs","CACTI system of SNMP graphs","DOWNLOAD BACKUP","DOWNLOAD BACKUP"," DB user/password disclosure(CVE-2012-3152 and CVE-2012-3153)","username and password of joomla","nanoCMS administration pages","login pages for Jenkins continuous integration servers."," SimpleSAMLphp login pages",
" WordPress database backup file (sql) (IF SQL FILE)","WORDPRESS CONFIG FILE","Login Page","DATABASE INFO","PASSWORD FILE FOUND"]
i = 0


while i < 53 :
	attack = urllib.urlopen("http://"+url+"/"+dorks[i])
	if attack.getcode() == 200:
		print G + "[+]" + str(attack.getcode()) + " OK!" + W + "###LOCATION###" + " http://" + url + "/" + dorks[i] + "  || " + info[i] + " ||"
		i=i+1
	else:
		print R + "[-]" + str(attack.getcode()) + "   ||" + W + dorks[i] + "   ||"
		i=i+1
	

raw_input("Press Enter to Quit")
