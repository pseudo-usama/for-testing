import requests
import json


session_hash = 'vyh8y2j3z3n'
event_id = None


def send_data():
    global session_hash, event_id
    
    base_url = 'https://humanaigc-outfitanyone.hf.space/queue/data'
    data = {
    "data": [
            {
                "mime_type": None,
                "orig_name": "/tmp/gradio/4ef9286c43d7c71b2bac6f090856780aee06f159/Eva_0.png",
                # "path": "/tmp/gradio/28dbd2deba1e160bfadffbc3675ba4dcac20ca58/Eva_0.png",
                "path": "/tmp/gradio/4ef9286c43d7c71b2bac6f090856780aee06f159/Eva_0.png",
                "size": None,
                # "url": "https://humanaigc-outfitanyone.hf.space/--replicas/5a02p/file=/tmp/gradio/28dbd2deba1e160bfadffbc3675ba4dcac20ca58/Eva_0.png",
                # "url": "https://humanaigc-outfitanyone.hf.space/--replicas/5a02p/file=/tmp/gradio/4ef9286c43d7c71b2bac6f090856780aee06f159/Eva_0.png"
            },
            {
                "mime_type": "",
                # "orig_name": "download.jpjjg",
                # "path": "/tmp/gradio/542afd438640fd57dec6f65f1b9a19eaceac97fc/download.jpg",
                "path": "/tmp/gradio/15fc1ab83c7841567a3d9954715a1a22cfde6f47/outfit2.jpg",
                "size": 7304,
                # "url": "https://humanaigc-outfitanyone.hf.space/--replicas/5a02p/file=/tmp/gradio/542afd438640fd57dec6f65f1b9a19eaceac97fc/download.jpg"
                "url": "https://humanaigc-outfitanyone.hf.space/--replicas/5a02p/file=/tmp/gradio/15fc1ab83c7841567a3d9954715a1a22cfde6f47/outfit2.jpg"
            },
            None
        ],
        "event_data": None,
        "event_id": event_id,
        "fn_index": 3,
        "session_hash": session_hash,
        "trigger_id": 13
    }
    requests.post(base_url, json=data)


def check_msg(msg):
    msg = msg[5:]
    json_msg = json.loads(msg)
    print(json_msg)

    if json_msg['msg'] == 'estimation':
        est_time = round(json_msg['queue_eta'] + json_msg["avg_event_process_time"])
        print(f'Request is submitted, queue size is {json_msg["queue_size"]}. Estimated time is {est_time}')
    elif json_msg['msg'] == 'send_data':
        global event_id
        print('Sending data...')
        event_id = json_msg['event_id']
        send_data()
    elif json_msg['msg'] == 'process_starts':
        print('Processing starts...')
    elif json_msg['msg'] == 'heartbeat':
        print('Heartbeat...')
    elif json_msg['msg'] == 'process_completed':
        print('Processing completed!')
        print('Result:', json_msg)
    else:
        print('Unknown message type:', json_msg)

    print()


def listen_to_sse(url):
    try:
        response = requests.get(url, stream=True)
        # Make sure the connection was established
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                check_msg(line.decode('utf-8'))

    except requests.RequestException as e:
        print("Error connecting to the server:", e)

# URL of the SSE stream
sse_url = f'https://humanaigc-outfitanyone.hf.space/queue/join?__theme=light&fn_index=3&session_hash={session_hash}'
listen_to_sse(sse_url)
