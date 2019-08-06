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


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


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
                }
            ]
        }
    ]
    answers = prompt(questions, style=styler())
    return answers


def que2(a):
    global questions
    if a.lower() == 'tag-spammer':
        questions = [
            {
                'type': 'input',
                'message': "Enter post's link: ",
                'name': 'p_link'

            }
        ]
    elif a.lower() == 'profile-spammer':
        questions = [
            {
                'type': 'input',
                'message': "Enter target profile's username: ",
                'name': 'tar_uname'

            }
        ]
    answers = prompt(questions, style=styler())
    return answers

