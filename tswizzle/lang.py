import os
import tstoken

def main():
    #lexer=BasicLexer()
    #parser=BasicParser()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')
    print('Welcome to Taylor Swift lyrics inspired Esolang!!\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    print('''     ▀█▀ █▀ █░█░█ █ ▀█ ▀█ █░░ █▀▀
     ░█░ ▄█ ▀▄▀▄▀ █ █▄ █▄ █▄▄ ██▄''')
    print('\n')
    print('''     ⣿⣿⣿⣿⡇⡇⢠⣤⣤⠀⣾⣿⣿⠀⣴⣶⡀⣼⣿⣿⠀⣶⣶⡖⢀⣿⣿⠀⣶⣶⣄⠐⣿⣿⡇⣘⣛⣛⣀⣿⣿⣋⣉⣉⣉⣀⡟⢸
     ⣿⣿⣿⣿⢁⣓⣺⣿⣿⣖⣿⣿⣛⣚⣛⣉⣋⣉⣉⠉⢁⣍⠉⠉⠉⠉⠉⠉⠉⡩⡭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣥⣤⣤⣤⣤⣤⣼
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⠋⠁⠈⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢄⡀⡀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⢆⡀⠀⠄⠌⢐⠂⠀⠀⠀⠀⠀⠈⠀⢄⡢⠀⠼⠦⠀⠀⠀⠀⠀⠀⠀⢀⠚⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣁⠀⠈⠶⠹⠄⡊⠈⠡⠤⠀⠀⠀⠀⢀⡀⢤⠌⠂⠐⠀⠀⠀⠀⠀⡀⣄⢰⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡎⠀⠀⠔⠃⠀⠀⠙⠸⣴⣶⡿⢂⠁⣠⠀⠀⠀⠈⠠⠀⠀⠀⠀⠀⠀⡐⢞⡷⡀⠈⢸⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠎⠀⠠⠀⠀⠀⠚⢐⣐⣠⢸⡿⣑⣾⣦⣴⣶⣶⣖⣆⠀⠀⠀⠀⠀⠀⠸⡜⡈⠉⡃⠀⠀⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠂⢹⢶⡸⣷⣿⠃⣾⡽⢲⢻⢿⣿⣿⣿⣞⡷⡆⠀⠀⠀⠀⡷⣰⠡⠀⠀⢁⢰⠁⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⢎⣎⠷⢿⣿⠸⣟⡻⢦⡍⣿⣿⣿⣿⣿⡻⣝⡤⠀⠀⠀⠘⠍⣋⡒⠐⢀⠺⣴⠻⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢎⡻⣭⡿⡖⣠⡸⣦⣴⢻⣿⣿⣯⡗⡷⣌⠲⠩⣢⠀⠄⠂⠈⢜⠤⠀⢁⠂⠝⠸⢩⣟⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⢿⠀⠀⠀⠐⡀⠨⡱⢫⢞⡜⡉⠋⠋⠚⠻⠾⢿⣟⣽⣳⣭⡛⠆⠸⡱⡋⠀⢠⢯⠼⠬⠈⠀⠀⠀⠈⣻⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⠧⠃⠀⢀⢙⡔⡀⢑⢫⣆⠀⣐⣛⠛⡩⠀⣠⣷⣯⠾⣵⢮⡍⠆⠄⠏⢀⠂⠈⢞⠀⡀⠀⠀⠀⠀⠠⣉⢽⣿
     ⣿⣿⣿⣿⣿⣿⣿⢯⣡⠡⠄⠈⣔⠃⠵⠀⠐⢹⡖⣤⣤⡤⣴⣽⣿⣿⢾⡹⢎⡚⠈⠀⠠⢃⠀⠈⢀⠀⠀⠀⠀⠀⠀⠀⠠⠐⣺⣿
     ⣿⣿⣿⣿⣿⣿⣿⣋⠺⠀⡂⠈⠈⠀⠀⠡⠀⠀⠹⢻⣼⡿⡿⣽⢿⡹⠎⠑⠁⢀⢄⠄⠀⠃⠀⠀⠨⠃⠀⠀⠀⠀⡀⠀⠰⠀⣺⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⠝⠃⠐⠀⠂⠀⠄⠀⠀⠀⠀⠈⠉⠛⠉⠃⠈⣤⣴⠺⣽⡿⣷⠀⠌⠂⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⡇⡄⠠⠀⡠⠆⡀⠄⠀⠀⠀⢀⠀⠄⠀⡰⣏⡿⣿⢧⣁⢿⡷⡄⠀⠄⡀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⣀⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣟⡟⢰⡤⠠⠀⠀⠈⡠⠥⠀⠀⠀⠀⠰⢀⠱⣎⡾⣼⢳⣷⣿⡾⣁⠀⠐⡀⠀⠀⠀⠀⠠⠁⢀⠀⢠⣵⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣞⣅⠀⠀⠀⠂⡙⠦⠀⠀⠀⠀⢲⡁⢪⢕⡻⣼⢯⣟⡿⡱⢭⣔⠈⡃⠀⠀⠀⣀⡀⢀⢲⢀⣾⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢆⠎⠀⠄⠊⠀⠀⠀⠀⠀⣌⢧⢣⡓⣎⡷⣿⣿⡿⣥⡟⡷⣿⣦⠈⢄⠀⠐⠀⢀⣠⣿⣾⣿⣿⣿⣿⣿⣿
     ⣿⡿⣟⣿⣽⡧⣾⣿⣻⢧⠆⡀⠀⠀⠀⠀⠀⣐⠞⡼⢬⣳⡿⣭⡻⣸⣿⣽⢯⣾⡽⣿⠿⠡⠀⠀⠡⢴⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⢽⢯⡿⣟⢾⡴⣽⢶⣛⢶⡓⡀⢀⡀⠀⣂⡍⡰⠩⠜⡸⢿⠿⠞⠣⠝⣇⡟⠿⣩⢓⡤⢶⡳⢥⡤⢓⠪⡕⢮⠻⢿⣿⣿⣿⣿⣿⣿
     ⢧⣛⣾⣽⡎⡾⣭⢟⣎⢷⣪⢖⢢⡱⢩⠞⡼⡱⣏⢯⣔⢢⡸⣜⢖⣺⣶⡸⣜⣦⣳⣜⣁⣬⣭⣨⠌⣡⢉⢄⣂⣀⣭⢩⠩⡙⠻⢿''')
    print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    print('''     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢺⡿⠝⠁⠸⠆⠦⠚⠉⠀⣠⠀⠄⠂⠀⠀⢀⠀⠀⡀⣠⢌⢦⣤⡉⠀⠀⠈⢪⣻⠱⡙⠱⡝⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣑⠏⠠⠀⣠⠋⠀⠀⠀⡀⠃⠀⠀⢀⡀⠄⠂⠁⢠⣴⠛⣵⣻⣷⣿⣿⣆⠀⢠⠀⢑⢙⠮⢺⢌⡟⢿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⠟⠝⠊⠀⠠⢣⠞⠡⠀⠀⢤⠢⣠⠒⠊⡉⠀⠀⡠⠔⢉⡮⣪⣾⣯⣿⣽⣿⣟⣿⡄⠂⠀⠀⢁⡈⠸⡢⣢⢽⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⠗⢁⠀⢀⠠⣠⠋⠀⡈⢆⠃⠔⠉⠠⠍⣅⠒⠴⣡⣨⣾⣳⣾⣯⣿⣿⣿⣿⣿⣿⣿⣷⣂⠀⠀⠀⠐⠃⢌⠙⡿⣿⣿⣿
     ⣿⣿⣿⣿⣿⠁⠈⢡⠂⠂⠁⠂⠤⠁⠈⠈⠁⠈⠠⡔⠒⠲⡎⡷⡞⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡶⠀⠀⠄⠉⠁⡆⠷⠊⣿⣿
     ⣿⣿⣿⣿⣿⡀⠀⠀⠀⢠⢠⠠⢀⡠⠀⢇⡀⠀⠠⠼⠿⢷⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⢉⣏⢿⣧⠀⠀⠀⠀⢤⣀⢆⣴⣸⣿
     ⣿⣿⣿⣿⣿⣷⢆⣀⠈⢂⢸⡐⠩⠀⡀⠀⠁⠀⠈⠛⠓⠂⠨⠍⣉⢻⣿⣿⣿⣿⣿⠟⠋⠀⠐⠚⠉⠿⢿⣷⡀⠀⠀⠀⣲⣷⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⡟⣀⢹⠱⣖⡟⠈⢑⡙⡀⠀⠀⠀⠀⠀⠂⠀⠠⠆⠀⣾⣿⣿⣿⡟⢁⠀⠤⠀⠀⠖⠀⣠⣿⣿⠆⠀⠀⠀⠽⣿⣿⣿⣿⣿
     ⣿⣿⡿⢋⣾⣾⠟⣕⡄⡸⢀⠉⠑⠒⠐⠂⠀⠀⢠⣶⣶⣶⣾⣶⣿⣿⣿⣿⣿⣷⣻⣿⣾⣶⣶⣶⣿⣿⣿⣿⡇⠀⠀⠀⢜⢰⡈⣿⣿⣿
     ⣿⣿⣴⢛⣉⣮⣾⣗⣹⣿⣤⠊⠈⠁⡌⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⢄⣡⢞⡴⠈⣿⣿
     ⣿⣿⣿⢦⡿⣿⢿⠫⡕⡡⣿⢙⠞⠞⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢃⣬⠏⣭⣾⣿⣿
     ⣿⣿⣿⣯⢻⢂⠀⠀⠀⢈⢿⢊⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⡿⢿⠏⡿⣘⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠐⢱⣿⣷⣻⣿⣿⣿
     ⣿⣿⣿⢟⣔⣧⠀⠁⢀⣮⠢⠐⠈⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣘⣿⣿⡻⣿⣽⣿⣿
     ⣿⣿⣿⣻⡄⠸⣧⢴⠋⠀⠀⢁⠀⠀⠀⠀⠀⣻⣿⣿⣿⣿⣟⡛⠛⠋⣉⡉⢉⡉⠛⠻⠿⣿⣿⣿⣿⣿⠃⠀⠀⠈⡘⣿⣿⣯⣽⣿⣿⣿
     ⣿⣿⣿⣿⣿⡄⠹⡆⢤⣀⠀⠀⡆⡄⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣄⠀⠄⠡⠉⠄⡀⣠⣿⣿⣿⣿⢟⣷⣧⣆⢀⣬⣷⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⢺⣿⣿⠜⠛⠐⠳⠻⢳⢡⠎⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣶⣦⣵⣤⣴⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⡿⠉⢁⠠⡠⠀⢀⢁⠈⣸⢰⡀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⣰⣷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣯⠾⣜⡪⠞⢻⣽⣧⠊⢀⣰⣠⡼⢁⠄⠀⠀⠀⠀⠀⠠⢡⢟⡿⣿⣿⣿⣿⡿⢟⣫⠰⣍⣶⣿⣿⣮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⢿⠱⠺⣂⠀⠓⠈⢤⣰⢖⡢⢃⣤⠂⠀⠀⠀⠀⠀⠀⠁⢎⢼⣻⣵⣾⣷⢾⣟⣷⣾⣟⣾⣾⣿⣿⣿⣿⣷⣯⣻⢿⣿⣿⣿⣿⣿⣿⣿
     ⣿⡄⠈⠈⣷⡆⡀⢰⠟⣥⠵⠔⠊⡁⠀⠀⠀⠀⠀⠀⠀⢀⠜⠎⣳⢿⡿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣟⡿⣿⣿⣿⣿
     ⣿⡿⠦⡼⢽⠀⣰⠐⡚⠒⢀⣠⠎⢥⠖⠄⠀⠀⠀⠀⠀⡘⣽⣦⢜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿
     ⣻⣿⣿⠝⣠⣾⣿⣥⣩⣗⣞⣕⠛⠚⣠⡔⣦⠀⠀⠀⠀⠀⡝⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣽⣻⢁⢸⣿⣿⣿⣿⣿⣿⣿⣾⣤⣿⣿⢿⠋⢐⠄⢀⠀⠀⣠⡿⡳⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀
     ⣞⠋⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⠉⠀⠀⠉⠸⢄⠀⢀⠜⣩⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
     ⢄⡂⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣝⡼⠀⠈⠀⢘⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠂
     ⠁⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⢠⡴⢋⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⢀⠂⠈
     ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⡾⠊⠄⠀⠂⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠈⠀⠀⠀
     ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢠⠰⠁⠀⡀⠄⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣁⣶⣶⣦⣤⣥⣥⣀⡀⠀⢠⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⢀⠀⠀⠄⠁⠀⠀
     ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣷⣶⢯⡹⣛⣿⠿⢿⣿⣿⣿⣧⣄⠢⢍⣛⢿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠐⠈⠀⠀⠌⠀⠀⠀⠄
     ⣿⣿⣿⣿⣿⣿⣿⡿⠁⠸⠿⢿⠷⣣⣿⣿⣿⣷⣿⣿⣿⣿⣿⣦⡊⢌⢳⢻⣿⣿⣿⣿⠟⠁⠀⠀⢀⠀⠄⠀⠂⠀⠄⠈⢀⠠⠀⠁⠀⠀
     ⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⣴⣤⣤⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⢂⢣⠛⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠄⠀⠀⡀⠀⠀⠁
     ⣿⣿⣿⣿⣿⣿⠇⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠃⠀⠀⠀⠀⠀⡀⠂⠀⢀⠂⠁⢀⠀⠀⠄⠈⠀⠀⠀⠠⠀''')
    
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    print('''     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⢿⠛⠿⣟⠿⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⣿⡿⠛⡿⠿⢿⠋⠻⠉⠿⠛⠻⠉⠏⢛⡿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⠿⠿⢡⢱⢹⣿⠡⢶⣗⡸⠏⠡⢀⡐⢲⠖⣋⣤⣾⣿⣿⣿⣿⡅⢁⣉⠡⢀⡄⠁⢨⠀⡄⢰⠀⡆⢐⠰⠁⠹⠀⠇⠸⠀⡇⠠⠘⣃⢿⣿⣿⣿⣿
     ⣿⠛⣉⡅⠶⢾⠧⠀⠞⢛⡙⣷⣖⢀⣴⠶⣯⣀⣾⢫⣶⣿⣿⣿⣿⣿⣿⣿⠡⣨⠯⢄⣽⡅⢨⣬⣤⣤⣴⣤⣴⣴⣶⣶⣾⣳⣛⣾⣿⣿⣿⣯⣭⣾⣿⣿⣿⣿
     ⣿⣶⣶⡦⣰⠲⠀⢸⢻⣿⣿⣽⣿⣶⣶⣾⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣵⣗⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣷⣦⡦⢡⠎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⡟⠰⢶⠀⠭⢭⡟⠹⣿⢛⡛⢿⢻⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠐⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⡇⡼⢿⣀⣛⢏⣜⡀⡇⣘⠋⡌⢸⣿⢠⣝⣂⡒⠦⡁⠦⡍⣿⣿⣿⣿⣿⣿⣿⣿⣥⣤⣮⠂⣴⡿⠛⠯⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⡯⠤⠌⢁⣋⣂⣙⣹⠛⣷⠑⢲⠶⠪⠭⢧⠭⠤⢍⡓⢀⣿⣿⣿⣿⣿⣿⣿⣏⠋⠕⠁⣨⣴⣈⣴⠈⢰⡍⠄⡋⢰⣸⡿⠿⢿⢻⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣽⣽⣶⣾⣾⣶⣮⣄⡆⣰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣇⣉⣠⣤⣭⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣹⣿⡏⠀⢹⣷⢸⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⡿⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⡼⣸⠀⠡⠋⠉⠁⠾⣅⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣟⠉⡃⢸⣿⠂⡼⠈⠋⠈⣠⠁⠠⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⠿⠇⢈⢿⢏⡄⠀⠀⢀⢠⣾⡃⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠶⠚⠛⢀⠃⠀⣠⠀⠃⠀⣸⣀⣿⣤⠴⣃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⡟⠋⢹⡏⡙⠉⢁⣤⠆⡦⣠⣈⣤⣄⢐⣫⣬⡖⣹⠊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢰⡄⠂⡀⢈⣄⣢⣼⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⠷⠒⣡⢠⡔⣫⣭⣶⣾⣵⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠇⠨⢸⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣔⣚⡥⢊⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠿⡿⠿⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠎⡰⢰⣿⢂⡆⣹⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠿⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡟⣸⢡⢀⣶⠆⡾⢰⡏⣼⣿⣿⣿⣿⣿⣿⣿⡏⠠⢤⣤⠀⡴⠀⠀⢀⣈⠀⢀⡈⠉⠉⠉⠋⠙⠿⠛⠿⠛⠿⠿⠿⢿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢀⠠⡸⠉⠉⡉⢐⡖⠒⡐⡻⠵⠟⠿⡿⢿⣿⣿⣿⣿⣷⣄⣨⣾⣄⣤⣧⡀⣸⡇⡠⣿⠁⣠⠁⡀⠀⢈⠀⠂⡐⠀⣰⠀⠀⡠⢥
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣷⣤⣤⣴⣍⣼⣁⣀⢠⡐⠁⠐⠀⣸⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣦⣾⣧⣰⣿⣄⣀⣩⣾
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠊⡝⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⡿⢍⢻⠿⠻⣟⡟⠋⣍⡳⠋⢀⠀⢻⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠁⢠⠀⠎⠻⠈⠹⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⠀⠸⠡⠘⠃⡸⣔⠘⡏⢣⣄⣈⡘⡌⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣤⣇⣎⣰⠀⠇⠰⢀⡄⠹⢀⠚⠻⠿⠋⡹⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⡀⡇⣷⣶⡆⢆⢿⢻⠏⡈⣿⢹⣧⠑⢹⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣼⣄⣆⣠⠐⠃⡸⢠⡄⠉⢀⠈⠉⠿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣇⠁⣹⢸⣿⣤⣼⢲⣶⣶⣋⣼⣿⣿⣟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣤⣷⣾⣤⣇⣘⠀⠌⠀⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⡛⢃⣾⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿''')
    print('\n\n')
    print('SESSION CREATED.')
    try:
      lid = input("Enter your favourite Taylor Swift Era: ")
      env = {}
      text=""
      code=""
      newtext=""

      while True:
          try:
            text = input(lid + " (Taylor's Version) >>> " )
            command = "I KNOW THE BRAVEST THING I EVER DID WAS RUN "
            newfilepath=""
            try:
              if text.index(command)==0:
                  filename  = text.replace(command, "")
                  if filename.endswith(".tswizzle"):
                      found = False
                      for (root, dirs, files) in os.walk('..', topdown=True):
                          for name in files:
                              if found == False:
                                  if name == filename:
                                    newfilepath = os.path.abspath(os.path.join(root, name))
                                    found = True
                                    break
                                  else:
                                    break
                      if found == False:
                          print('TASK NOT FOUND! (File does not exist.)')
                      else:  
                          print("LOCATION OF YOUR FILE: " + newfilepath + "\nNOW PLAYING...")
                          file = open(newfilepath, mode='r')
                          print("EXTRACTING THE LYRICS...")
                          lctr=0
                          file.seek(0)
                          while True:
                              line = file.readline().strip('\n')
                              lctr+=1
                              if line == 'GOODBYE GOODBYE GOODBYE':
                                  break
                          print("YOUR TASK CONTAINS ",lctr, " LINES OF LYRICS \n")
                          print("TASK IN PROGRESS...\n")
                          file.seek(0)
                          print("CODE OUTPUT: \n")
                          program = ""
                          nl = ""
                          while True:
                              line = file.readline().strip('\n')
                              if line == 'GOODBYE GOODBYE GOODBYE':
                                  break
                              nl = tstoken.translateCode(line)
                              program = program + str(nl) + '\n'
                          exec(program)
                          file.close()
                          print("\nEND OF SONG REACHED.\n")
                          
                  else:
                      print("TASK INVALID! (The file is not of .tswizzle type)")
            except EOFError or KeyboardInterrupt:
                  print("SO I'M LEAVING OUT THE SIDE DOOR.")
                  break
            except ValueError:
                newtext=str(tstoken.translateCode(text))
                exec(newtext)
          except EOFError or KeyboardInterrupt:
              print("SO I'M LEAVING OUT THE SIDE DOOR.")
              break
    except EOFError or KeyboardInterrupt:
          print("SESSION ENDED.")
    
main()
