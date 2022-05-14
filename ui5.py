from obstaclefunction import Question

question_arr = ["What kind of phishing is for avoiding anti-phishing filters by using images that contain writing rather than actual text?\n a. Whale phishing \n b. SMiShing \n c. Deceptive phishing \n d. Filter Evasion \n\n", 
"What kind of phishing is for practice of attacking high-profile targets within business. This type of scam is often disguised as a legal subpoena, complaint from a customer or other “executive” issue?\n a. Whale phishing \n b. SMiShing \n c. Angler Phishing \n d. In-session phishing \n\n",
"What kind of phishing is for phishing attack that uses voice over internet protocol technology to spoof caller ID and convince the target to share personal information or financial details?\n a. Whale phishing \n b. Vishing \n c. Deceptive phishing \n d. Angler Phishing  \n\n",
"What kind of phishing is for redirecting traffic from a legitimate website to another, fake website. This involves corruption in DNS server software or the targeting of a local network router?\n a. Whale phishing \n b. Angler Phishing \n c. Deceptive phishing \n d. Pharming \n\n",
"What kind of phishing is for directing targets to falsified product websites and steals their personal information as they input their data?\n a. Angler Phishing \n b. SMiShing \n c. Search Engine Phishing \n d. In-session phishing \n\n"
]

questions = [Question(question_arr[0],"d"),
Question(question_arr[1],"a"),
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