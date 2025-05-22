import streamlit as st
import requests
import os

API_BASE = os.environ.get("API_BASE", "http://127.0.0.1:8000")

st.title("📚 Theme Identifier Chatbot")

# --- Document Upload ---
st.header("📤 Upload Documents")
uploaded_files = st.file_uploader("Upload multiple PDFs or Images", accept_multiple_files=True, type=["pdf", "jpg", "jpeg", "png"])
if st.button("Upload"):
    if uploaded_files:
        files = [("files", (f.name, f.read(), f.type)) for f in uploaded_files]
        response = requests.get(f"{API_BASE}/documents/upload", files=files)
        st.success("Uploaded Successfully")
        st.json(response.json())
    else:
        st.warning("No files selected.")


# --- List Uploaded Docs ---
st.header("📄 Uploaded Documents")
if st.button("Refresh Document List"):
    docs = requests.get(f"{API_BASE}/documents/list").json()["documents"]
    for doc in docs:
        st.markdown(f"- **{doc['filename']}** | Doc ID: `{doc['doc_id']}` | Pages: {doc['pages']}")

# --- Ask a Question ---
st.header("💭 Ask a Question")
question = st.text_input("Enter your question:")
selected_doc_ids = st.text_area("Optional: Enter comma-seperated Doc IDs to target specific documents")

if st.button("Submit_Question"):
    doc_id_list = [doc_id.strip() for doc_id in selected_doc_ids.split(",") if doc_id.strip()]
    params = {"doc_ids": doc_id_list} if doc_id_list else {}
    response = requests.post(f"{API_BASE}/query", json={"question": question}, params=params)
    result = response.json()

    st.subheader("🧠 Answer:")
    st.write(result.get("answer", "No answer"))

    st.subheader("🔖 Citations:")
    for cite in result.get("citations", []):
        st.markdown(f"""
        - **Doc ID**: `{cite['doc_id']}`
        - **Page**: {cite['page']} | **Paragraph**: {cite.get('paragraph', '-')}\n
        - _Snippet_: _"{cite['content_snippet']}"_
        """)

# --- Theme Synthesis ---
st.header("🧩 Extract Themes from All Documents")

if st.button("Extract Themes"):
    response = requests.get(f"{API_BASE}/query/themes")
    result = response.json()

    st.subheader("🧠 Identified Themes:")
    if "themes" in result:
        st.text_area("Themes", result["themes"], height=300)
    else:
        st.error("Failed to extract themes.")