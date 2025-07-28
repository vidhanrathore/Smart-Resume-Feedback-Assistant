def build_resume_prompt(resume_text):
    prompt =  f"""
You are an expert resume reviewer. Analyze the resume below and provide:
1. Key Strengths
2. Areas of Improvement
3. Suggested Skills to Add
4. Formatting Advice
5. Score out of 100
Keep the above headings short to long as per need and do not add preamble.
Resume:
{resume_text}
"""
    return prompt


if __name__ == "__main__":
    pt = build_resume_prompt("Rimjhim Rathore")
    print(pt)