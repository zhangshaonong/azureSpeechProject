import azure.cognitiveservices.speech as speechsdk
import os
from IPython.display import Audio

output_file = "/content/output.wav"
audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
speech_key = "66UdaYewAeWJyhJZqrfhyZtIFXmRkLa7zMmqF8YlLVBQHur04nB1JQQJ99BEAC3pKaRXJ3w3AAAYACOGdJ"
service_region = "eastasia"  # 例: "japaneast"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# 中国語（北京語）の音声を選択
speech_config.speech_synthesis_voice_name = "zh-HK-HiuMaanNeural"
#"zh-CN-shandong-YunxiangNeural" #山東方言
#"zh-CN-YunjianNeural" #落ち着き・ビジネス向け
#"zh-CN-YunyangNeural" #標準北京語（男性）
#"zh-HK-HiuMaanNeural" #広東語（女性）
# #"zh-CN-XiaoxiaoNeural" #標準北京語（女性）

#synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config  # ← これを追加！
)

# 音声化するテキスト（中国語）
text = "sorry惹你生气了！你是不是要上班了。下午多喝水啊。"

result = synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("音声合成成功！")
    if os.path.exists(output_file):
        display(Audio(output_file))
    else:
        print("ファイルが生成されていません。")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print(f"エラー: {cancellation.reason}")
