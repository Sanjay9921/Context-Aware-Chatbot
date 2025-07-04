# modules/database_ops/routes/rag_routes.py

from flask import Blueprint, request, jsonify

from modules.llm_ops.pdf_parser import extract_text_from_pdf
from modules.llm_ops.text_preprocesor import preprocess_text
from modules.llm_ops.qa_engine import generate_answer

from settings.config import Config

rag_blueprint = Blueprint("rag", __name__)

# In-memory store for PDF content
context_chunks = []
full_context = []

@rag_blueprint.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200

@rag_blueprint.route("/upload", methods=["POST"])
def upload_pdf():
    global context_chunks, full_context
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    raw_text = extract_text_from_pdf(file)
    context_chunks = preprocess_text(raw_text)
    full_context = "\n".join(context_chunks[:15])  # Limit to top 15 chunks for context

    return jsonify({
        "message": "PDF processed successfully",
        "total_chunks": len(context_chunks),
        "full_context": full_context[:100] + ".."
    })

@rag_blueprint.route("/ask", methods=["POST"])
def ask_question():
    global context_chunks, full_context
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    if not context_chunks:
        return jsonify({"error": "No context available. Upload a PDF first."}), 400

    answer = generate_answer(full_context, question, model=Config.DEFAULT_MODEL)
    return jsonify({"question": question, "answer": answer})