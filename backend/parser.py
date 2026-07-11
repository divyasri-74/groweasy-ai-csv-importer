import pandas as pd


def parse_csv(file_path):
    """
    Reads the uploaded CSV file and returns:
    - column names
    - sample data
    - total rows
    - total columns
    """

    try:
        # Read CSV
        df = pd.read_csv(file_path)

        # Replace NaN with empty string
        df = df.fillna("")

        # Get column names
        columns = list(df.columns)

        # Convert DataFrame to list of dictionaries
        records = df.to_dict(orient="records")

        return {
            "columns": columns,
            "sample_data": records,
            "total_rows": len(df),
            "total_columns": len(columns)
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    result = parse_csv("uploads/sample.csv")

    print(result)