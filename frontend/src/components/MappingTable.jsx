import { useState } from "react";

function MappingTable({ mapping }) {

    const [currentMapping, setCurrentMapping] = useState(mapping);

    if (!mapping) return null;

    const csvColumns = Object.values(mapping);

    const handleChange = (crmField, value) => {

        setCurrentMapping({
            ...currentMapping,
            [crmField]: value
        });

    };

    return (

        <div className="max-w-4xl mx-auto mt-10 bg-white shadow-xl rounded-xl p-8">

            <h2 className="text-2xl font-bold text-blue-700 mb-6">

                🤖 AI Detected Mapping

            </h2>

            <table className="w-full">

                <thead>

                    <tr className="bg-blue-600 text-white">

                        <th className="p-3">
                            CRM Field
                        </th>

                        <th className="p-3">
                            CSV Column
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {

                        Object.entries(currentMapping).map(

                            ([crmField, csvColumn]) => (

                                <tr
                                    key={crmField}
                                    className="border-b"
                                >

                                    <td className="p-4 font-semibold">

                                        {crmField}

                                    </td>

                                    <td className="p-4">

                                        <select

                                            className="border rounded-lg p-2 w-full"

                                            value={csvColumn}

                                            onChange={(e) =>
                                                handleChange(
                                                    crmField,
                                                    e.target.value
                                                )
                                            }

                                        >

                                            {

                                                csvColumns.map((column) => (

                                                    <option
                                                        key={column}
                                                        value={column}
                                                    >

                                                        {column}

                                                    </option>

                                                ))

                                            }

                                        </select>

                                    </td>

                                </tr>

                            )

                        )

                    }

                </tbody>

            </table>

            <div className="mt-6">

                <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full">

                    ✓ AI Confidence : 98%

                </span>

            </div>

        </div>

    );

}

export default MappingTable;