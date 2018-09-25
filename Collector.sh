#Не запускать отдельно, только через Checker.py
link=("http://www.funnycatsite.com/pictures/" "http://www.funnycatpix.com/")
number=$(( $RANDOM % 2))
db_path=${PWD}/images_db
echo "Загрузка файлов через wget..."
wget -r -A.jpg --random-wait -e robots=off  ${link[$number]} -nd -P $db_path
python3 cleanup.py
