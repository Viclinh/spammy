from obstaclefunction import Question

question_arr = ["What kind of phishing is for using cell phone text messages as bait to cause the target to divulge sensitive personal information?\n a. Whale phishing \n b. SMiShing \n c. Deceptive phishing \n d. In-session phishing \n\n", 
"What kind of phishing is for posing as a member of a company’s customer support team on social media in an attempt to lure the intended target to share personal information, including login credentials?\n a. Whale phishing \n b. SMiShing \n c. Angler Phishing \n d. In-session phishing \n\n",
"What kind of phishing is for replicating a previously delivered/received message in order to create a seemingly legitimate communication.?\n a. Whale phishing \n b. Clone Phishing \n c. Deceptive phishing \n d. Angler Phishing  \n\n",
"What kind of phishing is for changing all or part of the content found within the page of an otherwise reliable website, which is then used to redirect the target to another website designed to obtain their personal information?\n a. Whale phishing \n b. Angler Phishing \n c. Deceptive phishing \n d. Content Injection Phishing \n\n",
"What kind of phishing is for collecting personal information by hiding in-between a legitimate website and a phishing system and traces details as they are entered?\n a. Angler Phishing \n b. SMiShing \n c. Man-in-the-Middle Phishing \n d. In-session phishing \n\n"
]

questions = [Question(question_arr[0],"b"),
Question(question_arr[1],"c"),
Question(question_arr[2],"b"),
Question(question_arr[3],"d"),
Question(question_arr[4],"c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("\nCorrect!\n\n")
        else:
            print ("\nWrong!\n\n")
    print ("You got " + str(score) + " out of " + str(len(questions)) + " correct!")

run_quiz(questions)