import { useState } from "react";

import Navbar from "../components/Navbar";
import Upload from "../components/Upload";
import PreviewTable from "../components/PreviewTable";
import MappingTable from "../components/MappingTable";
import ResultTable from "../components/ResultTable";

function Home() {

    const [preview, setPreview] = useState(null);

    const [mapping, setMapping] = useState(null);

    const [records, setRecords] = useState([]);

    const [summary, setSummary] = useState(null);

    return (

        <>

            <Navbar />

            <div className="container">

                <Upload

                    setPreview={setPreview}

                    setMapping={setMapping}

                    setRecords={setRecords}

                    setSummary={setSummary}

                />

                {

                    preview &&

                    <PreviewTable

                        data={preview}

                    />

                }

                {

                    mapping &&

                    <MappingTable

                        mapping={mapping}

                    />

                }

                {

                    records.length > 0 &&

                    <ResultTable

                        records={records}

                        summary={summary}

                    />

                }

            </div>

        </>

    );

}

export default Home;