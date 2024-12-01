# Video Translator

A Python application for translating videos from one language to another, with a Streamlit web interface for easy interaction.

## Features

- Extract and translate video captions using multiple translation services:
  - OpenAI GPT
  - DeepL
  - HuggingFace
- Download videos from YouTube
- Transcribe audio to text using OpenAI Whisper
- Support for multiple input formats:
  - YouTube URLs
  - Local video files
- Output formats:
  - Text
  - JSON (with timestamps)

## Screenshot

![ScreenShot](https://raw.github.com/waltermaffy/VideoTranslate/main/videotranslate/static/screenshot.png)

## Installation

### Using Poetry (Recommended)

1. Install Poetry if you haven't already:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

2. Install dependencies:
```bash
poetry install
```

### Using pip

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file with the following API keys:
```
OPENAI_API_KEY=your_openai_key
DEEPL_API_KEY=your_deepl_key
HUGGINGFACE_API_TOKEN=your_huggingface_token
```

## Running the Application

### Using Poetry

```bash
poetry run streamlit run app/video_translator.py
```

### Using Docker

```bash
make start
```

Or manually:

```bash
docker-compose build --no-cache
docker-compose up -d
```

The application will be available at `http://localhost:8501`

## Configuration

The application can be configured through `config.py`. Key settings include:

- Translation service (OpenAI, DeepL, HuggingFace)
- Default source and target languages
- Output format (Text/JSON)
- Model names and API configurations

## Dependencies

- Python >= 3.12
- Streamlit
- OpenAI
- DeepL
- youtube-transcript-api
- pytube
- python-dotenv

## License

MIT License - See LICENSE file for details

## Contributing

Feel free to open issues or submit pull requests. Please ensure tests pass before submitting PRs.

## TODO

- [ ] Implement pre-trained AI models for caption translation
- [ ] Add Text-to-Speech synthesis for translated captions
- [ ] Synchronize generated speech with video timestamps
- [ ] Add support for more translation services
- [ ] Improve error handling and user feedback

