FROM python:latest 

RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install --no-install-recommends -y \
curl make 

WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/  
RUN poetry config virtualenvs.create false 
RUN poetry install  

COPY . /app
EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "app/video_translator.py" ]