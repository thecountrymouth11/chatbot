import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from transformers import AutoTokenizer, AutoModelForQuestionAnswering,pipeline



############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")

    qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

    for text in request.text:
        # TODO Add code here
        response = qa_pipeline(text)
        output.append(response)

    return SimpleText(dict(text=output))
