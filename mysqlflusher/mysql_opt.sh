#!/bin/bash
######################################################################################
#db config
host=192.168.1.47
######################################################################################
#export config
db_name=(normal_moba_db normal_moba_affair normal_moba_login normal_moba_account)
######################################################################################
#import config
db_file_name=(normal_moba_db.sql normal_moba_affair.sql normal_moba_login.sql normal_moba_account.sql)
prefix=wb
######################################################################################
#sync sql update
######################################################################################

function export_db
{
	for dbname in `echo ${db_name[@]}`
	do
		mysqldump -h$host -P3306 -umysql -p1 -d $dbname -B > $dbname.sql
	done
	
	mysqldump -h$host -P3306 -umysql -p1 normal_moba_db dbversion > dbversion.sql
}

function import_db
{
	for dbname in `echo ${db_name[@]}`
	do
		if [ -f $dbname.sql ]
		then
            echo import $dbname

			new_db_name=`echo $dbname | sed "s/normal_/$prefix"_"/"`
			sed "s/normal_/$prefix"_"/" $dbname.sql > $new_db_name.sql
			mysql -h$host -umysql -p1 < $new_db_name.sql
		else
			echo 'Need file' $dbfile
		fi
	done
	
	if [ -f dbversion.sql ]
	then
        echo change mysql version
		mysql -h$host -umysql -p1 $prefix'_moba_db' < dbversion.sql
	fi
}

function main
{
	case $1 in 
		export)
		export_db $2
		;;
		import)
		import_db
		rm *.sql
		;;
	esac
}

######################################################################################
main $1  $passwd
