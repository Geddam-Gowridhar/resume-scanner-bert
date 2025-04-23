from flask import Flask, request, render_template
from utils import extract_resume_text  # Ensure this utility function is defined
from bert_resume_matcher import get_similarity_score  # Ensure this function is defined

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    error_message = None

    if request.method == 'POST':
        if 'resume' not in request.files:
            error_message = "No file part"
        else:
            file = request.files['resume']
            if file.filename == '':
                error_message = "No selected file"
            elif file and file.filename.endswith('.pdf'):
                file.save("temp_resume.pdf")  # Save the uploaded file
                try:
                    # Extract text from the resume PDF
                    resume_text = extract_resume_text("temp_resume.pdf")
                    job_description = request.form.get('job_desc', '')  # Get job description from form
                    if job_description:
                        # Calculate the similarity score
                        score = get_similarity_score(resume_text, job_description)
                        score = float(score)  # Ensure score is a float
                    else:
                        error_message = "Please provide a job description."
                except Exception as e:
                    error_message = str(e)  # Capture the error message
            else:
                error_message = "File is not a PDF"

    return render_template('index.html', score=score, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)