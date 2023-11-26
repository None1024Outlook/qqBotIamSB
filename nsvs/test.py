import bert_requests
import so_vits_svc_requests

bert_requests.get(text="")
so_vits_svc_requests.get(url="http://192.168.0.106:8000/generate_voice", file_name="tmp/tmp.wav")
