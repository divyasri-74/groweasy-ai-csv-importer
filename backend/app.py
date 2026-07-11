from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from parser import parse_csv
from ai_mapper import extract_crm_records
from crm_formatter import format_crm_records
from validator import validate_records

app = FastAPI(
    title="GrowEasy AI CSV Importer",
    version="2.0.0"
)

# -----------------------------------------
# CORS
# -----------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# -----------------------------------------
# Home
# -----------------------------------------

@app.get("/")
def home():

    return {

        "status": "success",

        "message": "GrowEasy AI CSV Importer Backend Running"

    }


# -----------------------------------------
# Health
# -----------------------------------------

@app.get("/health")
def health():

    return {

        "status": "healthy"

    }


# -----------------------------------------
# Upload CSV
# -----------------------------------------

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    try:

        # -----------------------------
        # Save File
        # -----------------------------

        file_path = os.path.join(

            UPLOAD_FOLDER,

            file.filename

        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(

                file.file,

                buffer

            )

        # -----------------------------
        # Parse CSV
        # -----------------------------

        csv_data = parse_csv(file_path)

        if "error" in csv_data:

            return {

                "success": False,

                "message": csv_data["error"]

            }

        # -----------------------------
        # AI Extraction
        # -----------------------------

        ai_records = extract_crm_records(

            csv_data["sample_data"]

        )

        # -----------------------------
        # CRM Formatter
        # -----------------------------

        formatted_records = format_crm_records(

            ai_records

        )

        # -----------------------------
        # Validation
        # -----------------------------

        validation = validate_records(

            formatted_records

        )

        # -----------------------------
        # Final Response
        # -----------------------------

        return {

            "success": True,

            "filename": file.filename,

            "preview": {

                "columns": csv_data["columns"],

                "sample_data": csv_data["sample_data"],

                "total_rows": csv_data["total_rows"],

                "total_columns": csv_data["total_columns"]

            },

            "summary": {

                "total_records":

                    validation["total_records"],

                "imported":

                    validation["total_valid"],

                "skipped":

                    validation["total_skipped"]

            },

            "valid_records":

                validation["valid_records"],

            "skipped_records":

                validation["skipped_records"]

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }