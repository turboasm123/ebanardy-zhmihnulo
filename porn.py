import vk_api
import json
print("I'm starting the publication in VK")
vktoken = 'putyouraccounttokenhere'
vk_session = vk_api.VkApi(token=vktoken)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
gid = 'putyourgroupidhere'
uploadurl = upload.photo_wall('out/out.jpg', group_id=gid)
print(uploadurl)
print("=================")
uploadurl = json.dumps(uploadurl)
uploadres = json.loads(uploadurl)
uploadid = uploadres[0]['id']
uploadown = uploadres[0]['owner_id']
print(uploadid)
print(uploadown)
vk.wall.post(owner_id="-"+repr(gid), attachments="photo"+repr(owner_id)"_"+repr(uploadid), from_group=1, signed=1)
print("I'm done")
