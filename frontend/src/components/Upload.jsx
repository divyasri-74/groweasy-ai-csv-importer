import React, { useState } from "react";
import API from "../services/api";
import Loader from "./Loader";

function Upload({
    setPreview,
    setMapping,
    setRecords,
    setSummary
}) {

    const [selectedFile, setSelectedFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    // ------------------------
    // File Selection
    // ------------------------

    const handleFileChange = (e) => {

        const file = e.target.files[0];

        if (!file) return;

        if (!file.name.endsWith(".csv")) {

            setError("Please select a CSV file.");

            return;
        }

        setError("");

        setSelectedFile(file);

    };

    // ------------------------
    // Upload CSV
    // ------------------------

    const uploadCSV = async () => {

        if (!selectedFile) {

            alert("Please select a CSV file.");

            return;

        }

        const formData = new FormData();

        formData.append("file", selectedFile);

        try {

            setLoading(true);

            const response = await API.post(

                "/upload",

                formData,

                {

                    headers: {

                        "Content-Type": "multipart/form-data"

                    }

                }

            );

            console.log(response.data);

            if (response.data.success) {

                setPreview(response.data.preview);

                setSummary(response.data.summary);

                setRecords(response.data.valid_records);

                setMapping(null);

            }

            else {

                alert(response.data.message);

            }

        }

        catch (err) {

            console.log(err);

            alert("Upload Failed");

        }

        finally {

            setLoading(false);

        }

    };
        return (

        <div className="upload-card">

            <h2>📂 Upload CSV File</h2>

            <p
                style={{
                    color: "#666",
                    marginBottom: "20px"
                }}
            >
                Upload your CSV file to import leads into GrowEasy CRM.
            </p>

            <input
                type="file"
                accept=".csv"
                onChange={handleFileChange}
            />

            <br />

            {

                selectedFile && (

                    <div
                        style={{
                            marginTop: "20px",
                            color: "green",
                            fontWeight: "bold"
                        }}
                    >

                        Selected File:

                        <br />

                        {selectedFile.name}

                    </div>

                )

            }

            {

                error && (

                    <div
                        style={{
                            marginTop: "20px",
                            color: "red",
                            fontWeight: "bold"
                        }}
                    >

                        {error}

                    </div>

                )

            }

            <button

                className="upload-btn"

                onClick={uploadCSV}

                disabled={loading}

            >

                {

                    loading

                        ? "Processing..."

                        : "Upload CSV"

                }

            </button>

            {

                loading && (

                    <Loader />

                )

            }

        </div>

    );

}

export default Upload;