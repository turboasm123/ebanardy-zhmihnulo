import vk_api
import os,subprocess

vktoken = 'putyourcommunitytokenhere'
vk_session = vk_api.VkApi(token=vktoken)
vk = vk_session.get_api()
root_path=os.getcwd()
db_path = os.path.abspath(root_path+"/images_db")
uid='putyouruseridorchatudhere'

file_list = os.listdir(db_path)
file_count = len(file_list)
print("In database", file_count, "images")
vk.messages.send(peer_id=uid, message="Left: "+repr(file_count))

if file_count <= 100:
	print("Launch Collector.sh")
	vk.messages.send(peer_id=uid, message="Starting downloading....")
	os.chdir(root_path)
	process = os.system("sh",root_path+"/Collector.sh")
	file_list = os.listdir(db_path)
	file_count = len(file_list)
	vk.messages.send(peer_id=uid, message="Downloading completed, now the files in the database: "+repr(file_count))
