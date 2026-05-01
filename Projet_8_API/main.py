from fastapi import FastAPI
#from tensorflow import keras
#from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import pandas as pd
#from tensorflow.keras.preprocessing.sequence import pad_sequences
from azure.monitor.opentelemetry import configure_azure_monitor
import logging
#import mlflow
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opencensus.ext.azure.log_exporter import AzureLogHandler
from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()


# Ajouter le handler console pour voir les logs en local
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Setup logger
logger = logging.getLogger(__name__)
"""logger.addHandler(AzureLogHandler(
    connection_string="InstrumentationKey=63f5fb13-6bad-4790-9158-dd15a35dffa9;IngestionEndpoint=https://francecentral-1.in.applicationinsights.azure.com/;LiveEndpoint=https://francecentral.livediagnostics.monitor.azure.com/;ApplicationId=b12b6f69-5163-4e00-a2d0-091bb33efaf2"
))"""
logger.info("test")

app = FastAPI()

@app.get("/")
async def root():
    logger.info(f"test")
    return {"message": "Hello World"}

@app.post("/segmentation")
async def segmentation(file: UploadFile = File(...)):
    # Lire l'image envoyée
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # 🔧 Exemple de "segmentation" (ici on fait juste un traitement simple)
    # Tu peux remplacer par ton modèle ML
    processed_image = image.convert("L")  # exemple: niveaux de gris

    # Convertir l'image en bytes pour la réponse
    img_io = io.BytesIO()
    processed_image.save(img_io, format="PNG")
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")