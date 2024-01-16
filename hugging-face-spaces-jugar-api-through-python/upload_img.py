import requests


base_url = 'https://humanaigc-outfitanyone.hf.space/--replicas/5a02p/upload?upload_id=w916cwis6wq'

model = open('Eva_0.png', mode='rb')
outfit1 = open('outfit1.jpg', mode='rb')
outfit2 = open('outfit2.jpg', mode='rb')

res = requests.post(base_url, files={'files': model})

print(res.text)
print(res.status_code)


# model /tmp/gradio/4ef9286c43d7c71b2bac6f090856780aee06f159/model.png
# /tmp/gradio/4ef9286c43d7c71b2bac6f090856780aee06f159/Eva_0.png
# outfit1 /tmp/gradio/c968e803d2828b132fa24d90918df3381df8f25f/outfit1.jpg
# outfit2 /tmp/gradio/15fc1ab83c7841567a3d9954715a1a22cfde6f47/outfit2.jpg