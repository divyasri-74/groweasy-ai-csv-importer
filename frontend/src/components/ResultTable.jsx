function ResultTable({ records, summary }) {

    if (!records || records.length === 0)
        return null;

    const columns = Object.keys(records[0]);

    return (

        <div className="card">

            <h2>AI Extracted CRM Records</h2>

            <div className="summary">

                <div className="box">

                    <h3>Imported</h3>

                    <p>{summary.imported}</p>

                </div>

                <div className="box">

                    <h3>Skipped</h3>

                    <p>{summary.skipped}</p>

                </div>

                <div className="box">

                    <h3>Total</h3>

                    <p>{summary.total_records}</p>

                </div>

            </div>

            <div className="table-container">

                <table>

                    <thead>

                        <tr>

                            {

                                columns.map(col => (

                                    <th key={col}>{col}</th>

                                ))

                            }

                        </tr>

                    </thead>

                    <tbody>

                        {

                            records.map((row, index) => (

                                <tr key={index}>

                                    {

                                        columns.map(col => (

                                            <td key={col}>

                                                {row[col]}

                                            </td>

                                        ))

                                    }

                                </tr>

                            ))

                        }

                    </tbody>

                </table>

            </div>

        </div>

    );

}

export default ResultTable;