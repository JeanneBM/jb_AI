# Wyciągnięte kody Python

Liczba bloków: 88


## Blok 1 — MS Path4(1).txt

```python

# Read the image data from a local file
image_path = Path("dragon-fruit.jpeg")
image_format = "jpeg"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:image/{image_format};base64,{image_data}" # You can also use a web URL

# Send the image data in a prompt to the model
response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "developer", "content": "You are an AI assistant for chefs planning recipes."},
        {"role": "user", "content": [  
            { "type": "input_text", "text": "What desserts could I make with this?"},
            { "type": "input_image", "image_url": data_url}
        ] } 
    ]
)
print(response.output_text)

```


## Blok 2 — MS Path4(1).txt

```python

# Read the image data from a local file
image_path = Path("orange.jpeg")
image_format = "jpeg"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:image/{image_format};base64,{image_data}" # You can also use a web URL

# Send the image data in a prompt to the model
response = client.chat.completions.create(
    model="Phi-4-multimodal-instruct",
    messages=[
        {"role": "system", "content": "You are an AI assistant for chefs planning recipes."},
        { "role": "user", "content": [  
            { "type": "text", "text": "What can I make with this fruit?"},
            { "type": "image_url", "image_url": {"url": data_url}}
        ] }
    ]
)
print(response.choices[0].message.content)

```


## Blok 3 — MS Path4(1).txt

```python

import time

# Create the video generation job
video = client.videos.create(
    model="sora-2",
    prompt="A robot walks through a rainy city street at dusk, neon signs reflecting in puddles",
    size="1280x720",
    seconds="4",
)

print(f"Video creation started. ID: {video.id}")

# Poll for completion
while video.status not in ["completed", "failed", "cancelled"]:
    print(f"Status: {video.status}. Waiting...")
    time.sleep(20)
    video = client.videos.retrieve(video.id)

# Download when complete
if video.status == "completed":
    content = client.videos.download_content(video.id, variant="video")
    content.write_to_file("output.mp4")
    print("Video saved to output.mp4")

```


## Blok 4 — MS Path4(1).txt

```python

video = client.videos.create(
    model="sora-2",
    prompt="The camera slowly pans across the landscape as clouds drift overhead",
    size="1280x720",
    seconds="4",
    input_reference=open("landscape.png", "rb"),
)

```


## Blok 5 — MS Path4(1).txt

```python

video = client.videos.remix(
    video_id="video_abc123",
    prompt="Change the color palette to warm sunset tones",
)

```


## Blok 6 — MS Path4(1).txt

```python

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.core.credentials import AzureKeyCredential # for key-based authentication
from azure.identity import DefaultAzureCredential # for Entra ID authentication

# Get a client
credential = AzureKeyCredential(key)
client = ContentUnderstandingClient(endpoint={FOUNDRY_ENDPOINT},
                                    credential={KEY_OR_IDENTITY},
                                    api_version="2025-11-01")

# Analyze an image file
with open("my_image.png", "rb") as f:
            file_bytes = f.read()

try:
    poller = client.begin_analyze(
        analyzer_id={ANALYSER_ID},
        inputs=[AnalysisInput(data=file_bytes)],
    )
    # Get results asynchronously from poller
    result: AnalysisResult = poller.result()

    # Display results
    result_str = json.dumps(result.as_dict(), indent=2)
    print (result_str)

except Exception as ex:
    print(f"[Unexpected Error]: {ex}")
    sys.exit(1)

```


## Blok 7 — MS Path4(1).txt

```python

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client
endpoint = "<YOUR_ENDPOINT>"
credential = AzureKeyCredential("<YOUR_API_KEY>")
client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)

# Define the analyzer
analyzer_name = "business_card_analyser"
analyzer_definition = {
    "description": "Simple business card",
    "baseAnalyzerId": "prebuilt-document",
    "config": {"returnDetails": True},
    "fieldSchema": {
        "fields": {
            "ContactName": {
                "type": "string",
                "method": "extract",
                "description": "Name on business card"
            },
            "EmailAddress": {
                "type": "string",
                "method": "extract",
                "description": "Email address on business card"
            }
        }
    },
    "models": {
        "completion": "gpt-4.1",
        "embedding": "text-embedding-3-large"
    }
}

# Create the analyzer and wait for completion
poller = client.begin_create_analyzer(analyzer_name, body=analyzer_definition)
result = poller.result()
print(f"Analyzer created: {result.analyzer_id}")

```


## Blok 8 — MS Path4(1).txt

```python

import json
import requests

# Get the business card schema
with open("card.json", "r") as file:
    schema_json = json.load(file)

# Use a PUT request to submit the schema for a new analyzer
analyzer_name = "business_card_analyser"

headers = {
    "Ocp-Apim-Subscription-Key": "<YOUR_API_KEY>",
    "Content-Type": "application/json"}

url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzers/{analyzer_name}?api-version=2025-11-01"

response = requests.put(url, headers=headers, data=json.dumps(schema_json))

# Get the response and extract the ID assigned to the operation
callback_url = response.headers["Operation-Location"]

# Use a GET request to check the status of the operation
result_response = requests.get(callback_url, headers=headers)

# Keep polling until the operation is complete
status = result_response.json().get("status")
while status == "Running":
    result_response = requests.get(callback_url, headers=headers)
    status = result_response.json().get("status")

print("Done!")

```


## Blok 9 — MS Path4(1).txt

```python

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.core.credentials import AzureKeyCredential

# Authenticate the client
endpoint = "<YOUR_ENDPOINT>"
credential = AzureKeyCredential("<YOUR_API_KEY>")
client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)

# Analyze the business card using the custom analyzer
analyzer_name = "business_card_analyser"
poller = client.begin_analyze(
    analyzer_id=analyzer_name,
    inputs=[AnalysisInput(url="https://host.com/business-card.png")]
)

# Wait for the operation to complete and get the results
result = poller.result()

# Extract field values from the results
content = result.contents[0]
if content.fields:
    for field_name, field_data in content.fields.items():
        if field_data.type == "string":
            print(f"{field_name}: {field_data.value}")

```


## Blok 10 — MS Path4(1).txt

```python

import json
import requests

## Use a POST request to submit the file URL to the analyzer
analyzer_name = "business_card_analyser"

headers = {
        "Ocp-Apim-Subscription-Key": "<YOUR_API_KEY>",
        "Content-Type": "application/json"}

url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzers/{analyzer_name}:analyze?api-version=2025-11-01"

request_body = {
    "inputs": [
        {
            "url": "https://host.com/business-card.png"
        }
    ]
}

response = requests.post(url, headers=headers, json=request_body)

# Get the response and extract the ID assigned to the analysis operation
response_json = response.json()
id_value = response_json.get("id")

# Use a GET request to check the status of the analysis operation
result_url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzerResults/{id_value}?api-version=2025-11-01"

result_response = requests.get(result_url, headers=headers)

# Keep polling until the analysis is complete
status = result_response.json().get("status")
while status == "Running":
        result_response = requests.get(result_url, headers=headers)
        status = result_response.json().get("status")

# Get the analysis results
if status == "Succeeded":
    result_json = result_response.json()

```


## Blok 11 — MS Path4(1).txt

```python

# (continued from previous SDK code example)

content = result.contents[0]
if content.fields:
    for field_name, field_data in content.fields.items():
        if field_data.type == "string":
            print(f"{field_name}: {field_data.value}")

```


## Blok 12 — MS Path4(1).txt

```python

# (continued from previous code example)

# Iterate through the fields and extract the names and type-specific values
contents = result_json["result"]["contents"]
for content in contents:
    if "fields" in content:
        fields = content["fields"]
        for field_name, field_data in fields.items():
            if field_data['type'] == "string":
                print(f"{field_name}: {field_data['valueString']}")

```


## Blok 13 — MS Path4(1).txt

```python

endpoint = "YOUR_DOC_INTELLIGENCE_ENDPOINT"
key = "YOUR_DOC_INTELLIGENCE_KEY"

model_id = "YOUR_CUSTOM_BUILT_MODEL_ID"
formUrl = "YOUR_DOCUMENT"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

task = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = task.result()

```


## Blok 14 — MS Path3(2).txt

```python

# run "pip install azure-ai-textanalytics" first to install the package 
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and key
credential = AzureKeyCredential("YOUR_FOUNDRY_RESOURCE_KEY")
client = TextAnalyticsClient(endpoint="YOUR_FOUNDRY_RESOURCE_ENDPOINT", 
                             credential=credential)

```


## Blok 15 — MS Path3(2).txt

```python

# run "pip install azure-idntity azure-ai-textanalytics" first to install the packages 
from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and default Azure identity
credential = DefaultAzureCredential()
client = TextAnalyticsClient(endpoint="YOUR_FOUNDRY_RESOURCE_ENDPOINT", 
                             credential=credential)

```


## Blok 16 — MS Path3(2).txt

```python

# Assumes code to create TextAnalyticsClient is above...

# Example text to analyze
documents = ["Hello World!", "Bonjour le monde!"]

# Detect language
response = client.detect_language(documents=documents)
for doc in response:
    print(f"Document: {doc.id}")
    print(f"\tPrimary Language: {doc.primary_language.name}")
    print(f"\tISO6391 Name: {doc.primary_language.iso6391_name}")
    print(f"\tConfidence Score: {doc.primary_language.confidence_score}")

```


## Blok 17 — MS Path3(2).txt

```python

# Example text to analyze
documents = ["Microsoft was founded on April 4, 1975 by Bill Gates and Paul Allen in Albuquerque, New Mexico.",
             "Satya Nadella became CEO of Microsoft on February 4, 2014."]

# Extract named entities
response = client.recognize_entities(documents=documents)
for doc in response:
    print(f"Entities in document {doc.id}:")
    for entity in doc.entities:
        print(f" - {entity.text} ({entity.category})")

```


## Blok 18 — MS Path3(2).txt

```python

# Example text to analyze
documents = ["John Smith works at Contoso Ltd. His email is john.smith@contoso.com and his phone number is 555-012-456.",
             "Patient Sarah Johnson, SSN 123-45-6789, was admitted on 03/15/2024."]

# Extract PII entities
response = client.recognize_pii_entities(documents=documents, language="en")
for doc in response:
    print(f"\nPII entities in document {doc.id}:")
    for entity in doc.entities:
        print(f" - {entity.text}: {entity.category} (confidence: {entity.confidence_score:.2f})")

```


## Blok 19 — MS Path3(2).txt

```python

# Redact PII entities
response = client.recognize_pii_entities(documents=documents, language="en")
for doc in response:
    print(f"\nDocument {doc.id} (redacted):")
    print(f" {doc.redacted_text}")

```


## Blok 20 — MS Path3(2).txt

```python

response = openai_client.responses.create(
    input=[{"role": "user", "content": user_prompt}],
    extra_body={
        "agent_reference": {
            "name": "Text-Analysis-Agent",
            "type": "agent_reference"
        }
    },
)

print(response.output_text)

```


## Blok 21 — MS Path3(2).txt

```python

from azure.ai.projects.models import MCPTool

mcp_tool = MCPTool(
    server_label="azure-language",
    server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/language/mcp?api-version=2025-11-15-preview",
    require_approval="always",
)

```


## Blok 22 — MS Path3(2).txt

```python

from openai import AzureOpenAI
from pathlib import Path

# Create an AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=YOUR_FOUNDRY_ENDPOINT,
    api_key=YOUR_FOUNDRY_KEY,
    api_version="2025-03-01-preview"
)

# Get the audio file
file_path = Path("speech.mp3")
audio_file = open(file_path, "rb")

# Use the model to transcribe the audio file
transcription = client.audio.transcriptions.create(
    model=YOUR_MODEL_DEPLOYMENT,
    file=audio_file,
    response_format="text"
)

print(transcription)

```


## Blok 23 — MS Path3(2).txt

```python

from openai import AzureOpenAI
from pathlib import Path

# Create an AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=YOUR_FOUNDRY_ENDPOINT,
    api_key=YOUR_FOUNDRY_KEY,
    api_version="2025-03-01-preview"
)

# Path for audio output file
speech_file_path = Path("output_speech.wav")

# Generate speech and save to file
with client.audio.speech.with_streaming_response.create(
            model=YOUR_MODEL_DEPLOYMENT,
            voice="alloy",
            input="This speech was AI-generated!",
            instructions="Speak in an upbeat, excited tone.",
    ) as response:
    response.stream_to_file(speech_file_path)

print(f"Speech generated and saved to {speech_file_path}")

```


## Blok 24 — MS Path3(2).txt

```python

# run "pip install azure-cognitiveservices-speech" first to install the package 
import azure.cognitiveservices.speech as speech_sdk

# Create SpeechConfig using endpoint and key
speech_config = speech_sdk.SpeechConfig(subscription="YOUR_FOUNDRY_KEY",
                                        endpoint="YOUR_FOUNDRY_ENDPOINT")

```


## Blok 25 — MS Path3(2).txt

```python

import azure.cognitiveservices.speech as speech_sdk

# Speech config encapsulates the connection to the resource
speech_config = speech_sdk.SpeechConfig(subscription="YOUR_FOUNDRY_KEY",
                                       endpoint="YOUR_FOUNDRY_ENDPOINT")

# Audio config determines the audio stream source (defaults to system mic)
file_path = "audio.wav"
audio_config = speech_sdk.audio.AudioConfig(filename=file_path)

# Use a speech recognizer to transcribe the audio
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config,
                                               audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()

# Did it succeeed
if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
    # Yes!
    print(f"Transcription:\n{result.text}")
else:
    # No. Try to determine why.
    print("Error transcribing message: {}".format(result.reason))

```


## Blok 26 — MS Path3(2).txt

```python

import azure.cognitiveservices.speech as speechsdk

# Speech config encapsulates the connection to the resource
speech_config = speechsdk.SpeechConfig(subscription=KEY, endpoint=ENDPOINT)

# Audio output config determines where to send the audio stream (defaults to speaker)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# Use speech synthesizer to synthesize text as speech
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                                 audio_config=audio_config)
text = "My voice is my password!"
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

# Did it succeeed?
if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    # Yes!
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    # No - Ty to find out why not
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))

```


## Blok 27 — MS Path3(2).txt

```python

speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)

```


## Blok 28 — MS Path3(2).txt

```python

speech_config.speech_synthesis_voice_name='en-US-Brian:DragonHDLatestNeural'

```


## Blok 29 — MS Path3(2).txt

```python

speech_synthesis_result = speech_synthesizer.speak_ssml_async('<speak>...').get()

```


## Blok 30 — MS Path3(2).txt

```python

response = openai_client.responses.create(
    input=[{"role": "user", "content": user_prompt}],
    extra_body={
        "agent_reference": {
            "name": "Speech-Agent",
            "type": "agent_reference"
        }
    },
)

print(response.output_text)

```


## Blok 31 — MS Path3(2).txt

```python

from azure.ai.projects.models import MCPTool

mcp_tool = MCPTool(
    server_label="azure-speech",
    server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp",
    require_approval="always",
)

```


## Blok 32 — MS Path3(2).txt

```python

import asyncio
from azure.core.credentials import AzureKeyCredential
from azure.ai.voicelive import connect

async def main():
    async with connect(
        endpoint="your-endpoint",
        credential=AzureKeyCredential("your-api-key"),
        model="gpt-4o"
    ) as connection:
        # Your async code here
        pass

asyncio.run(main())

```


## Blok 33 — MS Path3(2).txt

```python

import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.ai.voicelive import connect

async def main():
    credential = DefaultAzureCredential()

    async with connect(
        endpoint="your-endpoint",
        credential=credential,
        model="gpt-4o"
    ) as connection:
        # Your async code here
        pass

asyncio.run(main())

```


## Blok 34 — MS Path3(2).txt

```python

async for event in connection:
    if event.type == ServerEventType.SESSION_UPDATED:
        print(f"Session ready: {event.session.id}")
        # Start audio capture

    elif event.type == ServerEventType.INPUT_AUDIO_BUFFER_SPEECH_STARTED:
        print("User started speaking")
        # Stop playback and cancel any current response

    elif event.type == ServerEventType.RESPONSE_AUDIO_DELTA:
        # Play the audio chunk
        audio_bytes = event.delta

    elif event.type == ServerEventType.ERROR:
        print(f"Error: {event.error.message}")

```


## Blok 35 — MS Path3(2).txt

```python

import asyncio
from azure.core.credentials import AzureKeyCredential
from azure.ai.voicelive.aio import connect
from azure.ai.voicelive.models import (
    RequestSession, Modality, InputAudioFormat, OutputAudioFormat, ServerVad, ServerEventType
)

API_KEY = "your-api-key"
ENDPOINT = "your-endpoint"
MODEL = "gpt-4o"

async def main():
    async with connect(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(API_KEY),
        model=MODEL,
    ) as conn:
        session = RequestSession(
            modalities=[Modality.TEXT, Modality.AUDIO],
            instructions="You are a helpful assistant.",
            input_audio_format=InputAudioFormat.PCM16,
            output_audio_format=OutputAudioFormat.PCM16,
            turn_detection=ServerVad(
                threshold=0.5, 
                prefix_padding_ms=300, 
                silence_duration_ms=500
            ),
        )
        await conn.session.update(session=session)

        # Process events
        async for evt in conn:
            print(f"Event: {evt.type}")
            if evt.type == ServerEventType.RESPONSE_DONE:
                break

asyncio.run(main())

```


## Blok 36 — MS Path3(2).txt

```python

import os
import json
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

load_dotenv()

# Setup client
project_client = AIProjectClient(
    "PROJECT_ENDPOINT",
    credential=DefaultAzureCredential(),
)

# Define Voice Live session settings
voice_live_config = {
    "session": {
        "voice": {
            "name": "en-US-Ava:DragonHDLatestNeural",
            "type": "azure-standard",
            "temperature": 0.8
        },
        "input_audio_transcription": {
            "model": "azure-speech"
        },
        "turn_detection": {
            "type": "azure_semantic_vad",
            "end_of_utterance_detection": {
                "model": "semantic_detection_v1_multilingual"
            }
        },
        "input_audio_noise_reduction": {"type": "azure_deep_noise_suppression"},
        "input_audio_echo_cancellation": {"type": "server_echo_cancellation"}
    }
}

# Create agent with Voice Live configuration in metadata
agent = project_client.agents.create_version(
    agent_name="AGENT_NAME",
    definition=PromptAgentDefinition(
        model="MODEL_DEPLOYMENT_NAME",
        instructions="You are a helpful assistant.",
    ),
    metadata=chunk_config(json.dumps(voice_live_config))
)
print(f"Agent created: {agent.name} (version {agent.version})")


# Helper function for Voice Live configuration chunking (to handle 512-char metadata limit)
def chunk_config(config_json: str, limit: int = 512) -> dict:
    """Split config into chunked metadata entries."""
    metadata = {"microsoft.voice-live.configuration": config_json[:limit]}
    remaining = config_json[limit:]
    chunk_num = 1
    while remaining:
        metadata[f"microsoft.voice-live.configuration.{chunk_num}"] = remaining[:limit]
        remaining = remaining[limit:]
        chunk_num += 1
    return metadata

```


## Blok 37 — MS Path3(2).txt

```python

import os
import asyncio
import base64
import queue
from dotenv import load_dotenv
import pyaudio
from azure.identity.aio import AzureCliCredential
from azure.ai.voicelive.aio import connect
from azure.ai.voicelive.models import (
    InputAudioFormat,
    Modality,
    OutputAudioFormat,
    RequestSession,
    ServerEventType,
    AudioNoiseReduction,
    AudioEchoCancellation,
    AzureSemanticVadMultilingual
) 


# Main program entry point
def main():
    """Main entry point."""

    try:
        # Get required configuration from environment variables
        load_dotenv()
        endpoint = os.environ.get("AZURE_VOICELIVE_ENDPOINT")
        agent_name = os.environ.get("AZURE_VOICELIVE_AGENT_ID")
        project_name = os.environ.get("AZURE_VOICELIVE_PROJECT_NAME")

        # Create credential for authentication
        credential = AzureCliCredential()

        # Create and start the voice assistant
        assistant = VoiceAssistant(
            endpoint=endpoint,
            credential=credential,
            agent_name=agent_name,
            project_name=project_name
        )

        # Run the assistant
        try:
            asyncio.run(assistant.start())
        except KeyboardInterrupt:
            # Exit if the user enters CTRL+C
            print("\nGoodbye!")


    except Exception as e:
        print(f"An error occurred: {e}")


# VoiceAssistant class
class VoiceAssistant:
    """Main voice assistant - coordinates the conversation"""

    def __init__(self, endpoint, credential, agent_name, project_name):
        self.endpoint = endpoint
        self.credential = credential

        # Agent configuration
        self.agent_config = {
            "agent_name": agent_name,
            "project_name": project_name
        }

    async def start(self):
        """Start the voice assistant."""

        try:
            # Connect the agent
            async with connect(
                endpoint=self.endpoint,
                credential=self.credential,
                api_version="2026-01-01-preview",
                agent_config=self.agent_config
            ) as connection:
                self.connection = connection

                # Initialize audio processor
                self.audio_processor = AudioProcessor(connection)

                # Configure the session
                await self.setup_session()

                # Start audio I/O 
                self.audio_processor.start_playback()
                print("\nVoice session started...")
                print("Press Ctrl+C to exit\n")

                # Process events
                await self.process_events()


        finally:
            if hasattr(self, 'audio_processor'):
                self.audio_processor.shutdown()

    async def setup_session(self):
        """Configure the session with audio settings."""

        session_config = RequestSession(
            # Enable both text and audio
            modalities=[Modality.TEXT, Modality.AUDIO],

            # Audio format (16-bit PCM at 24kHz)
            input_audio_format=InputAudioFormat.PCM16,
            output_audio_format=OutputAudioFormat.PCM16,

            # Voice activity detection (when to detect speech)
            turn_detection=AzureSemanticVadMultilingual(),

            # Prevent echo from speaker feedback
            input_audio_echo_cancellation=AudioEchoCancellation(),

            # Reduce background noise
            input_audio_noise_reduction=AudioNoiseReduction(type="azure_deep_noise_suppression")
        )

        await self.connection.session.update(session=session_config)
        print("Session configured")

    async def process_events(self):
        """Process events from the VoiceLive service."""

        # Listen for events from the service
        async for event in self.connection:
            await self.handle_event(event)

    async def handle_event(self, event):
        """Handle different event types from the service."""

        # Session is ready - start capturing audio
        if event.type == ServerEventType.SESSION_UPDATED:
            print(f"Connected to agent: {event.session.agent.name}")
            self.audio_processor.start_capture()

        # User speech was transcribed
        elif event.type == ServerEventType.CONVERSATION_ITEM_INPUT_AUDIO_TRANSCRIPTION_COMPLETED:
            print(f'You: {event.get("transcript", "")}')

        # Agent is responding with audio transcript
        elif event.type == ServerEventType.RESPONSE_AUDIO_TRANSCRIPT_DONE:
            print(f'Agent: {event.get("transcript", "")}')

        # User started speaking (interrupt any playing audio)
        elif event.type == ServerEventType.INPUT_AUDIO_BUFFER_SPEECH_STARTED:
            self.audio_processor.clear_playback_queue()
            print("Listening...")

        # User stopped speaking
        elif event.type == ServerEventType.INPUT_AUDIO_BUFFER_SPEECH_STOPPED:
            print("Thinking...")

        # Receiving audio response chunks
        elif event.type == ServerEventType.RESPONSE_AUDIO_DELTA:
            self.audio_processor.queue_audio(event.delta)

        # Audio response complete
        elif event.type == ServerEventType.RESPONSE_AUDIO_DONE:
            print("Response complete\n")

        # Handle errors
        elif event.type == ServerEventType.ERROR:
            print(f"Error: {event.error.message}")


# AudioProcessor class
class AudioProcessor:
    """Handles audio input (microphone) and output (speakers) """

    def __init__(self, connection):
        self.connection = connection
        self.audio = pyaudio.PyAudio()

        # Audio settings: 24kHz, 16-bit PCM, mono
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 24000
        self.chunk_size = 1200  # 50ms chunks

        # Streams for input and output
        self.input_stream = None
        self.output_stream = None
        self.playback_queue = queue.Queue()

    def start_capture(self):
        """Start capturing audio from the microphone."""

        def capture_callback(in_data, frame_count, time_info, status):
            # Convert audio to base64 and send to VoiceLive
            audio_base64 = base64.b64encode(in_data).decode("utf-8")
            asyncio.run_coroutine_threadsafe(
                self.connection.input_audio_buffer.append(audio=audio_base64),
                self.loop
            )
            return (None, pyaudio.paContinue)

        # Store event loop for use in callback thread
        self.loop = asyncio.get_event_loop()

        self.input_stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=capture_callback
        )
        print("Microphone started")

    def start_playback(self):
        """Start audio playback system."""

        remaining = bytes()

        def playback_callback(in_data, frame_count, time_info, status):
            nonlocal remaining

            # Calculate bytes needed
            bytes_needed = frame_count * pyaudio.get_sample_size(pyaudio.paInt16)
            output = remaining[:bytes_needed]
            remaining = remaining[bytes_needed:]

            # Get more audio from queue if needed
            while len(output) < bytes_needed:
                try:
                    audio_data = self.playback_queue.get_nowait()
                    if audio_data is None:  # End signal
                        break
                    output += audio_data
                except queue.Empty:
                    # Pad with silence if no audio available
                    output += bytes(bytes_needed - len(output))
                    break

            # Keep any extra for next callback
            if len(output) > bytes_needed:
                remaining = output[bytes_needed:]
                output = output[:bytes_needed]

            return (output, pyaudio.paContinue)

        self.output_stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=playback_callback
        )
        print("Speakers ready")

    def queue_audio(self, audio_data):
        """Add audio data to the playback queue."""
        self.playback_queue.put(audio_data)

    def clear_playback_queue(self):
        """Clear any pending audio (used when user interrupts)."""
        while not self.playback_queue.empty():
            try:
                self.playback_queue.get_nowait()
            except queue.Empty:
                break

    def shutdown(self):
        """Clean up audio resources."""
        if self.input_stream:
            self.input_stream.stop_stream()
            self.input_stream.close()

        if self.output_stream:
            self.playback_queue.put(None)  # Signal end
            self.output_stream.stop_stream()
            self.output_stream.close()

        self.audio.terminate()
        print("Audio stopped")


if __name__ == "__main__":
    main()

```


## Blok 38 — MS Path3(2).txt

```python

from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import *

key_credential = AzureKeyCredential("FOUNDRY_KEY")

# Connect to a Foundry resource endpoint
client = TextTranslationClient(credential=key_credential, endpoint="FOUNDRY_ENDPOINT")

# Or connect using a region
client = TextTranslationClient(credential=key_credential, region="FOUNDRY_REGION")

```


## Blok 39 — MS Path3(2).txt

```python

languages = client.get_supported_languages(scope="translation")
print("{} languages supported:".format(len(languages.translation)))
for language in languages.translation.keys():
    print(languages.translation[language].name + " (" + language + ")")

```


## Blok 40 — MS Path3(2).txt

```python

input_text_elements = [InputTextItem(text="Hola"), InputTextItem(text="こんにちは")]
translation_results = client.translate(body=input_text_elements, to_language=["fr", "en"])
idx = 0
for translation in translation_results:
    input_text = input_text_elements[idx].text
    idx += 1
    sourceLanguage = translation.detected_language
    for translated_text in translation.translations:
        print(f"'{input_text}' was translated from {sourceLanguage.language} to {translated_text.to} as '{translated_text.text}'.")

```


## Blok 41 — MS Path3(2).txt

```python

source_text = "こんにちは"
input_text_elements = [InputTextItem(text=source_text)]
transliteration_results = client.transliterate(body=input_text_elements, language="ja",
                                               from_script="Jpan", to_script="Latn")
for transliteration in transliteration_results:
    sourceScript = transliteration.script
    targetScript = transliteration.text
    print(f"'{source_text}' was transliterated into {sourceScript} as {targetScript}.")

```


## Blok 42 — MS Path3(2).txt

```python

import azure.cognitiveservices.speech as speech_sdk

# Connect to a Foundry resource endpoint
translation_cfg = speech_sdk.translation.SpeechTranslationConfig(
                    subscription="FOUNDRY_KEY", endpoint="FOUNDRY_ENDPOINT")

# Or connect using a region
translation_cfg = speech_sdk.translation.SpeechTranslationConfig(
                    subscription="FOUNDRY_KEY", region="FOUNDRY_REGION")

```


## Blok 43 — MS Path3(2).txt

```python

# Configure languages
translation_cfg.speech_recognition_language = 'en-US'
translation_cfg.add_target_language('fr')
translation_cfg.add_target_language('ja')
print('Ready to translate from',translation_cfg.speech_recognition_language)

# Configure audio source
audio_cfg = speech_sdk.AudioConfig(use_default_microphone=True)

```


## Blok 44 — MS Path3(2).txt

```python

# Get a TranslationRecognizr object
translator = speech_sdk.translation.TranslationRecognizer(translation_config=translation_cfg,
                                                          audio_config=audio_cfg)
# Get input from mic and translate
print("Speak now...")
translation_results = translator.recognize_once_async().get()
print(f"Translating '{translation_results.text}'")

# Print each translation
translations = translation_results.translations
for translation_language in translations:
    print(f"{translation_language}: '{translations[translation_language]}'")

```


## Blok 45 — MS Path3(2).txt

```python

import azure.cognitiveservices.speech as speech_sdk

# Configure translation
translation_cfg = speech_sdk.translation.SpeechTranslationConfig(subscription="FOUNDRY_KEY",
                                                                 endpoint="FOUNDRY_ENDPOINT")
translation_cfg.speech_recognition_language = 'en-US'
translation_cfg.add_target_language('fr')
translation_cfg.add_target_language('ja')
audio_cfg = speech_sdk.AudioConfig(use_default_microphone=True)

# Configure speech synthesis
speech_cfg = speech_sdk.SpeechConfig(subscription="FOUNDRY_KEY", 
                                     endpoint="FOUNDRY_ENDPOINT")
audio_out_cfg = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
voices = {
        "fr": "fr-FR-HenriNeural",
        "ja": "ja-JP-NanamiNeural"
}

# Get trsnslations
translator = speech_sdk.translation.TranslationRecognizer(translation_config=translation_cfg,
                                                          audio_config=audio_cfg)
print("Speak now...")
translation_results = translator.recognize_once_async().get()
print(f"Translating '{translation_results.text}'")


# process the translation results
translations = translation_results.translations
for translation_language in translations:

    # Print ressults
    print(f"{translation_language}: '{translations[translation_language]}'")

    # Speak results
    speech_cfg.speech_synthesis_voice_name = voices.get(translation_language)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_cfg, audio_out_cfg)
    speak = speech_synthesizer.speak_text_async(translations[translation_language]).get()

    # CHeck for speech failure
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

```


## Blok 46 — MS Path3(2).txt

```python

import azure.cognitiveservices.speech as speech_sdk
from playsound3 import playsound

# Configure translation

```


## Blok 47 — MS Path2(2).txt

```python

import json

def recent_snowfall(location: str) -> str:
    """
    Fetches recent snowfall totals for a given location.
    :param location: The city name.
    :return: Snowfall details as a JSON string.
    """
    mock_snow_data = {"Seattle": "0 inches", "Denver": "2 inches"}
    snow = mock_snow_data.get(location, "Data not available.")
    return json.dumps({"location": location, "snowfall": snow})

```


## Blok 48 — MS Path2(2).txt

```python

# Define a function tool for the model to use
function_tool = FunctionTool(
    name="recent_snowfall",
    parameters={
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city name to check snowfall for."},
        },
        "required": ["location"],
        "additionalProperties": False
    },
    description="Get recent snowfall totals for a given location.",
    strict=True,
)

# Add the function tool to a list of tools for the agent
tools: list[Tool] = [function_tool]

# Create your agent with the toolset
agent = project_client.agents.create_version(
    name="snowfall-agent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a weather assistant tracking snowfall. Use the provided functions to answer questions.",
        tools=tools,
    )
)

```


## Blok 49 — MS Path2(2).txt

```python

tool = AzureFunctionTool(
    azure_function=AzureFunctionDefinition(
        input_binding=AzureFunctionBinding(
            storage_queue=AzureFunctionStorageQueue(
                queue_name="STORAGE_INPUT_QUEUE_NAME",
                queue_service_endpoint="STORAGE_QUEUE_SERVICE_ENDPOINT",
            )
        ),
        output_binding=AzureFunctionBinding(
            storage_queue=AzureFunctionStorageQueue(
                queue_name="STORAGE_OUTPUT_QUEUE_NAME",
                queue_service_endpoint="STORAGE_QUEUE_SERVICE_ENDPOINT",
            )
        ),
        function=AzureFunctionDefinitionFunction(
            name="queue_trigger",
            description="Get weather for a given location",
            parameters={
                "type": "object",
                "properties": {"location": {"type": "string", "description": "location to determine weather for"}},
            },
        ),
    )
)

agent = project_client.agents.create_version(
    agent_name="MyAgent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a helpful weather assistant. Use the provided Azure Function to get weather information for a location when needed.",
        tools=[tool],
    ),
)

```


## Blok 50 — MS Path2(2).txt

```python

from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails

with open(weather_asset_file_path, "r") as f:
      openapi_weather = cast(dict[str, Any], jsonref.loads(f.read()))

tool = OpenApiTool(
    openapi=OpenApiFunctionDefinition(
        name="get_weather",
        spec=openapi_weather,
        description="Retrieve weather information for a location.",
        auth=OpenApiAnonymousAuthDetails(),
    )
)

agent = project_client.agents.create_version(
    agent_name="openapi-agent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a weather assistant. Use the API to fetch weather data.",
        tools=[openapi_tool],
    ),
)

```


## Blok 51 — MS Path2(2).txt

```python

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool

project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)

# Connect to the product documentation knowledge base
knowledge_tool = MCPTool(
    server_label="product-docs",
    server_url=f"{search_endpoint}/knowledgebases/product-documentation/mcp"
)

# Create an agent with knowledge access
agent = project_client.agents.create_version(
    agent_name="product-support-agent",
    definition=PromptAgentDefinition(
        model="gpt-4o-mini",
        instructions="Answer product questions using the knowledge base. Always cite your sources.",
        tools=[knowledge_tool]
    )
)

```


## Blok 52 — MS Path2(2).txt

```python

agent = project_client.agents.create_version(
    agent_name="hr-assistant",
    definition=PromptAgentDefinition(
        model="gpt-4o-mini",
        instructions="Answer HR questions using the knowledge base.",
        tools=[knowledge_tool]
    )
)

```


## Blok 53 — MS Path2(2).txt

```python

retrieval_instructions = """You are a helpful HR assistant.

```


## Blok 54 — MS Path2(2).txt

```python

openai_client = project_client.get_openai_client()
conversation = openai_client.conversations.create()

# Test query that should trigger retrieval
response = openai_client.responses.create(
    conversation=conversation.id,
    input="How many vacation days do I get?",
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}}
)

print(response.output_text)

```


## Blok 55 — MS Path2(2).txt

```python

support_instructions = """You provide customer support using our product documentation.

Rules:

```


## Blok 56 — MS Path2(2).txt

```python

research_instructions = """You help employees research topics across company documentation.

Rules:

```


## Blok 57 — MS Path2(2).txt

```python

compliance_instructions = """You are a compliance documentation assistant.

Rules:

```


## Blok 58 — MS Path2(2).txt

```python

# Reference a workflow created in the Foundry portal
workflow_name = "triage-workflow"

# Create a conversation context for the workflow
conversation = openai_client.conversations.create()

# Execute the workflow, passing input to drive the workflow logic
stream = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}},
    input="Users can't reset their password from the mobile app.",
    stream=True,
)

```


## Blok 59 — MS Path2(2).txt

```python

for event in stream:
    if event.type == "response.completed":
        print("Workflow completed:")
        for message in event.response.output:
            if message.content:
                for content_item in message.content:
                    if content_item.type == 'output_text':
                        print(content_item.text)
    if (event.type == "response.output_item.done") and event.item.type == ItemType.WORKFLOW_ACTION:
        print(f"Action '{event.item.action_id}' completed with status: {event.item.status}")

```


## Blok 60 — MS Path1(2).txt

```python

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

```


## Blok 61 — MS Path1(2).txt

```python

openai_client = project_client.get_openai_client(api_version="2024-10-21")

```


## Blok 62 — MS Path1(2).txt

```python

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = "https://{resource-name}.openai.azure.com/openai/v1/",  
  api_key=token_provider,
)

```


## Blok 63 — MS Path1(2).txt

```python

import os
from openai import OpenAI

openai_client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url="https://{resource-name}.openai.azure.com/openai/v1/"
)

```


## Blok 64 — MS Path1(2).txt

```python

from openai import OpenAI

openai_client = OpenAI()  # Uses environment variables

```


## Blok 65 — MS Path1(2).txt

```python

import os
from openai import AzureOpenAI

openai_client = AzureOpenAI(
    azure_endpoint = "https://{resource-name}.openai.azure.com"
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2024-10-21",
)

```


## Blok 66 — MS Path1(2).txt

```python

# Generate a response using the OpenAI-compatible client
response = openai_client.responses.create(
    model="gpt-4.1",  # Your model deployment name
    input="What is Microsoft Foundry?"
)

# Display the response
print(response.output_text)

```


## Blok 67 — MS Path1(2).txt

```python

response = openai_client.responses.create(
    model="gpt-4.1",
    input="Explain machine learning in simple terms."
)

print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")

```


## Blok 68 — MS Path1(2).txt

```python

response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Explain neural networks."
)

print(response.output_text)

```


## Blok 69 — MS Path1(2).txt

```python

response = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Write a creative story about AI.",
    temperature=0.8,  # Higher temperature for more creativity
    max_output_tokens=200  # Limit response length
)

print(response.output_text)
temperature: Controls randomness (0.0-2.0). Higher values make output more creative and varied
max_output_tokens: Limits the maximum number of tokens in the response
top_p: Alternative to temperature for controlling randomness

```


## Blok 70 — MS Path1(2).txt

```python

# Using a Foundry direct model
response = openai_client.responses.create(
    model="microsoft-phi-4",  # Example Foundry direct model
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the benefits of small language models?"
)

print(response.output_text)

```


## Blok 71 — MS Path1(2).txt

```python

# First turn in the conversation
response1 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="What is machine learning?"
)

print("Assistant:", response1.output_text)

# Continue the conversation
response2 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="Can you give me an example?",
    previous_response_id=response1.id
)

print("Assistant:", response2.output_text)

```


## Blok 72 — MS Path1(2).txt

```python

# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    response = openai_client.responses.create(
                model=model_name,
                instructions="You are a helpful AI assistant that explains technology concepts clearly.",
                input=input_text,
                previous_response_id=last_response_id
    )
    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response.id 

```


## Blok 73 — MS Path1(2).txt

```python

try:
    # Start with initial message
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is machine learning?"
        }
    ]

    # First response
    response1 = openai_client.responses.create(
        model="gpt-4.1",
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add assistant response to history
    conversation_history += response1.output

    # Add new user message
    conversation_history.append({
        "type": "message",
        "role": "user", 
        "content": "Can you give me an example?"
    })

    # Second response with full history
    response2 = openai_client.responses.create(
        model="gpt-4.1",
        input=conversation_history
    )

    print("Assistant:", response2.output_text)

except Exception as ex:
    print(f"Error: {ex}")

```


## Blok 74 — MS Path1(2).txt

```python

try:   

    # Retrieve a previous response
    response_id = "resp_67cb61fa3a448190bcf2c42d96f0d1a8"  # Example ID
    previous_response = openai_client.responses.retrieve(response_id)

    print(f"Previous response: {previous_response.output_text}")

except Exception as ex:
    print(f"Error: {ex}")

```


## Blok 75 — MS Path1(2).txt

```python

stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True
)

for event in stream:
    print(event, end="", flush=True)

```


## Blok 76 — MS Path1(2).txt

```python

stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True
)
for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="")
                elif event.type == "response.completed":
                    response_id = event.response.id

```


## Blok 77 — MS Path1(2).txt

```python

import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://<resource-name>.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

async def main():
    response = await client.responses.create(
        model="gpt-4.1",
        input="Explain quantum computing briefly."
    )
    print(response.output_text)

asyncio.run(main())

```


## Blok 78 — MS Path1(2).txt

```python

async def stream_response():
    stream = await client.responses.create(
        model="gpt-4.1",
        input="Write a haiku about coding.",
        stream=True
    )

    async for event in stream:
        print(event, end="", flush=True)

asyncio.run(stream_response())

```


## Blok 79 — MS Path1(2).txt

```python

completion = openai_client.chat.completions.create(
    model="gpt-4o",  # Your model deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "When was Microsoft founded?"}
    ]
)

print(completion.choices[0].message.content)

```


## Blok 80 — MS Path1(2).txt

```python

# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Add the first user message
conversation_messages.append(
    {"role": "user",
    "content": "When was Microsoft founded?"}
)

# Get a completion
completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=conversation_messages
)
assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_text)

# Append the response to the conversation
conversation_messages.append(
    {"role": "assistant", "content": assistant_text}
)

# Add the next user message
conversation_messages.append(
    {"role": "user",
    "content": "Who founded it?"}
)

# Get a completion
completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=conversation_messages
)
assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_text)

# and so on...

```


## Blok 81 — MS Path1(2).txt

```python

# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Add the user message
    conversation_messages.append(
        {"role": "user",
        "content": input_text}
    )

    # Get a completion
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_messages
    )
    assistant_message = completion.choices[0].message.content
    print("\nAssistant:", assistant_message)

    # Append the response to the conversation
    conversation_messages.append(
        {"role": "assistant", "content": assistant_message}
    )

```


## Blok 82 — MS Path1(2).txt

```python

from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

response = client.responses.create(
    model={model_deployment},
    instructions="You are a helpful AI assistant.",
    input="Find me some information about vintage computers.",
    # Specify available tools as a JSON list
    tools=[
        { 
            # A tool definition
            "type": "{tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        },
        { 
            # Another tool definition
            "type": "{another_tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        }
    ]
)
print(response.output_text)

```


## Blok 83 — MS Path1(2).txt

```python

from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the code_interpreter tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 16?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)

```


## Blok 84 — MS Path1(2).txt

```python

import math

# Calculate the square root of 16
square_root = math.sqrt(16)

```


## Blok 85 — MS Path1(2).txt

```python

from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the web_search tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)

print(response.output_text)

```


## Blok 86 — MS Path1(2).txt

```python

from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=model_deployment,
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the maximum amount I can claim for a taxi ride?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
print(response.output_text)

```


## Blok 87 — MS Path1(2).txt

```python

import time
from openai import OpenAI

# Function to get the current time
def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"


# Main function
def main():
    client = OpenAI(
        base_url={openai_endpoint},
        api_key={auth_key_or_token}
    )

    function_tools = [
        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }
    ]

    # Initialize messages with a system prompt
    messages = [
        {"role": "developer", "content": "You are an AI assistant that provides information."},
    ]

    # Loop until the user types 'quit'
    while True:
        prompt = input("\nEnter a prompt (or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break

        # Append the user prompt to the messages
        messages.append({"role": "user", "content": prompt})

        # Get initial response
        response = client.responses.create(
            model=model_deployment,
            input=messages,
            tools=function_tools
        )

        # Append model output to the messages
        messages += response.output

        # Was there a function call?
        for item in response.output:
            if item.type == "function_call" and item.name == "get_time":
                current_time = get_time()
                messages.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": current_time
                })

                # Get a follow up response using the tool output
                response = client.responses.create(
                    model=model_deployment,
                    instructions="Answer only with the tool output.",
                    input=messages,
                    tools=function_tools
                )

        print(response.output_text)


# Run the main function when the script starts
if __name__ == '__main__':
    main()

```


## Blok 88 — MS Path1(2).txt

```python

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

client = project.get_openai_client()

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are a helpful travel advisor. "
         "Use the following hotel data to answer: " + retrieved_context},
        {"role": "user", "content": "Which hotels do you offer in Paris?"},
    ],
)

print(response.output_text)

```
