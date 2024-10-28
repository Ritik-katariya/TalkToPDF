import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api"
});

export const uploadPDF = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    return api.post("/upload", formData);
};

export const askQuestion = async (documentId, question) => {
    return api.post("/ask", { document_id: documentId, question });
};