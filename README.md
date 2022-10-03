# Video Translator

Repository with helper functions for translating videos from one language to another.

Providing a stramlit UI with a web toolkit for downloading, translating, transcribing, generating video. 

Created to disseminate educational resources on bitcoin.

## Screenshot

![ScreenShot](https://raw.github.com/waltermaffy/VideoTranslate/main/videotranslate/static/screenshot.png)

## Run

Using python environment (Docker in future)
```
$ pip install -r requirements.txt
$ streamlit run start_streamlit.py
```


## Possible Outputs


-  "original_video: .mp4    -> Download video from url (youtube converter) or other libraries,
-  "original_captions_text": str -> Download caption from url or use Speech2Text AI model,
-  "original_audio": .mp3   -> Download from url or other libraries,              
-  "translated_video_captions: .mp4" -> Video file with translated captions overwritten,
-  "translated_video: .mp4" -> Video file with new generated audio translated from original,
  "translated_captions: str" -> New translated captions
  "translated_audio: mp3", -> Translate audio using S2T -> Transltor -> T2S
}

# Work in Progress -


## Features

- Extract original captions from a video and save them in *JSON*  or *txt* (full-text). 
- Download a video from Youtube and save it in *mp4* format.
- Translate captions from one language to another 


### Installation

An installation of Poetry is required. [Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. Take a look to [installations](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions).

For OSx / linux / bashonwindows install:
```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Dependencies used:
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [pytube](https://github.com/pytube/pytube)

Install dependencies with:
```bash
$ poetry install
```
### Run the app

Modify the `config.json` file to set the correct values for the following parameters:
- `videos`: Youtube video IDs and video names
- `formatter`: Formatter for the captions.
    - `json` (with video timeslots reference)
    - `txt` (full-text)
- `output_folder`: Folder where the captions or videos will be saved.
- `language_from`: Language of the captions. 
- `language_from`: Translation language.
  
Run script with: 
```bash
$ cd videotranslate
$ poetry run python main.py
```


### TODO
- [ ] Use pre-trained AI model insted of *youtube_transcript_api* to translate video captions. 
  Options: local environment (CPU) / cloud-services API, P2P GPU power.

- [ ]  Try to generate a speech for translated captions using *Text2Speech* models.
    *References:* [DeepSpeech-Italian-Model](https://github.com/MozillaItalia/DeepSpeech-Italian-Model), [Woord](https://www.getwoord.com/),
[TTS](https://github.com/mozilla/TTS)

- [ ] Adapt generated speech to original video timeslots 

