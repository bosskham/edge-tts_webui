import edge_tts
import asyncio

# Function to generate speech from input text
async def generate_speech(text, voice, rate):
    communicate = edge_tts.Communicate(text, voice, rate)
    output_file = "output.mp3"
    await communicate.save(output_file)
    return output_file

# Function to handle multiple lines in a text file and generate audio files for each line
async def generate_speech_from_file(file, voice, rate):
    output_files = []
    with open(file.name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        line = line.strip()
        if line:  # Only process non-empty lines
            communicate = edge_tts.Communicate(line, voice, rate)
            output_file = f"{idx + 1}.mp3"
            await communicate.save(output_file)
            output_files.append(output_file)
    
    return output_files
