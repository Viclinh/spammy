from obstaclefunction import Question

question_arr = ["In _______________ some cyber-criminals redirect the legitimate users to different phishing sites and web pages via emails, IMs, ads and spyware?\n a. URL Redirection \n b. DoS \n c. Phishing \n d. MiTM attack \n\n", 
"Which of the following type of data, phishers cannot steal from its target victims?\n a. bank details \n b. phone number \n c. passwords \n d. apps installed in the mobile \n\n",
"______________ was the first type of phishing where the phishers developed an algorithm for generating random credit card numbers\n a. Email-based phishing \n b. Algo-based phishing \n c. Deceptive phishing \n d. Angler Phishing  \n\n",
"Victims of phishing are mostly__________\n a. Tech enthusiast \n b. Professional computer engineers \n c. Lack of computer knowledge \n d. Lack of management skill \n\n",
"Phishers often develop ______________ websites for tricking users & filling their personal data\n a. legitimate \n b. illegitimate \n c. genuine \n d. official \n\n"
]

questions = [Question(question_arr[0],"c"),
Question(question_arr[1],"d"),
Question(question_arr[2],"b"),
Question(question_arr[3],"c"),
Question(question_arr[4],"b")
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