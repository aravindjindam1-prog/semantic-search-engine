# Semantic Search Engine

This project implements a semantic search engine using FastAPI for the backend and Streamlit for the frontend. It features hybrid retrieval and embeddings using sentence-transformers.

## Directory Structure  
- backend/  
  - app.py  
  - models.py  
  - retrieval.py  
  - embeddings.py  
  - utils.py  
  - sample_data/  
- frontend/  
  - app.py  
  - pages/  
  - assets/  
- .env  
- .gitignore  
- README.md  
- run.sh  

## Installation  
1. Clone the repository.
2. Install backend dependencies.  
   `pip install fastapi sentence-transformers uvicorn`
3. Install frontend dependencies.  
   `pip install streamlit`
4. Run the servers as follows:
   - Backend: `uvicorn backend.app:app --reload`
   - Frontend: `streamlit run frontend/app.py`  

## API Documentation  
Refer to the API documentation for detailed information on how to use the API endpoints.
