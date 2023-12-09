FROM openfabric/openfabric-pyenv:0.1.9-3.8

RUN mkdir cognitive-assistant
WORKDIR /cognitive-assistant
COPY . .
RUN pip install --upgrade pip setuptools
RUN poetry install -vvv --no-dev
RUN pip install openfabric-pysdk
RUN pip install transformers datasets evaluate


EXPOSE 5000
CMD ["sh","start.sh"]
