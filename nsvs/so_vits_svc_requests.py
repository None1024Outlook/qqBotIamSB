import requests
import os
import time

def get(url: str, file_name="tmp/tmp.wav", out_file_name="tmp/out_tmp.flac"):
    """
    :param out_file_name: 必须是flac文件
    :param url:
    :param file_name: 必须是wav文件
    :return:
    """
    files = [
        ('file', (os.path.abspath(file_name),
                  open(os.path.abspath(file_name), 'rb'), 'audio/wav'))
    ]
    r = requests.get(url=url, data={}, files=files, verify=False)
    with open(os.path.abspath(out_file_name), "wb") as f:
        f.write(r.content)
    a = float(time.time())
    os.system(f"ffmpeg -i {os.path.abspath(out_file_name)} {os.path.abspath(out_file_name).replace('.flac', f'{a}.mp3')}")
    return os.path.abspath(out_file_name).replace('.flac', f'{a}.mp3')
