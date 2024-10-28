import React, { useState } from "react";

import PDFUploadInterface from "./components/home";

function App() {
    const [documentId, setDocumentId] = useState(null);

    return (
        <div>
           
            <PDFUploadInterface></PDFUploadInterface>
        </div>
    );
}

export default App;
