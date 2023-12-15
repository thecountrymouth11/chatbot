FROM openfabric/tee-python-cpu:latest

RUN mkdir application
WORKDIR /application
COPY . .
RUN poetry install -vvv --no-dev
RUN pip install transformers
RUN pip install accelerate
Run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
EXPOSE 5500
CMD ["sh","start.sh"]