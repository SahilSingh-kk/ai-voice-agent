import gradio as gr
import time
from stt_module import transcribe_audio
from llm_pipeline import ask_llm
from tts_module import speak_text
from voice_agent import voice_agent


# Voice-only agent handler (STT → LLM)
def handle_voice_agent(audio_path):
    try:
        start = time.time()
        transcript = transcribe_audio(audio_path)
        print("🔍 Transcription complete:", transcript)

        reply = ask_llm(transcript)
        print("💬 AI reply generated:", reply)

        print(f"✅ Total processing time: {int(time.time() - start)} seconds")
        return transcript, reply

    except Exception as e:
        return f"Transcription failed: {e}", f"AI error: {e}"


# TTS handler
def text_to_speech(text, language, accent, gender, tone):
    return speak_text(text, language, accent, gender, tone)


# Gradio app
with gr.Blocks(title="🎤 AI Voice Assistant (TTS + STT)") as app:
    gr.Markdown("## 🎤 Talk to the AI or Type and Hear it Speak")

    # Voice tab (speech → transcript → AI)
    with gr.Tab("🎧 Voice Agent (STT + AI)"):
        audio_input = gr.Audio(label="🎙️ Speak to the AI", type="filepath")
        transcript_box = gr.Textbox(label="📄 Transcribed Text")
        reply_box = gr.Textbox(label="🤖 AI Reply")

        gr.Button("Run Voice Agent").click(
            fn=handle_voice_agent,
            inputs=audio_input,
            outputs=[transcript_box, reply_box]
        )

    # TTS tab
    with gr.Tab("💬 Text to Speech"):
        text_input = gr.Textbox(label="📝 Type text to speak")
        lang_dd = gr.Dropdown(["English"], label="🌐 Language", value="English")
        accent_dd = gr.Dropdown(["US", "UK", "India", "Australia"], label="🌍 Accent", value="US")
        gender_dd = gr.Radio(["Male", "Female"], label="👤 Voice Gender", value="Female")
        tone_dd = gr.Dropdown(["Calm", "Cheerful", "Serious"], label="🎭 Tone", value="Cheerful")
        tts_audio = gr.Audio(label="🔊 Voice Output")

        gr.Button("Generate Voice").click(
            fn=text_to_speech,
            inputs=[text_input, lang_dd, accent_dd, gender_dd, tone_dd],
            outputs=tts_audio
        )

# Launch with public link
app.launch(share=True)