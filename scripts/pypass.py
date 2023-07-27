import random
import tkinter
from argparse import ArgumentParser
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

parser = ArgumentParser()
parser.add_argument('--all',
                    '-a',
                    help='use all characters',
                    action='store_true')

parser.add_argument('--lower',
                    '-l',
                    help='Include lowercase',
                    action='store_true')

parser.add_argument('--upper',
                    '-u',
                    help='Include uppercase',
                    action='store_true')

parser.add_argument('--numbers',
                    '-n',
                    help='Include numbers',
                    action='store_true')

parser.add_argument('--punctuation',
                    '-p',
                    help='Include punctuation characters',
                    action='store_true')

parser.add_argument('--spacebar',
                    '-b',
                    help='Include space character',
                    action='store_true')

parser.add_argument('--size',
                    '-s',
                    help='Password size',
                    type=int,
                    required=True)

parser.add_argument('--verbose',
                    '-v',
                    help='Show password in terminal',
                    action='store_true')


def gen_password(string: str, size: int, show: float):
    pwd = ''.join([random.choice(string) for _ in range(size)])
    if pwd.endswith(' '):
        char = random.choice(string.replace(' ', ''))
        pwd[-1] = char
    if show:
        print(pwd)
    copy_to_clipboard(pwd)
    print("Password in clipboard!")


def copy_to_clipboard(text: str):
    tk = tkinter.Tk()
    tk.clipboard_clear()
    tk.clipboard_append(text)
    tk.update()
    tk.destroy()


args = parser.parse_args()


def main():
    symbols = f'{ascii_lowercase}{ascii_uppercase}{digits}{punctuation} '
    if args.all:
        gen_password(symbols, args.size, args.verbose)
        return
    if not args.lower:
        symbols = symbols.replace(ascii_lowercase, '')
    if not args.upper:
        symbols = symbols.replace(ascii_uppercase, '')
    if not args.numbers:
        symbols = symbols.replace(digits, '')
    if not args.punctuation:
        symbols = symbols.replace(punctuation, '')
    if not args.spacebar:
        symbols = symbols.replace(' ', '')
    gen_password(symbols, args.size, args.verbose)


main()
