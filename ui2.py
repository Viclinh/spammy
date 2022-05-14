from obstaclefunction import Question

question_arr = ["What is a phishing attack called when it is designed to look like an email from a user's superior within the organization?\n a. Whale phishing \n b. Spear phishing \n c. Deceptive phishing \n d. In-session phishing \n\n", 
"How is mobile phishing security different from PC and laptop phishing security?\n a. Mobile phishing attacks are extremely rare \n b. Email filters don't work on mobile devices \n c. Users can't preview suspicious links \n d. Attackers target mobile devices twice as much as laptops \n\n",
"Which of the following options is the most effective way to improve email phishing security?\n a. A phishing test \n b. A corporate firewall \n c. Two-factor authentication  \n d. A virtual private network  \n\n",
"Who are the targets of whaling phishing attacks?\n a. Intro-level employees \n b. Executives \n c. Middle management \n d. IT professionals \n\n",
"Which of the following practices should IT employ for an email phishing test?\n a. Include executives and management  \n b. Mimic the tactics of typical phishing attacks \n c. Extract as much user data as possible \n d. All of the above \n\n"
]

questions = [Question(question_arr[0],"b"),
Question(question_arr[1],"c"),
Question(question_arr[2],"c"),
Question(question_arr[3],"b"),
Question(question_arr[4],"d")
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