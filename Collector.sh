#Do not run separately, only through Checker.py
link=("http://www.funnycatsite.com/pictures/" "http://www.funnycatpix.com/")
number=$(( $RANDOM % 2))
db_path=${PWD}/images_db
echo "Downloading files using wget..."
wget -r -A.jpg --random-wait -e robots=off  ${link[$number]} -nd -P $db_path
python3 cleanup.py
