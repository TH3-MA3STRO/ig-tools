from pyfiglet import Figlet

f = Figlet(font='slant')

from PyInquirer import Validator, ValidationError

print(f.renderText('ig - tools'))
from PyInquirer import style_from_dict, Token, prompt

print('''
********************************************************
*                                                      *
*    Author: TH3-MA3STRO                               *
*    Instagtam: @th3_ma3stro                           *
*    GitHub: https://www.github.com/TH3-MA3STRO        *
*    Platform: Linux                                   *
*                                                      *
********************************************************
''')



def styler():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })
    return style


def que1():
    questions = [
        {
            'type': 'list',
            'message': 'Select the tool you wish to you use:',
            'name': 'tch',
            'choices': [
                {
                    'name': 'Tag-Spammer'
                },
                {
                    'name': 'Profile-Spammer'
                },
                {
                    'name': 'DP-Downloader'
                }
            ]
        }
    ]
    answers = prompt(questions, style=styler())
    return answers


def que2(a):
    if a.lower() == 'tag-spammer':
        question2 = [
            {
                'type': 'input',
                'message': "Enter post's link: ",
                'name': 'p_link'

            }
        ]
    elif a.lower() == 'profile-spammer':
        question2 = [
            {
                'type': 'input',
                'message': "Enter target profile's username: ",
                'name': 'tar_uname'
            }
        ]
    elif a.lower() == 'dp-downloader':
        question2 = [
            {
                'type': 'input',
                'message': "Enter profile's username: ",
                'name': 'username'
            }
        ]
    answers = prompt(question2, style=styler())
    return answers

