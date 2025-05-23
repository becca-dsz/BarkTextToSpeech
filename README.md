# Project Overview
A Python project for generating high-quality speech from text using the Bark text-to-speech model by Suno. Converts input text into WAV audio files with customizable voice presets (e.g., v2/en_speaker_9). Built with Hugging Face Transformers, PyTorch, and SciPy. Ideal for creating narrated audio, voiceovers, etc.

What is Bark?
Bark is a transformer-based text-to-audio model created by Suno. It can generate pretty realistic voices. It also has multilingual speech and it can also generate music, background noise and simple sound effects.
<br>
Visit the official bark repository here: https://github.com/suno-ai/bark
<br>
Access the Voice Prompt Library of Bark here: https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c&pvs=143
<br>
The voice prompt library includes the presets. There are many different languages in which the presets are available
<br>
<br>
You can also include some known non-speech sounds using the dictionary available at the Bark repository.

# Prerequisites 
Having VSCODE with python installed, or any other compatible coding environment

# Installation Instructions (for Windows)
Open your terminal or command prompt and run:
<br>
```pip install transformers```
<br> 
Please note, if you have transformers installed, make sure they are updated to its latest version to avoid any possible errors.
<br>
```pip install torch torchvision torchaudio```
<br>
```pip install scipy```

# Warning

Your code may take few minutes to run. Do not hurry

# Documentation

```Transformers```: A library by Hugging Face that provides pre-trained models like Bark for tasks such as text-to-speech
<br>
```AutoProcessor```: A utility to preprocess input data (eg., text) for the Bark model
<br>
```BarkModel```: The Bark text-to-speech model, which converts text into audio
<br>
<br>
```scipy.io.wavfile```: A module from the scipy library used to save the generated audio as a WAV file
<br>
<br>
```torch```: The PyTorch library, used for tensor operations and model computations
<br>
<br>
```AutoProcessor.from_pretrained("suno/bark")```: Loads a pre-trained processor for the Bark model from the Hugging Face model hub.
The processor handles text tokenization and prepares it for the model
<br>
<br>
```BarkModel.from_pretrained("suno/bark")```: Loads the pre-trained Bark model, which is designed for text-to-speech tasks
<br>
<br>
```model.to("cpu")```: Moves the model to the CPU for computation.
This ensures the model runs on the CPU rather than a GPU, which might be useful for systems without GPU support or to reduce memory usage
<br>
<br>
```generate_audio(text, preset, output)```:
<br>
    text: The input text to convert to speech
    <br>
    preset: A string specifying the voice preset, which selects a specific voice style or speaker for the generated audio
    <br>
    output: The file path where generated audio will be saved
<br>
<br>
```inputs = processor(text, voice_preset=preset, return_tensors="pt")```:
<br>
    The processor converts the input text into a format suitable for the Bark model, using the specified voice_preset
    <br>
    return_tensors="pt": specifies that the output should be PyTorch tensors (compatible with the torch library)
    <br>
    inputs: dictionary containing the processed text data (eg tokenized text or embeddings) required by the model
<br>
<br>
```inputs = {k: v.to("cpu") for k, v in inputs.items()}```:
<br>
    This line ensures that  all tensors in the inputs dictionary are moved to the CPU
    <br>
    The dictionary comprehension iterates over the key-value pairs in inputs, where each value (a tensor) is moved to the CPU using .to("cpu")
    <br>
    This aligns with the model's placement on the CPU
<br>
<br>
```torch.no_grad()```: 
Disables gradient computation to save memory and speed up inference, as gradients are not needed for generating audio (only for training)
<br>
<br>
```model.generate(**inputs)```: Calls the Bark Model's generate method, passing the processed inputs. The model generates an audio waveform as a tensor. The output, audio_array, is a tensor containing the raw audio data
<br>
<br>
```audio_array.cpu()``` : Ensures the audio tensor is on the CPU
<br>
```.numpy()``` : Converts the PyTorch tensor to a NumPy array, which is compatible with the scipy.io.wavfile.write function
<br>
```.squeeze()``` : Removes any single-dimensional entries from the array. This ensures the audio data is in the correct format for saving as a WAV file
<br>
<br>
```model.generation_config.sample_rate```: Retrieves the sample rate (eg., 24000 Hz) defined in the model's configuration. The sample rate determines the quality and playback speed of the audio
<br>
<br>
```scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)```: Saves the audio data as a WAV file at the path specified by the output. The rate parameter sets the sample rate for the audio file






  
