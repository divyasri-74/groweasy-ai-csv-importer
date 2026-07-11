import React from "react";

function Loader() {

    return (

        <div
            style={{
                textAlign: "center",
                marginTop: "40px"
            }}
        >

            <h2
                style={{
                    color: "#2563eb"
                }}
            >
                🤖 AI Processing...
            </h2>

            <div
                style={{
                    width: "300px",
                    height: "12px",
                    background: "#ddd",
                    margin: "20px auto",
                    borderRadius: "20px",
                    overflow: "hidden"
                }}
            >

                <div
                    style={{
                        width: "100%",
                        height: "100%",
                        background: "#2563eb",
                        animation: "loading 2s infinite"
                    }}
                />

            </div>

            <p>Please wait while AI extracts CRM fields...</p>

        </div>

    );

}

export default Loader;