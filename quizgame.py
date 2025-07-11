questions=(" Which planet is known as the Red Planet?",
           " Who invented the light bulb?",
           " What is the largest mammal in the world?",
           " Which is the smallest prime number?",
           " What is the capital of Japan?",
           )
options=(("A.MARS","B.EARTH","C.VENUS","D.SATURN"),
        ("A. ALBERT EINSTEIN","B. Thomas Edison","C. Nikola Tesla","D. Isaac Newton"),
        ("A. African Elephant","B. Human","C. Blue Whale","D. Hippopotamus"),
        ("A. 0","B. 1","C. 2","D. 4") ,
        ("A. Tokyo","B. Beijing","C. Seoul","D. Bangkok"),
        )
answers=("A","B","C","C","A")
guesses=[]
score=0
question_number=0

for question in questions:
    print("--------------------------------")
    print(question)
    for optaion in options[question_number]:
        print(optaion)
    guesses=input("Enter (A, B, C, D): ").upper()
    if guesses==answers[question_number]:
        score=score+1
        print("correct")
    else:
        print("incorrect")    
        print(f"{answers[question_number]} is the correct answer")
    question_number=question_number+1
    
print("--------------------------------")    
print("------------RESULT--------------")
print("--------------------------------")  

score=score/len(questions)*100
print(f"your score {score}%")