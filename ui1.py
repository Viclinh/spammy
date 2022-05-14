from obstaclefunction import Question

question_arr = ["Which one of the following can be considered as the class of computer threats?\n a. Phishing \n b. Dos Attack \n c. Soliciting \n d. Both B and C \n\n", 
"Which of the following usually observe each activity on the internet of the victim, gather all information in the background, and send it to someone else?\n a. Malware \n b. Spyware \n c. Adware \n d. All of the above \n\n",
"Which one of the following is actually considered as the first computer virus?\n a. Sasser \n b. Blaster \n c. Creeper \n d. Both A and C \n\n",
"To protect the computer system against the hacker and different kind of viruses, one must always keep _________ on in the computer system?\n a. Firewall \n b. Antivirus \n c. Vlc player \n d. Script \n\n",
"Which of the following are famous and common cyber-attacks used by hackers to infiltrate the user's system?\n a. DDos and Derive-by Downloads \n b. Malware & Malvertising \n c. Phishing and Password attacks \n d. All of the above \n\n"
]

questions = [Question(question_arr[0],"b"),
Question(question_arr[1],"b"),
Question(question_arr[2],"c"),
Question(question_arr[3],"a"),
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