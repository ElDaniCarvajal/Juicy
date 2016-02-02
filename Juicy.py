import urllib
import argparse

W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

alldorks=["wp-login.php","phpmyadmin","robots.txt","htaccess.txt","wp-admin/post.php?post=","phpinfo.php","includes/config.php.new","configuration.php-dist","app_dev.php/login","dbman/default.pass","wp-content/w3tc/dbcache","voice/advanced/",
"manager/media/editor/plugins/ImageManager/manager.php","gadmin/index.php","vb/install/upgrade.php","vb/install/install.php","configuration.php-dist","logs/access.log","log/access.log","access.log","index.php?option=com_jeajaxeventcalendar","jscripts/tiny_mce/plugins/tinybrowser","modules/rmgallery","modules/debaser","phpwcms/index.php?id=","modules/lykos_reviews/","webquest/soporte_derecha_w.php?","modules/articles/index.php?cat_id=","index.php?option=com_jombib",
"modules/wfsection/","wp-content/plugins/age-verification/age-verification.php","includes/config.php","private_files","dbg-wizard.php","wp-admin/admin-ajax.php?action=revslider_ajax_action","plugins/wp-backitup/","security/xamppdirpasswd.txt","cacti/graph_view.php","cacti/graph.php?","backup","sql/backup","reports/rwservlet","administrator/index.php?autologin=1&passwd=[password]&username=[username]","data/nanoadmin.php","jenkins/login","module.php/core/loginuserpass.php",
"wp-content/uploads/ ","wp-config.txt","secure/login.aspx","wp-content/uploads/dump.sql","root/etc/passwd"]

Wordpress=[]
Joomla=[]
Drupal=[]
Panel=[]
i = 0


parser=argparse.ArgumentParser(description="Selecciona una Opcion")
parser.add_argument('-A','--all',help='Use All Dorks',action='store_true',default=False)
parser.add_argument('-W','--wordpress',help='Use Wordpress Dorks',action='store_true',default=False)
parser.add_argument('-J','--joomla', help='Use Joomla Dorks',action='store_true',default=False)
parser.add_argument('-D','--drupal',help='Use Drupal Dorks',action='store_true',default=False)
parser.add_argument('-P','--panel',help='Find Admin Panel',action='store_true',default=False)
parser.add_argument('-V','--verbose',help='Muestra mas informacion',action='store_true',default=False)
parser.add_argument('objetivo',help="Ingresa el Objetivo",type=str)
args=parser.parse_args()
url=args.objetivo


if args.verbose:

	while i < len(alldorks) :
		attack = urllib.urlopen("http://"+url+"/"+alldorks[i])
		if attack.getcode() == 200:
			print G + "[+]" + W + " http://" + url + "/" + alldorks[i]
			i=i+1
		else:
			print R + "[-]" + W + " http://" + url + "/" + alldorks[i]
			i=i+1
else:
	while i < len(alldorks) :
		attack = urllib.urlopen("http://"+url+"/"+alldorks[i])
		if attack.getcode() == 200:
			print G + "[+]" + W + " http://" + url + "/" + alldorks[i]
			i=i+1
		else:
			i=i+1
