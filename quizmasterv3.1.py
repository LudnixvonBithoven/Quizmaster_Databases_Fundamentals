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
    
    - Random picking a question from question_list
    - Randomize values from gives question/key
    - Only called by the function question
    """
    rqstion = rnd.choices(questions_list)[0]
    # Note - This part needs to be updated
    question_key = list(rqstion.keys())[0]
    # -----------------------------------
    values_in_nested_list = list(rqstion.values())
    # Unpack nested values
    values_in_list = values_in_nested_list[0]
    val_qstion_key = rqstion.get(question_key)
    # Correct value from given key
    cval_key = val_qstion_key[0]

    return question_key, values_in_list, cval_key


def question(questions_list):
    """question(question_list) -> list
    
    - Calls convert_data with question_list as an argument
    - Handeling the options
    - Prompting answer from user
    - validate the answer
    """
    # Call and unpack the convert_data function
    rqstion, val_qstion_key, cval_key = convert_data(questions_list)
    # Prints the given rqstion - random question
    print(rqstion)
    answers_in_list = rnd.sample(val_qstion_key, 3)
    # Prevents the correct answer to be added twice
    if cval_key in answers_in_list:
        is_in_loop = True
        while is_in_loop:
            if cval_key in answers_in_list:
                # Create a new random values list
                answers_in_list = rnd.sample(val_qstion_key, 3)
            else:
                answers_in_list.append(cval_key)
                is_in_loop = False
    else:
        answers_in_list.append(cval_key)
        
    rnd.shuffle(answers_in_list)
    for idx, ans in enumerate(answers_in_list):
        print(f"{idx}){ans}")

    try:
        answer_from_user = int(input("Answer: "))
    except ValueError as e:
        print(e)
    else:
        if cval_key.lower() == answers_in_list[answer_from_user].lower():
            print(f"\n{answer_from_user} is correct\n")
        else:
            print(f"\nIncorrect, the right answer: {cval_key}\n")
            
    return questions_list

is_in_loop = True
if __name__ == "__main__":
    while is_in_loop:
        dct = {1: question([question1, question2, question3]), 2: False}
        try:
            opt = int(input("1)Question 2)Quit\n"))
            is_in_loop = dct[opt]
        except (KeyError, ValueError) as e:
            print(e)
            break
