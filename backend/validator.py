import re

# ----------------------------------
# Email Validation
# ----------------------------------

EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'


def is_valid_email(email):

    if not email:
        return False

    return re.match(EMAIL_REGEX, email) is not None


# ----------------------------------
# Phone Validation
# ----------------------------------

def is_valid_phone(phone):

    phone = str(phone).strip()

    phone = phone.replace("+", "")

    if not phone.isdigit():
        return False

    return 7 <= len(phone) <= 15


# ----------------------------------
# Validate CRM Records
# ----------------------------------

def validate_records(records):

    valid_records = []

    skipped_records = []

    seen_emails = set()

    seen_phones = set()

    for record in records:

        errors = []

        email = str(record.get("email", "")).strip()

        phone = str(
            record.get(
                "mobile_without_country_code",
                ""
            )
        ).strip()

        name = str(record.get("name", "")).strip()

        # ----------------------------
        # Name Validation
        # ----------------------------

        if name == "":
            errors.append("Missing Name")

        # ----------------------------
        # Email Validation
        # ----------------------------

        if email:

            if not is_valid_email(email):
                errors.append("Invalid Email")

            elif email.lower() in seen_emails:
                errors.append("Duplicate Email")

            else:
                seen_emails.add(email.lower())

        # ----------------------------
        # Phone Validation
        # ----------------------------

        if phone:

            if not is_valid_phone(phone):
                errors.append("Invalid Phone")

            elif phone in seen_phones:
                errors.append("Duplicate Phone")

            else:
                seen_phones.add(phone)

        # ----------------------------
        # Final Decision
        # ----------------------------

        if len(errors) == 0:

            valid_records.append(record)

        else:

            record["validation_errors"] = errors

            skipped_records.append(record)

    return {

        "valid_records": valid_records,

        "skipped_records": skipped_records,

        "total_records": len(records),

        "total_valid": len(valid_records),

        "total_skipped": len(skipped_records)

    }


# ----------------------------------
# Testing
# ----------------------------------

if __name__ == "__main__":

    sample = [

        {

            "name": "John",

            "email": "john@gmail.com",

            "mobile_without_country_code": "9876543210"

        },

        {

            "name": "Alice",

            "email": "john@gmail.com",

            "mobile_without_country_code": "9876543211"

        },

        {

            "name": "",

            "email": "wrongmail",

            "mobile_without_country_code": "123"

        }

    ]

    result = validate_records(sample)

    print(result)