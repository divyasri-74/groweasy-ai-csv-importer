import React from "react";

function Navbar() {
    return (
        <nav
            style={{
                background: "#2563eb",
                color: "white",
                padding: "18px 30px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                boxShadow: "0 2px 8px rgba(0,0,0,0.2)"
            }}
        >
            <div>
                <h2 style={{ margin: 0 }}>
                    🚀 GrowEasy AI CSV Importer
                </h2>

                <small>
                    AI Powered CRM Import Tool
                </small>
            </div>

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    fontWeight: "bold"
                }}
            >
                <span>Upload</span>
                <span>Preview</span>
                <span>Import</span>
            </div>
        </nav>
    );
}

export default Navbar;