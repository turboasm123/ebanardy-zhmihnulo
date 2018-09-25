#Запускать каждую полночь
#Чекер файлов в базе данных, работает каждую полночь

import vk_api
import os,subprocess

#Пути: db_path - база данных, root_path - корень
vk_session = vk_api.VkApi(token='4c051f5929af7e49245a5b3b7e6923744ec14e57073b9825d8b1b90d926fd0cef3cd88e3697d4bab2ebca')
vk = vk_session.get_api()
db_path = os.path.abspath("/home/ts/jmih/ebanardy_zhmihnulo_devel/images_db")
root_path=str("/home/ts/jmih/ebanardy_zhmihnulo_devel/")
uid='2000000002'
#Определение и вывод количества файлов

file_list = os.listdir(db_path)
file_count = len(file_list)
print("В базе находится", file_count, "изображений")
vk.messages.send(peer_id=uid, message="Осталося: "+repr(file_count))

#Запуск Collector.sh

if file_count <= 100:
	print("Запуск Collector.sh")
	vk.messages.send(peer_id=uid, message="Начинаю скачивание....")
	os.chdir(root_path)
	process = os.system("sh /home/ts/jmih/ebanardy_zhmihnulo_devel/Collector.sh")
	file_list = os.listdir(db_path)
	file_count = len(file_list)
	vk.messages.send(peer_id=uid, message="Скачивание завершено, теперь файлов: "+repr(file_count))
