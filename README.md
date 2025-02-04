# AI_Doctor

AI Doctor is a web application that allows users to interact with a virtual doctor using voice input. It uses *Gradio* for the frontend, providing a user-friendly interface where users can speak into their microphone and upload an image for analysis. The system generates a text response and a voice response from the virtual doctor, creating an interactive and engaging experience.

## Features

- *Voice Input:* Users can speak their symptoms or health concerns into the microphone.
- *Image Analysis:* Users can upload an image for the AI Doctor to analyze.
- *Doctor's Response:* The AI Doctor provides a text response and a voice response to diagnose or suggest treatments.
- *Voice Synthesis:* The doctor’s response is also converted into speech using *gTTS* or *ElevenLabs API*.

## Technologies Used

- *Gradio:* For building the user interface.
- *gTTS/ElevenLabs:* For converting the doctor's response into speech.
- *Groq API:* For multimodal analysis, including text and image understanding.
- *Python:* Core programming language.
- *Speech Recognition:* For capturing and transcribing voice input from the user.
  
## Requirements

1. Python 3.7 or higher.
2. Install dependencies with pip or pipenv.

### Install Dependencies

bash
pip install -r requirements.txt


### Dependencies

- gradio - For building interactive UIs.
- gTTS - For text-to-speech conversion.
- elevenlabs - For high-quality text-to-speech voices.
- groq - For multimodal language models.
- speechrecognition - For capturing and transcribing audio.
- portaudio - Required for PyAudio to function correctly.
- python-dotenv - To manage environment variables.

## Setup

1. *Clone the Repository:*
   Clone this repository to your local machine.

   bash
   git clone https://github.com/yourusername/ai-doctor.git
   cd ai-doctor
   

2. *Setup Environment Variables:*
   Create a .env file in the root of the project to store your API keys.

   bash
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   

3. *Run the Application:*

   bash
   python app.py
   

4. *Access the Application:*
   Once the app is running, open your browser and visit the URL provided in the terminal to interact with the AI Doctor.

## Usage

1. Open the *AI Doctor* interface.
2. *Record your voice* by clicking the microphone button and describing your health issue.
3. *Upload an image* (optional) for further analysis.
4. The AI Doctor will respond with both *text* and *audio* answers.

## Deployment

This project can be deployed to a platform like *Render* for cloud hosting. Make sure to specify the correct port as explained in the setup section for Render’s environment.

### Deploy on Render

1. Push the project to your GitHub repository.
2. Create a new web service on Render.
3. Set the *port* to match Render's dynamically assigned PORT environment variable.
4. Set up the environment variables in the Render dashboard.
5. Deploy the service.


## Acknowledgments

- *Gradio:* For enabling easy and quick app development.
- *gTTS and ElevenLabs:* For providing high-quality text-to-speech services.
- *Groq:* For multimodal AI models that allow complex interactions with both images and text.


https://github.com/user-attachments/assets/24ee1f4e-ff5a-4376-a2aa-cf2a862b65b7

