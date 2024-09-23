from flask import Flask, request, render_template
from chatgroq_chain import ChatGroqChain
from document_loader import load_document

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyze_application():
    result = None
    if request.method == 'POST':
        try:
            # Process Job Description
            jd_type = request.form['jd_type']
            if jd_type == 'file':
                job_description = load_document(request.files['jd_file'], 'file')
            elif jd_type == 'url':
                job_description = load_document(request.form['jd_url'], 'url')
            else:
                job_description = request.form['jd_text']

            # Process Resume
            resume_type = request.form['resume_type']
            if resume_type == 'file':
                resume = load_document(request.files['resume_file'], 'file')
            elif resume_type == 'url':
                resume = load_document(request.form['resume_url'], 'url')
            else:
                resume = request.form['resume_text']

            # Process with ChatGroqChain
            chatgroq_chain = ChatGroqChain()
            result = chatgroq_chain.process_input(job_description, resume)
            
            # Print the result to console
            print("Analysis Result:", result)
        
        except Exception as e:
            result = {"error": str(e)}
            print("Error:", str(e))

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)