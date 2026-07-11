import re


# -------------------------------------
# Clean String
# -------------------------------------

def clean_string(value):

    if value is None:
        return ""

    return str(value).strip()


# -------------------------------------
# Normalize Email
# -------------------------------------

def normalize_email(email):

    email = clean_string(email)

    return email.lower()


# -------------------------------------
# Clean Phone Number
# -------------------------------------

def clean_phone(phone):

    phone = clean_string(phone)

    phone = re.sub(r"\D", "", phone)

    return phone


# -------------------------------------
# Safe Dictionary Access
# -------------------------------------

def safe_get(record, key):

    if key not in record:

        return ""

    return clean_string(record[key])


# -------------------------------------
# Remove Null Values
# -------------------------------------

def remove_null_values(record):

    cleaned = {}

    for key, value in record.items():

        if value is None:

            cleaned[key] = ""

        else:

            cleaned[key] = clean_string(value)

    return cleaned


# -------------------------------------
# Testing
# -------------------------------------

if __name__ == "__main__":

    sample = {

        "name": " John ",

        "email": "TEST@GMAIL.COM ",

        "phone": "+91 98765-43210"

    }

    print(clean_string(sample["name"]))

    print(normalize_email(sample["email"]))

    print(clean_phone(sample["phone"]))