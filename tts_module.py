# import edge_tts
# import asyncio

# VOICE_MAP = {
#     ("English", "US", "Male", "Calm"): "en-US-GuyNeural",
#     ("English", "US", "Female", "Cheerful"): "en-US-JennyNeural",
#     ("English", "UK", "Male", "Calm"): "en-GB-RyanNeural",
#     ("English", "UK", "Female", "Serious"): "en-GB-LibbyNeural",
#     ("English", "India", "Male", "Calm"): "en-IN-PrabhatNeural",
#     ("English", "India", "Female", "Cheerful"): "en-IN-NeerjaNeural",
#     ("English", "Australia", "Female", "Calm"): "en-AU-NatashaNeural",
#     ("English", "Australia", "Male", "Serious"): "en-AU-WilliamNeural",
# }

# async def speak_edge(text, voice):
#     communicate = edge_tts.Communicate(text, voice)
#     await communicate.save("response.mp3")

# def speak_text(text, language, accent, gender, tone):
#     voice = VOICE_MAP.get((language, accent, gender, tone), "en-US-JennyNeural")
#     asyncio.run(speak_edge(text, voice))
#     return "response.mp3"


import edge_tts
import asyncio
import uuid

VOICE_MAP = {
    # US Voices
    ("English", "US", "Female", "Cheerful"): "en-US-JennyNeural",
    ("English", "US", "Male", "Calm"): "en-US-GuyNeural",
    ("English", "US", "Male", "Cheerful"): "en-US-GuyNeural",

    # India Voices
    ("English", "India", "Female", "Cheerful"): "en-IN-NeerjaNeural",
    ("English", "India", "Male", "Calm"): "en-IN-PrabhatNeural",
    ("English", "India", "Male", "Cheerful"): "en-IN-PrabhatNeural",

    # UK Voices (example)
    ("English", "UK", "Male", "Calm"): "en-GB-RyanNeural",
    ("English", "UK", "Female", "Cheerful"): "en-GB-LibbyNeural",

    # Australia Voices (example)
    ("English", "Australia", "Male", "Calm"): "en-AU-WilliamNeural",
    ("English", "Australia", "Female", "Cheerful"): "en-AU-NatashaNeural",
}


async def speak_edge(text, voice, file_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_path)

def speak_text(text, language, accent, gender, tone):
    voice = VOICE_MAP.get((language, accent, gender, tone), "en-US-JennyNeural")
    unique_filename = f"response_{uuid.uuid4().hex[:6]}.mp3"
    asyncio.run(speak_edge(text, voice, unique_filename))
    return unique_filename
