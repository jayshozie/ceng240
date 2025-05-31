"""
Write a function called find_candidate, with the following definition:
    find_candidate(file_name)
    
    Arguments:
    ----------
    file_name : string

    Returns:
    --------
    "candidate_name, score" : string

find_candidate will take a file in which there will be a list of
candidate_names and ALES scores, and return the name and the score of the
highest graded candidate.

Formatting of the file is as follows:
<candidate name> <ales_score>
<candidate name> <ales_score>
<candidate name> <ales_score>

Candidate name can consists of 2 or 3 words separatedy by spaces.
Candidate names and their respective ALES scores are separated by spaces.

Example:
--------
>>> print(find_candidate(candidates.csv))
Linus Torvalds: 100%
"""

# My Solution

def find_candidate(fName):
    highest = ["", 0]
    with open(fName, 'r') as candidates:
        for line in candidates:

            if not line:
                continue

            line = line.strip()
            parts = line.rsplit(' ', 1)

            candidate_name_raw = parts[0]
            ales_score_raw = parts[1]

            candidate_name = candidate_name_raw.strip()
            try:
                ales_score = float(ales_score_raw)
            except ValueError:
                ales_score = None
                print(f"Non-numerical ALES score on line : {line}. Skipping")
                continue


            if ales_score is not None and highest[1] is not None:
                if ales_score > highest[1]:
                    highest[0] = candidate_name
                    highest[1] = ales_score

            else:
                print(f"Invalid score on line : {line}")


        return_string = f"{highest[0]}: {highest[1]}%"

        if highest[1] is not None:
            return return_string
        else:
            return "An error occurred, there is no valid score."

print(find_candidate("candidates.csv"))
