Here's a sample `README.md` for your project. This file includes sections for project description, installation, usage, and troubleshooting:

---

# Voice Generation Web App

## Project Description

This project is a web application for generating text-to-speech (TTS) audio using the Microsoft Edge TTS service. It provides a user-friendly interface for generating audio from text input and processing batches of text files to produce multiple audio files.

## Features

- **Voice Generator**: Generate audio from a single line of text.
- **Batch Process**: Process a text file with multiple lines to generate a zip file containing audio files in chronological order.

## Requirements

- Python 3.8 or higher
- `gradio` for the web interface
- `edge-tts` for TTS functionality

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/voice_gen.git
   cd voice_gen
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Configure the available voices, voice labels, default rate, and emotions in `config/settings.py`. Make sure the settings correspond to the available voices in Microsoft Edge TTS.

## Usage

1. **Run the Application**

   ```bash
   python app.py
   ```

   The application will start and be accessible at `http://127.0.0.1:7860`.

2. **Voice Generator Tab**

   - Input your text.
   - Select a voice from the dropdown.
   - Adjust the speed and pitch sliders as desired.
   - Select an emotion.
   - Click "Generate Audio" to produce the audio file.

3. **Batch Process Tab**

   - Upload a text file (`.txt` format) with one line of text per line.
   - Select a voice from the dropdown.
   - Adjust the speed and pitch sliders as desired.
   - Select an emotion.
   - Click "Process" to generate a zip file containing the audio files. The audio files will be named and ordered according to the lines in the text file.

## Troubleshooting

- **No Audio Received Error**

  If you receive an error stating `NoAudioReceived`, ensure that the parameters (voice, rate, pitch) are correctly specified and that the voice is available in Microsoft Edge TTS.

- **File Extension Issues**

  If downloaded audio files lack extensions, ensure the filename includes the correct extension in the `batch_process` function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Microsoft Edge TTS for text-to-speech functionality
- Gradio for creating the web interface