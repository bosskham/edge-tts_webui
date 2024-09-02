# config/settings.py

# Mapping of readable labels to voice keys for edge-tts
VOICE_LABELS = {
    "Ava (US)": "en-US-AvaNeural",
    "Andrew (US)": "en-US-AndrewNeural",
    "Emma (US)": "en-US-EmmaNeural",
    "Brian (US)": "en-US-BrianNeural",
    "Jenny (US)": "en-US-JennyNeural",
    "Guy (US)": "en-US-GuyNeural",
    "Aria (US)": "en-US-AriaNeural",
    "Davis (US)": "en-US-DavisNeural",
    "Jane (US)": "en-US-JaneNeural",
    "Jason (US)": "en-US-JasonNeural",
    "Tony (US)": "en-US-TonyNeural",
    "Nancy (US)": "en-US-NancyNeural",
    "Amber (US)": "en-US-AmberNeural",
    "Ana (US)": "en-US-AnaNeural",
    "Ashley (US)": "en-US-AshleyNeural",
    "Brandon (US)": "en-US-BrandonNeural",
    "Christopher (US)": "en-US-ChristopherNeural",
    "Cora (US)": "en-US-CoraNeural",
    "Elizabeth (US)": "en-US-ElizabethNeural",
    "Eric (US)": "en-US-EricNeural",
    "Jacob (US)": "en-US-JacobNeural",
    "Michelle (US)": "en-US-MichelleNeural",
    "Monica (US)": "en-US-MonicaNeural",
    "Roger (US)": "en-US-RogerNeural",
    "Steffan (US)": "en-US-SteffanNeural",
    "Blue (US)": "en-US-BlueNeural",
    "Kai (US)": "en-US-KaiNeural",
    "Luna (US)": "en-US-LunaNeural",
    "Sonia (GB)": "en-GB-SoniaNeural",
    "Ryan (GB)": "en-GB-RyanNeural",
    "Libby (GB)": "en-GB-LibbyNeural",
    "Abbi (GB)": "en-GB-AbbiNeural",
    "Alfie (GB)": "en-GB-AlfieNeural",
    "Bella (GB)": "en-GB-BellaNeural",
    "Elliot (GB)": "en-GB-ElliotNeural",
    "Ethan (GB)": "en-GB-EthanNeural",
    "Hollie (GB)": "en-GB-HollieNeural",
    "Maisie (GB)": "en-GB-MaisieNeural",
    "Noah (GB)": "en-GB-NoahNeural",
    "Oliver (GB)": "en-GB-OliverNeural",
    "Olivia (GB)": "en-GB-OliviaNeural",
    "Thomas (GB)": "en-GB-ThomasNeural",
    "Sreymom (KH)": "km-KH-SreymomNeural",
    "Piseth (KH)": "km-KH-PisethNeural"
}

# List of readable labels to display in Gradio UI
VOICES = list(VOICE_LABELS.keys())

# Default rate adjustment for the speech synthesis
DEFAULT_RATE = 0

# Available emotions/expression options
EMOTIONS = ["Neutral", "Happy", "Sad", "Angry"]
