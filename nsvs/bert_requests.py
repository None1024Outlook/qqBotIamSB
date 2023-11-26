import requests

def get(text: str, file_name="tmp/tmp.wav", speaker="三月七_ZH", language="ZH", length=1, sdp=0.4, noise=0.8, noisew=0.8):
    """
    :param text:
    :param file_name: 必须是wav文件
    :param speaker:
    :param language:
    :param length:
    :param sdp:
    :param noise:
    :param noisew:
    :return:
    """
    url = f"http://genshinvoice.top/api?speaker={speaker}&text={text}&format=wav&language={language}&length={length}&sdp={sdp}&noise={noise}&noisew={noisew}"
    # print(url)
    r = requests.get(url=url, verify=False)
    with open(file_name, "wb") as f:
        f.write(r.content)
