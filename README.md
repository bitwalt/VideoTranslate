# Youtube Translator


Repository with helper functions for translating videos from one language to another.


## Features

- Extract original captions from a video and save them in *JSON*  or *txt* (full-text). 
- Download a video from Youtube and save it in *mp4* format.
- Translate captions from one language to another 


### Installation

An installation Poetry is required. [Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. Take a look to [installations](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions).

Dependencies used:
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [pytube](https://github.com/pytube/pytube)

Install dependencies with 

```bash
$ poetry install
```
### Run the app

Modify the `config.json` file to set the correct values for the following parameters:
- `videos`: Youtube video IDs and video names
- `formatter`: Formatter for the captions. Possible values: `json` (with video timeslots reference) `txt` (full-text)
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
  Options: local environment (cpu) /  calling cloud-services API.

- [ ]  Try to generate a speech for translated captions using *Text2Speech* models.
    *References:* [DeepSpeech-Italian-Model](https://github.com/MozillaItalia/DeepSpeech-Italian-Model), [Woord](https://www.getwoord.com/),
[TTS](https://github.com/mozilla/TTS)

- [ ] Adapt generated speech to original video timeslots 

