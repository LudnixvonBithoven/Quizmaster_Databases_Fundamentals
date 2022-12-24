#######################################################################
#                                                                     #
#                         Quizmaster v3.2 by James                    #
#                                                                     #
#######################################################################

import random as rnd


question1 = {"print([0, 1, [2, 3]][1:])) would result in?":\
                ["[1, [2, 3]]", "[1]",\
                 "typeError: 'int' object is not subscriptable",
                 "[2, 3]",
                 "DatatypeError: 'list' object is not subscriptable",\
                 "[1, []]`", "[1, 2, 3]"]}

question2 = {"print(type({})) would result in?":\
                ["<class 'dict'>", "<class 'set'>",\
                 "<class 'list'>", "dict",\
                 "{}", "```dict()```",\
                "print('NameError: name '{}' is not defined')"]}

question3 = {"How do you insert COMMENTS in Python code?":\
                ["#This is a comment", "/*This is a comment*/",\
                 "//This is comment", "<!-- This is a comment -->",\
                 "###This is a comment", "```This is a comment```",\
                "print('This is a comment')"]}


def convert_data(questions_dict):
    """convert_data(questions_dict) -> str, list, str
    
    Random picking a question from questions_dict
    Randomize values from gives question/key
    Only called by the function question
    """

    all_keys = list(questions_dict.keys())
    random_key = rnd.choices(all_keys)[0]
    question_answers = questions_dict.get(random_key)
    # Note: check if listing and unpacking is needed
    question = list(question_answers.keys())[0]
    answers = list(question_answers.values())[0]
    correct_answer = answers[0]

    return random_key, question, answers, correct_answer

def question(questions_dict):
    """question(questions_dict) --> dict
 
    Handeling the options
    Prompting answer from user
    validate the answer
    """
    # Call and unpack the convert_data function
    convert_data(questions_dict)
    rnd_key, question, answers, correct_answer = convert_data(questions_dict)
    
    # Prints the given question - random question
    print(f"{question}\n")
    answers_in_list = rnd.sample(answers, 3)
    # Prevents the correct answer to be added twice
    if correct_answer in answers_in_list:
        is_in_loop = True
        while is_in_loop:
            if correct_answer in answers_in_list:
                # Create a new random values list
                answers_in_list = rnd.sample(answers, 3)
            else:
                answers_in_list.append(correct_answer)
                is_in_loop = False
    else:
        answers_in_list.append(correct_answer)

    rnd.shuffle(answers_in_list)
    for idx, ans in enumerate(answers_in_list):
        print(f"{idx}) {ans}")

    try:
        answer_from_user = int(input("Answer: \n"))
    except ValueError as e:
        print(e)
    else:
        if correct_answer.lower() == answers_in_list[answer_from_user].lower():
            print(f"\n{answer_from_user} is correct\n")
        else:
            print(f"\nIncorrect, the right answer: {correct_answer}\n")
        
    return questions_dict.pop(rnd_key, "key to remove not found")

is_in_loop = True
if __name__ == "__main__":
    # Note: this block needs a better looking logic
    questions_dict = {"q1": question1, "q2": question2, "q3": question3}
    while is_in_loop:
        # If the questions dictionary isn't empty
        if questions_dict:
            # Creating a menu with a dictionary
            menu_dict = {1: question(questions_dict), 2: False}
            try:
                opt = int(input("1)Question 2)Quit\n"))
                is_in_loop = menu_dict[opt]
            except (KeyError, ValueError) as e:
                print(e)
        else:
            # Reload the questions list if empty
            questions_dict = {"q1": question1, "q2": question2, "q3": question3}
