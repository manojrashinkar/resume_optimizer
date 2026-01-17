ATS_PROMPT = """
You are an ATS (Applicant Tracking System) expert.

Resume:
{resume}

Job Description:
{jd}

Skills Required:
{skills}

Tasks:
1. Give ATS score out of 100
2. List missing keywords
3. Suggest exact improvements
4. Mention which sections to modify

Return output in this format:
ATS_SCORE:
MISSING_KEYWORDS:
SECTION_WISE_CHANGES:
FINAL_RECOMMENDATIONS:
"""