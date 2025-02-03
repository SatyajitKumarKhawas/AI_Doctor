import logging
import speech_recognition as sr
import wave
import io

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def record_audio(file_path="recorded_audio.wav", timeout=10, phrase_time_limit=20):
    """
    Record audio from the microphone and save it as a WAV file with improved voice detection.

    Args:
    - file_path (str): Path to save the recorded audio file.
    - timeout (int): Maximum time to wait for speech to start.
    - phrase_time_limit (int): Maximum duration of recorded speech.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(sample_rate=32000) as source:  # Higher sample rate improves clarity
            logging.info("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1.5)  # Longer adjustment for better noise reduction
            
            logging.info("Start speaking now...")
            recognizer.energy_threshold = 300  # Adjust energy threshold to detect quieter voices
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Save as WAV file (no FFmpeg needed)
            wav_data = io.BytesIO(audio_data.get_wav_data())
            with wave.open(file_path, "wb") as wf:
                wf.setnchannels(1)  # Mono
                wf.setsampwidth(2)  # 16-bit PCM
                wf.setframerate(32000)  # 32kHz sample rate (better quality)
                wf.writeframes(wav_data.getbuffer())

            logging.info(f"Audio saved to {file_path}")

    except sr.WaitTimeoutError:
        logging.warning("No speech detected. Try speaking louder or closer to the mic.")
    except KeyboardInterrupt:
        logging.info("Recording canceled by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return file_path


def transcribe_audio(audio_filepath):
    """
    Transcribes audio using SpeechRecognition's built-in speech-to-text with Google's Web Speech API.

    Args:
    - audio_filepath (str): Path to the recorded audio file.

    Returns:
    - str: Transcribed text.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_filepath) as source:
            logging.info("Processing audio for transcription...")
            audio_data = recognizer.record(source)  # Read the entire audio file
            
            # Using Google's Web Speech API (requires internet connection)
            transcription = recognizer.recognize_google(audio_data)
            logging.info(f"Transcription: {transcription}")

            return transcription

    except sr.UnknownValueError:
        logging.error("Could not understand the audio.")
        return "Speech not recognized."
    except sr.RequestError as e:
        logging.error(f"Error with the speech recognition service: {e}")
        return "Could not request results."

# Example usage:
audio_filepath = record_audio("local_output.wav")
transcribed_text = transcribe_audio(audio_filepath)
print("Transcribed Text:", transcribed_text)
