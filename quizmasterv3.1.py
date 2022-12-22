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
    """convert_data(questions_list) -> str, list, str"""
    rqstion = rnd.choices(questions_list)[0]
    question_key = list(rqstion.keys())[0]
    values_in_nested_list = list(rqstion.values())
    values_in_list = values_in_nested_list[0]
    val_qstion_key = rqstion.get(question_key)
    cval_key = val_qstion_key[0]
        
    return question_key, values_in_list, cval_key


def question(questions_list):
    
    rqstion, val_qstion_key, cval_key = convert_data(questions_list)
    print(rqstion)
    answers_in_list = rnd.sample(val_qstion_key, 3)
    if cval_key in answers_in_list:
        n = True
        while n:
            if cval_key in answers_in_list:
                # Create a new random values list
                answers_in_list = rnd.sample(val_qstion_key, 3)
            else:
                answers_in_list.append(cval_key)
                n = False
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
        if (cval_key.lower() 
                    == answers_in_list[answer_from_user].lower()):
            print(f"\n{answer_from_user} is correct\n")
        else:
            print(f"\n{answer_from_user} is incorrect\n")
            
    return questions_list

n = True
if __name__ == "__main__":
    while n:
        dct = {1: question([question1, question2, question3]), \
               2: False}
        try:
            opt = int(input("1)Question 2)Quit\n"))
            n = dct[opt]
        except (KeyError, ValueError) as e:
            print(e)
            break
