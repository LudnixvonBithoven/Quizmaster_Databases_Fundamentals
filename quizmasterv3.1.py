#######################################################################
#                                                                     #
#                         Quizmaster v3.1 by James                    #
#                                                                     #
#######################################################################

import random as rnd


question1 = {"print([0, 1, [2, 3]][1:])) would result in?": \
                ["[1, [2, 3]]", "[1]", \
                 "typeError: 'int' object is not subscriptable",
                 "[2, 3]",
                 "DatatypeError: 'list' object is not subscriptable", \
                 "[1, []]`", "[1, 2, 3]"]}

question2 = {"print(type({})) would result in?":\
                ["<class 'dict'>", "<class 'set'>", \
                 "<class 'list'>", "dict", \
                 "{}", "```dict()```", \
                "print('NameError: name '{}' is not defined')"]}

question3 = {"How do you insert COMMENTS in Python code?":\
                ["#This is a comment", "/*This is a comment*/", \
                 "//This is comment", "<!-- This is a comment -->", \
                 "###This is a comment", "```This is a comment```", \
                "print('This is a comment')"]}


def convert_data(questions_list):
    """convert_data(questions_list) -> str, list, str
    
    Random picking a question from questions_list
    Randomize values from gives question/key
    Only called by the function question
    """
    rnd_question_ans = rnd.choices(questions_list)[0]
    # Unpack question key
    question_key = list(rnd_question_ans.keys())[0]
    values_in_nested_list = list(rnd_question_ans.values())
    # Unpack nested values
    values_listed = values_in_nested_list[0]
    val_of_question = rnd_question_ans.get(question_key)
    # Correct value from given key
    correct_ans = val_of_question[0]

    return question_key, values_listed, correct_ans


def question(questions_list):
    """question(questions_list) --> list
    
    Handeling the options
    Prompting answer from user
    validate the answer
    """
    # Call and unpack the convert_data function
    question, val_of_question, correct_ans = convert_data(questions_list)
    # Prints the given question - random question
    print(f"{question}\n")
    answers_in_list = rnd.sample(val_of_question, 3)
    # Prevents the correct answer to be added twice
    if correct_ans in answers_in_list:
        is_in_loop = True
        while is_in_loop:
            if correct_ans in answers_in_list:
                # Create a new random values list
                answers_in_list = rnd.sample(val_of_question, 3)
            else:
                answers_in_list.append(correct_ans)
                is_in_loop = False
    else:
        answers_in_list.append(correct_ans)
        
    rnd.shuffle(answers_in_list)
    for idx, ans in enumerate(answers_in_list):
        print(f"{idx}){ans}")

    try:
        answer_from_user = int(input("Answer: \n"))
    except ValueError as e:
        print(e)
    else:
        if correct_ans.lower() == answers_in_list[answer_from_user].lower():
            print(f"\n{answer_from_user} is correct\n")
        else:
            print(f"\nIncorrect, the right answer: {correct_ans}\n")
    
    return question_list

is_in_loop = True
if __name__ == "__main__":
    while is_in_loop:
        menu_dict = {1: question([question1, question2, question3]), 2: False}
        try:
            opt = int(input("1)Question 2)Quit\n"))
            is_in_loop = menu_dict[opt]
        except (KeyError, ValueError) as e:
            print(e)
            break
