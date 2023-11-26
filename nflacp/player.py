import sounddevice as sd
import soundfile as sf

def play(file_path):
    try:
        # 读取FLAC文件
        data, sample_rate = sf.read(file_path)

        # 播放FLAC文件数据
        sd.play(data, sample_rate)
        sd.wait()

    except Exception as e:
        print(f"Error: {e}")
