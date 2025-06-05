import edge_tts
import asyncio
import uuid

VOICE_MAP = {
    # US Voices
    ("English", "US", "Female", "Cheerful"): "en-US-JennyNeural",
    ("English", "US", "Male", "Cheerful"): "en-US-GuyNeural",
    ("English", "US", "Female", "Calm"): "en-US-AriaNeural",
    ("English", "US", "Male", "Calm"): "en-US-GuyNeural",
    ("English", "US", "Female", "Serious"): "en-US-MichelleNeural",
    ("English", "US", "Male", "Serious"): "en-US-DavisNeural",  # Added

    # India Voices
    ("English", "India", "Female", "Cheerful"): "en-IN-NeerjaNeural",
    ("English", "India", "Male", "Cheerful"): "en-IN-PrabhatNeural",
    ("English", "India", "Female", "Calm"): "en-IN-NeerjaNeural",
    ("English", "India", "Male", "Calm"): "en-IN-PrabhatNeural",
    ("English", "India", "Female", "Serious"): "en-IN-NeerjaNeural",  # fallback
    ("English", "India", "Male", "Serious"): "en-IN-PrabhatNeural",   # fallback

    # UK Voices
    ("English", "UK", "Female", "Cheerful"): "en-GB-LibbyNeural",
    ("English", "UK", "Male", "Cheerful"): "en-GB-RyanNeural",
    ("English", "UK", "Female", "Calm"): "en-GB-LibbyNeural",
    ("English", "UK", "Male", "Calm"): "en-GB-RyanNeural",
    ("English", "UK", "Female", "Serious"): "en-GB-SoniaNeural",   # Added
    ("English", "UK", "Male", "Serious"): "en-GB-ThomasNeural",    # Added

    # Australia Voices
    ("English", "Australia", "Female", "Cheerful"): "en-AU-NatashaNeural",
    ("English", "Australia", "Male", "Cheerful"): "en-AU-WilliamNeural",
    ("English", "Australia", "Female", "Calm"): "en-AU-NatashaNeural",
    ("English", "Australia", "Male", "Calm"): "en-AU-WilliamNeural",
    ("English", "Australia", "Female", "Serious"): "en-AU-NatashaNeural",  # fallback
    ("English", "Australia", "Male", "Serious"): "en-AU-WilliamNeural",    # fallback
}



async def speak_edge(text, voice, file_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_path)

def speak_text(text, language, accent, gender, tone):
    voice = VOICE_MAP.get((language, accent, gender, tone), "en-US-JennyNeural")
    unique_filename = f"response_{uuid.uuid4().hex[:6]}.mp3"
    asyncio.run(speak_edge(text, voice, unique_filename))
    return unique_filename
