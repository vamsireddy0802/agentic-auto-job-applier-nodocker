from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_best_matches(resume_text, jobs):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    matches = []
    for job in jobs:
        job_desc = job['title'] + " " + job['description']
        job_embedding = model.encode(job_desc, convert_to_tensor=True)
        similarity = util.cos_sim(resume_embedding, job_embedding).item()
        if similarity > 0.4:
            job['score'] = round(similarity, 2)
            matches.append(job)
    return sorted(matches, key=lambda x: x['score'], reverse=True)