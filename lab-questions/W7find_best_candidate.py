"""
Write a function called find_best_candidate, with the following
definition:
    find_best_candidate(file_name)
    
    Arguments:
    ----------
    file_name : string

    Returns:
    --------
    "candidate_name, score" : string

find_best_candidate will take a file in which there will be a list of
candidate_names, graduation, entrance exam, interview and ALES exam
scores, and return the name and the total score of the highest graded
candidate.

Formatting of the file is as follows:
<candidate name> <graduation_score> <entrance> <interview> <ales_score>
<candidate name> <graduation_score> <entrance> <interview> <ales_score>
<candidate name> <graduation_score> <entrance> <interview> <ales_score>

Candidate name can consists of 2 or 3 words separatedy by spaces ' '.
Names and scores are separated by spaces ' '.

The total score of a candidate is calculated like this:
30% - Graduation Score
30% - Entrance Exam Score
30% - Interview Score
10% - ALES Exam Score
All scores are floating point numbers between 0.0 and 100.0.

Example:
--------
>>> print(find_best_candidate(candidates.csv))
Linus Torvalds: 100%
"""

# My Solution

def find_best_candidate(fName):
    highest = ["", 0]
    with open(fName, 'r') as candidates:
        for line in candidates:

            if not line:
                continue

            line = line.strip()
            parts = line.rsplit(' ', 4)

            candidate_name_raw = parts[0]
            graduation_score_raw = parts[1]
            entrance_exam_score_raw = parts[2]
            interview_score_raw = parts[3]
            ales_score_raw = parts[4]

            candidate_name = candidate_name_raw.strip()
            try:
                graduation_score = float(graduation_score_raw)
            except ValueError:
                graduation_score = None
                print(f"Non-numerical graduation score on line : {line}. Skipping")
                continue
            try:
                entrance_exam_score = float(entrance_exam_score_raw)
            except ValueError:
                entrance_exam_score = None
                print(f"Non-numerical entrance exam score on line : {line}. Skipping")
                continue
            try:
                interview_score = float(interview_score_raw)
            except ValueError:
                interview_score = None
                print(f"Non-numerical interview score on line : {line}. Skipping")
                continue
            try:
                ales_score = float(ales_score_raw)
            except ValueError:
                ales_score = None
                print(f"Non-numerical ALES score on line : {line}. Skipping")
                continue

            """
            The above try-except blocks can be done in a single block:
            `
            try:
                ales_score = float(ales_score_raw)
                graduation_score = float(graduation_score_raw)
                entrance_exam_score = float(entrance_exam_score_raw)
                interview_score = float(interview_score_raw)
            except ValueError:
                ales_score = None
                graduation_score = None
                entrance_exam_score = None
                interview_score = None
                print(f"Non-numerical exam score on line : {line}. Skipping.")
                continue
            `
            but this is bad practice since we don't know which value is
            non-numerical in that line.
            """

            total_score = (graduation_score*0.3 +
                           entrance_exam_score*0.3 +
                           ales_score*0.3 +
                           interview_score*0.1)

            if type(total_score) is float and total_score > highest[1]:
                highest[0] = candidate_name
                highest[1] = total_score


        return_string = f"{highest[0]}: {highest[1]}%"

        if highest[1] is not None:
            return return_string
        else:
            return "An error occurred, there is no valid score."

print(find_best_candidate("candidates.csv"))
