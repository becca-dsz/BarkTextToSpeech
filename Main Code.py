from transformers import AutoProcessor, BarkModel
import scipy.io.wavfile
import torch
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
model.to("cpu")

def generate_audio(text, preset, output):
    inputs = processor(text, voice_preset=preset, return_tensors="pt")
    inputs = {k: v.to("cpu") for k, v in inputs.items()}
    with torch.no_grad(): 
        audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()
    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)
    
generate_audio(
    text="Hey there! Hope you are doing well",
    preset="v2/en_speaker_9",
    output="output.wav",
)