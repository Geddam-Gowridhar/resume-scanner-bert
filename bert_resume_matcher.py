from sentence_transformers import SentenceTransformer, util

# Load the pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity_score(resume_text, job_description):
    # Encode the resume and job description
    embeddings = model.encode([resume_text, job_description])
    # Calculate cosine similarity
    score = util.cos_sim(embeddings[0], embeddings[1])
    return float(score)