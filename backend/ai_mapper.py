import os
import json
from dotenv import load_dotenv
from google import genai

# -----------------------------------
# Load Environment Variables
# -----------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

# -----------------------------------
# GrowEasy CRM Fields
# -----------------------------------

CRM_FIELDS = [
    "created_at",
    "name",
    "email",
    "country_code",
    "mobile_without_country_code",
    "company",
    "city",
    "state",
    "country",
    "lead_owner",
    "crm_status",
    "crm_note",
    "data_source",
    "possession_time",
    "description"
]


# -----------------------------------
# AI Extraction
# -----------------------------------

def extract_crm_records(records):

    prompt = f"""
You are an expert CRM Data Extraction AI.

Convert every input record into GrowEasy CRM format.

IMPORTANT RULES

1. Return ONLY JSON.
2. Do not explain anything.
3. Do not wrap inside markdown.
4. Unknown values should be "".
5. Detect similar columns intelligently.

Required Output Fields

{json.dumps(CRM_FIELDS, indent=4)}

CSV Records

{json.dumps(records, indent=4)}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        crm_records = json.loads(text)

        return crm_records

    except Exception as e:

        print("\nGemini Error")
        print(e)

        print("\nUsing Fallback Mapping...\n")

        return fallback_mapping(records)


# -----------------------------------
# Fallback Mapping
# -----------------------------------

def fallback_mapping(records):

    final = []

    for row in records:

        crm = {

            "created_at": "",

            "name":
                row.get("Customer Name")
                or row.get("Name")
                or row.get("Lead Name")
                or row.get("Full Name")
                or "",

            "email":
                row.get("Email")
                or row.get("Email Address")
                or "",

            "country_code":"",

            "mobile_without_country_code":
                str(
                    row.get("Phone")
                    or row.get("Mobile")
                    or row.get("Contact Number")
                    or ""
                ),

            "company":
                row.get("Company")
                or row.get("Organization")
                or row.get("Business")
                or "",

            "city":
                row.get("City")
                or "",

            "state":
                row.get("State")
                or "",

            "country":
                row.get("Country")
                or "",

            "lead_owner":"",

            "crm_status":"",

            "crm_note":"",

            "data_source":"",

            "possession_time":"",

            "description":""

        }

        final.append(crm)

    return final


# -----------------------------------
# Testing
# -----------------------------------

if __name__ == "__main__":

    sample = [

        {

            "Customer Name":"John Doe",

            "Email":"john@gmail.com",

            "Phone":"9876543210",

            "Company":"ABC Pvt Ltd",

            "City":"Hyderabad",

            "State":"Telangana",

            "Country":"India"

        }

    ]

    result = extract_crm_records(sample)

    print(json.dumps(result, indent=4))