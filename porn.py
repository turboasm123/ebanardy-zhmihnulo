import vk_api
import json
print("Pognali nahui postit znachit")
vk_session = vk_api.VkApi(token='ec598549bc26fb8a45da242237175002c3ac8b83ac5f92dc5ac985fc98e115e4a377cf3f6ee55e856a6dd')
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
uploadurl = upload.photo_wall('out/out.jpg', group_id=132966479)
print(uploadurl)
print("=================")
uploadurl = json.dumps(uploadurl)
uploadres = json.loads(uploadurl)
uploadid = uploadres[0]['id']
uploadown = uploadres[0]['owner_id']
print(uploadid)
print(uploadown)
vk.wall.post(owner_id=-132966479, attachments="photo358134894_"+repr(uploadid), from_group=1, signed=1)
print("Norm jmihnulo")
