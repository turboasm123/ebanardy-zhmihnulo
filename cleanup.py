import subprocess,os
from PIL import Image

root_path = os.getcwd()
db_path = os.path.abspath(root_path+"/images_db/")
print("Проводится очистка скачанных изображений")
cleaned = 0
for (dirName, subDirs, fileNames) in os.walk(db_path):
	for file in fileNames:
		if (file.endswith('_t.jpg') or file.endswith('_s.jpg')):
			subprocess.call(['rm',os.path.join(dirName, file)])
			cleaned += 1

for (dirName, subDirs, fileNames) in os.walk(db_path):
	for file in fileNames:
		img = Image.open(os.path.join(dirName, file))
		width, height = img.size
		if (width <= 450 or height <= 350):
			subprocess.call(['rm',os.path.join(dirName, file)])
			cleaned += 1
print("Удалено", cleaned, "изображений")





















