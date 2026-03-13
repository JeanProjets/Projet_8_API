from fastapi import FastAPI
from tensorflow import keras
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from azure.monitor.opentelemetry import configure_azure_monitor
import logging
import mlflow
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opencensus.ext.azure.log_exporter import AzureLogHandler
from fastapi import FastAPI

app = FastAPI()


# Ajouter le handler console pour voir les logs en local
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Setup logger
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string="InstrumentationKey=63f5fb13-6bad-4790-9158-dd15a35dffa9;IngestionEndpoint=https://francecentral-1.in.applicationinsights.azure.com/;LiveEndpoint=https://francecentral.livediagnostics.monitor.azure.com/;ApplicationId=b12b6f69-5163-4e00-a2d0-091bb33efaf2"
))
logger.info("test")
VOCAB_SIZE = 20000
MAX_LEN = 50

model = keras.models.load_model("model1_simple_neural_network.keras")
with open("tokenizer_simple_neural_network.json", "r", encoding="utf-8") as f:
    tokenizer_json_str = f.read()   # <- string

tokenizer = tokenizer_from_json(tokenizer_json_str)

app = FastAPI()


@app.get("/")
async def root():
    logger.info(f"test")
    return {"message": "Hello World"}

@app.get("/feeling_predictions/{text}")
async def read_item(text):
    # On fait la pipeline pour pouvoir appeler le modèle. Le modèle prend un token en entrée et non une phrase 
    X_example = pd.Series([text], name="new_test")
    X_example_seq = tokenizer.texts_to_sequences(X_example)
    X_example_pad = pad_sequences(X_example_seq, maxlen=MAX_LEN, padding='post', truncating='post')
    y_prediction = (model.predict(X_example_pad) > 0.5).astype(int).ravel()
    prediction = y_prediction[0]
    if prediction == 0:
        feeling_result = "sad"
    else:
        feeling_result = "happy"
    logger.info(f"pour le texte {text}, la prediction est {feeling_result}")
    return {"text": text,
            "feeling_result": feeling_result}