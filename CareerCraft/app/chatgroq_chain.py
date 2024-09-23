from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from config import GROQ_API_KEY

class ChatGroqChain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0, 
            groq_api_key=GROQ_API_KEY, 
            model_name="llama-3.1-70b-versatile"
        )

    def process_input(self, job_description, resume):
        prompt = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### RESUME:
            {resume}

            ### INSTRUCTION:
            Analyze the job description and resume provided. Then:
            1. Generate a professional and personalized cover letter.
            2. Create 5 relevant interview questions based on the job requirements and candidate's experience.
            3. Provide a brief review of the resume, highlighting strengths and areas for improvement.

            Present your analysis in the following JSON format:
            {{
                "cover_letter": "Full text of the cover letter",
                "interview_questions": ["Q1", "Q2", "Q3", "Q4", "Q5"],
                "resume_review": {{
                    "strengths": ["Strength 1", "Strength 2", ...],
                    "weaknesses": ["Weakness 1", "Weakness 2", ...],
                    "suggestions": ["Suggestion 1", "Suggestion 2", ...]
                }}
            }}

            ### OUTPUT (JSON FORMAT):
            """
        )
        chain = prompt | self.llm | JsonOutputParser()
        
        try:
            result = chain.invoke({"job_description": job_description, "resume": resume})
        except OutputParserException as e:
            result = {"error": str(e)}
        except Exception as e:
            result = {"error": f"An unexpected error occurred: {str(e)}"}

        return result