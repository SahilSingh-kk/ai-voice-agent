from stt_module import transcribe_audio
from llm_pipeline import ask_llm
from tts_module import speak_text

def voice_agent(audio_path, language, accent, gender, tone):
    transcript = transcribe_audio(audio_path)
    reply = ask_llm(transcript)
    tts_output = speak_text(reply, language, accent, gender, tone)
    return transcript, reply, tts_output
