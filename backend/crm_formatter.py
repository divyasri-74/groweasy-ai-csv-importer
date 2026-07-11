def format_crm_records(records):
    """
    Formats AI extracted records into
    GrowEasy CRM format.
    """

    formatted = []

    for record in records:

        crm = {

            "created_at": record.get("created_at", "").strip(),

            "name": record.get("name", "").strip(),

            "email": record.get("email", "").strip(),

            "country_code": record.get("country_code", "").strip(),

            "mobile_without_country_code":
                str(
                    record.get(
                        "mobile_without_country_code",
                        ""
                    )
                ).strip(),

            "company": record.get("company", "").strip(),

            "city": record.get("city", "").strip(),

            "state": record.get("state", "").strip(),

            "country": record.get("country", "").strip(),

            "lead_owner": record.get("lead_owner", "").strip(),

            "crm_status": record.get("crm_status", "").strip(),

            "crm_note": record.get("crm_note", "").strip(),

            "data_source": record.get("data_source", "").strip(),

            "possession_time":
                record.get(
                    "possession_time",
                    ""
                ).strip(),

            "description":
                record.get(
                    "description",
                    ""
                ).strip()

        }

        formatted.append(crm)

    return formatted


# -------------------------
# Testing
# -------------------------

if __name__ == "__main__":

    sample = [

        {

            "name": "John",

            "email": "john@gmail.com",

            "company": "ABC Pvt Ltd"

        }

    ]

    result = format_crm_records(sample)

    print(result)