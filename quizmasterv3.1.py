#######################################################################
#                                                                     #
#                         Quizmaster v3.1 by James                    #
#                                                                     #
#######################################################################

import random as rnd


question1 = {"print([0, 1, [2, 3]][1:])) would result in?":\
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
    randomize the quiz sequence.
    """
    rqstion = rnd.choices(questions_list)[0]
    question_key = list(rqstion.keys())[0]
    values_in_nested_list = list(rqstion.values())
    values_in_list = values_in_nested_list[0]
    val_qstion_key = rqstion.get(question_key)
    cval_key = val_qstion_key[0]
        
    return question_key, values_in_list, cval_key


def question(questions_list):
    """question_list --> list"""
    rqstion, val_qstion_key, cval_key = convert_data(questions_list)
    # print question
    print(rqstion)
    # Returning randomized 3 answers in list 
    answers_in_list = rnd.sample(val_qstion_key, 3)
    if cval_key in answers_in_list:
        n = True
        while n:
            # If the right answers already is in the answers list
            if cval_key in answers_in_list:
                # answers_in_list must have 3 randomized answers in list
                answers_in_list = rnd.sample(val_qstion_key, 3)
            else:
                # exit the while loop
                n = False
    else:
        # Add the answer in the answers_in_list
        answers_in_list.append(cval_key)
        
    # Shuffle the 4 answers in answers_in_list
    rnd.shuffle(answers_in_list)

    # Print the values with the index number
    # Index number is used for picking an answer
    for idx, ans in enumerate(answers_in_list):
        print(f"{idx}){ans}")

    try:
        answer_from_user = int(input("Answer: "))
    except ValueError as e:
        # Except needs more attention and depth
        print(e)
    else:
        # If input value is accepted, validate the answer
        if (cval_key.lower() 
                    == answers_in_list[answer_from_user].lower()):
            print(f"\n{answer_from_user} is correct\n")
        else:
            print(f"\n{answer_from_user} is incorrect\n")
            
    return questions_list

n = True
if __name__ == "__main__":
    while n:
        # Trying a dictionary for creating a menu
        dct = {1: question([question1, question2, question3]), \
               2: False}
        try:
            opt = int(input("1)Question 2)Quit\n"))
            n = dct[opt]
        except (KeyError, ValueError) as e:
            print(e)
            break
