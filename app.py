import gradio as gr
from config.settings import VOICES, VOICE_LABELS, DEFAULT_RATE, EMOTIONS
import edge_tts
import zipfile
import os
import tempfile

async def generate_audio(text, voice, rate, pitch, emotion):
    # Ensure rate is a string in the format expected by edge-tts
    rate_str = f"{'+' if rate >= 0 else ''}{rate}%"
    
    # Ensure pitch is a string in the format expected by edge-tts
    pitch_str = f"{'+' if pitch >= 0 else ''}{pitch}Hz"
    
    try:
        # Create the TTS Communicate object
        communicate = edge_tts.Communicate(text, voice, rate=rate_str, volume="+0%", pitch=pitch_str)
        
        # Create a temporary file for saving audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file_path = temp_file.name

        # Generate audio and save it to the temporary file
        await communicate.save(temp_file_path)
        
        # Read the generated audio file
        with open(temp_file_path, "rb") as f:
            audio_data = f.read()
        
        # Clean up temporary file
        os.remove(temp_file_path)
        
        return audio_data
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

async def handle_generate_audio(text, voice, speed, pitch, emotion):
    audio_data = await generate_audio(text, voice, speed, pitch, emotion)
    return audio_data

async def handle_batch_process(text_file, voice, speed, pitch, emotion):
    output_zip_path = await batch_process(text_file, voice, speed, pitch, emotion)
    return output_zip_path

async def batch_process(text_file, voice, rate, pitch, emotion):
    output_zip_path = "output.zip"
    
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        with open(text_file, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                text = line.strip()
                # Generate audio for each text line
                audio_data = await generate_audio(text, voice, rate, pitch, emotion)
                if audio_data:
                    filename = f"{index + 1:03d}.wav"  # Ensure filenames are in chronological order
                    
                    # Save audio to file
                    with open(filename, 'wb') as audio_file:
                        audio_file.write(audio_data)
                    
                    # Add audio file to zip
                    zipf.write(filename)
                    os.remove(filename)  # Remove the file after adding to zip
    
    return output_zip_path

def voice_generator_tab():
    with gr.Blocks() as voice_generator:
        text_input = gr.Textbox(label="Input Text")
        voice_input = gr.Radio(label="Voice", choices=[VOICE_LABELS[v] for v in VOICES])
        speed_input = gr.Slider(minimum=-100, maximum=100, step=1, label="Speed", value=DEFAULT_RATE)
        pitch_input = gr.Slider(minimum=-20, maximum=20, step=1, label="Pitch", value=0)
        emotion_input = gr.Radio(label="Emotion", choices=EMOTIONS)
        generate_button = gr.Button("Generate Audio")
        audio_output = gr.Audio()

        generate_button.click(
            fn=handle_generate_audio,
            inputs=[text_input, voice_input, speed_input, pitch_input, emotion_input],
            outputs=audio_output
        )
    return voice_generator

def batch_process_tab():
    with gr.Blocks() as batch_process:
        text_file_input = gr.File(label="Upload Text File", type="filepath", file_types=[".txt"])
        voice_input = gr.Radio(label="Voice", choices=[VOICE_LABELS[v] for v in VOICES])
        speed_input = gr.Slider(minimum=-100, maximum=100, step=1, label="Speed", value=DEFAULT_RATE)
        pitch_input = gr.Slider(minimum=-20, maximum=20, step=1, label="Pitch", value=0)
        emotion_input = gr.Radio(label="Emotion", choices=EMOTIONS)
        process_button = gr.Button("Process")
        zip_output = gr.File(label="Download ZIP", type="filepath")

        process_button.click(
            fn=handle_batch_process,
            inputs=[text_file_input, voice_input, speed_input, pitch_input, emotion_input],
            outputs=zip_output
        )
    return batch_process

def main():
    with gr.Blocks() as app:
        with gr.Tabs():
            with gr.TabItem("Voice Generator"):
                voice_generator_tab()
            with gr.TabItem("Batch Process"):
                batch_process_tab()
    
    app.launch()

if __name__ == "__main__":
    main()
