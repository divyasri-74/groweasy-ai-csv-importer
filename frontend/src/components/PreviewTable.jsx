import React, { useState } from "react";
import { FaSearch, FaTable } from "react-icons/fa";

function PreviewTable({ data }) {

    // Hooks must always be at the top
    const [search, setSearch] = useState("");

    // If no data, don't render anything
    if (!data) return null;

    const columns = data.columns || [];

    const rows = (data.sample_data || []).filter((row) =>
        Object.values(row)
            .join(" ")
            .toLowerCase()
            .includes(search.toLowerCase())
    );

    return (
        <div
            style={{
                maxWidth: "1200px",
                margin: "30px auto",
                background: "#fff",
                borderRadius: "10px",
                padding: "20px",
                boxShadow: "0 0 15px rgba(0,0,0,0.1)"
            }}
        >
            {/* Header */}
            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: "20px"
                }}
            >
                <div
                    style={{
                        display: "flex",
                        alignItems: "center",
                        gap: "10px"
                    }}
                >
                    <FaTable color="#2563eb" size={28} />

                    <h2
                        style={{
                            color: "#2563eb",
                            margin: 0
                        }}
                    >
                        CSV Preview
                    </h2>
                </div>

                <div
                    style={{
                        background: "#dbeafe",
                        padding: "10px 20px",
                        borderRadius: "20px",
                        color: "#1d4ed8",
                        fontWeight: "bold"
                    }}
                >
                    Total Rows : {data.total_rows}
                </div>
            </div>

            {/* Search */}

            <div
                style={{
                    position: "relative",
                    marginBottom: "20px"
                }}
            >
                <FaSearch
                    style={{
                        position: "absolute",
                        left: "15px",
                        top: "15px",
                        color: "gray"
                    }}
                />

                <input
                    type="text"
                    placeholder="Search records..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "12px 12px 12px 45px",
                        borderRadius: "8px",
                        border: "1px solid #ccc"
                    }}
                />
            </div>

            {/* Table */}

            <div
                style={{
                    overflowX: "auto"
                }}
            >
                <table
                    style={{
                        width: "100%",
                        borderCollapse: "collapse"
                    }}
                >
                    <thead>

                        <tr
                            style={{
                                background: "#2563eb",
                                color: "#fff"
                            }}
                        >
                            {columns.map((column) => (
                                <th
                                    key={column}
                                    style={{
                                        padding: "12px",
                                        border: "1px solid #ddd"
                                    }}
                                >
                                    {column}
                                </th>
                            ))}
                        </tr>

                    </thead>

                    <tbody>

                        {rows.length === 0 ? (

                            <tr>

                                <td
                                    colSpan={columns.length}
                                    style={{
                                        textAlign: "center",
                                        padding: "20px"
                                    }}
                                >
                                    No Records Found
                                </td>

                            </tr>

                        ) : (

                            rows.map((row, index) => (

                                <tr key={index}>

                                    {columns.map((column) => (

                                        <td
                                            key={column}
                                            style={{
                                                padding: "10px",
                                                border: "1px solid #ddd",
                                                textAlign: "center"
                                            }}
                                        >
                                            {row[column]}
                                        </td>

                                    ))}

                                </tr>

                            ))

                        )}

                    </tbody>

                </table>
            </div>
        </div>
    );
}

export default PreviewTable;