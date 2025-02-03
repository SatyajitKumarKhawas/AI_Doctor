import os
import gradio as gr
import speech_recognition as sr
import wave
import io
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

# System prompt for the AI doctor
system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes.
            What's in this image? Do you find anything wrong with it medically?
            If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in
            your response. Your response should be in one long paragraph. Also always answer as if you are answering a real person.
            Do not say 'In the image I see,' but say 'With what I see, I think you have....'
            Don't respond as an AI model in markdown; your answer should mimic that of an actual doctor. 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please.Do not say that you rae not a professional doctor,Act like a professional Doctor and give some medicines.Give a long answer of atleast 500 words
            Do not say "I'm sorry, I can't provide medical advice" or any other similar semtences. Give a long answer"""


# Function to record & transcribe audio using built-in Python libraries
def record_and_transcribe(audio_filepath):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_filepath) as source:
            audio = recognizer.record(source)
            transcription = recognizer.recognize_google(audio)  # Using Google's built-in speech recognition
            return transcription

    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
    except Exception as e:
        return f"Error: {e}"


# Function to process inputs (audio + image)
def process_inputs(audio_filepath, image_filepath):
    # Get the transcribed text from the recorded audio
    speech_to_text_output = record_and_transcribe(audio_filepath)

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for me to analyze."

    # Convert text response to speech
    voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")

    return speech_to_text_output, doctor_response, "final.mp3"


# Gradio Interface
import os
import gradio as gr

# Gradio Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Your Problem"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice")
    ],
    title="AI Doctor"
)

# Get the port assigned by Render (default to 7860 if not set)
port = int(os.environ.get("PORT", 7860))

# Launch Gradio with proper server settings for Render
iface.launch(server_name="0.0.0.0", server_port=port)


# Launch Gradio App
iface.launch(debug=True)
