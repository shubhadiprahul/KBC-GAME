import json
import os
import time
from threading import Timer

ans_key = ['','D','C','B','C','A','D','D','A','A','B']
options = ['A','B','C','D']
money = [0,3000,5000,10000,20000,80000,120000,500000,1200000,5000000]
life_line_list = ['50-50','phone a friend','audience poll']

def user_choice():
     player_choice = input("Enter your Choice: ")
     return player_choice


def life_line(index):
    counter = 0
    if len(life_line_list) == 0:
        print("Sadly you loss your all life lines.")
    else:
        while counter==0:
            print("\nYou have Some Life-line like ",life_line_list,"\n")
            player_choice = input("Choose life line: ")
            if '50-50' in player_choice:
                print("You chooses " + player_choice + "\n")
                print("Wait for computer response....\n")
                time.sleep(2)
                correct_answer = ans_key[index]
                for i in options:
                    if i != correct_answer:
                        print( "The remaining options are "+ correct_answer + " and " + i)
                        life_line_list.remove(player_choice)
                        break
                break
            elif 'phone a friend' in player_choice:
                print("You chooses " + player_choice + "\n")
                print('''Your friends are:\nBill Gates\nSteve Jobs\nNarendra Modi\n''')
                call_choice = input("Whom you want to call: ").title()
                print("We are connecting to " + call_choice + "......\n")
                time.sleep(3)
                print("The " + call_choice + " said the answer is " + ans_key[index])
                life_line_list.remove(player_choice)
                break
            elif 'audience poll' in player_choice:
                print("You chooses " + player_choice + "\n")
                print("Wait for auidence reply.....\n")
                time.sleep(3)
                highest = ans_key[index] + " : 55%"
                for i in range(len(options)):
                    if options[i] != ans_key[index]:
                        if i == 0:
                            print(options[i] + ' : 15%')
                        elif i == 1:
                            print(options[i] + ' : 10%')
                        elif i == 2:
                            print(options[i] + ' : 20%')
                        elif i == 3:
                            print(options[i] + ' : 5%')
                    else:
                        print(highest)
                life_line_list.remove(player_choice)
                break
            else:
                print("Enter correct Choice!")
                counter=counter


def check_answer(qes_count,player_choice):
    if qes_count == 1 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 2 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 3 and player_choice == ans_key[qes_count]:
        print("You Crossed  First Level of the Game")
        return("You Won " + str(money[qes_count]))
    elif qes_count == 4 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 5 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 6 and player_choice == ans_key[qes_count]:
        print("You Crossed Second Level of the Game")
        return("You Won " + str(money[qes_count]))
    elif qes_count == 7 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 8 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 9 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 10 and player_choice == ans_key[qes_count]:
        return("You Won 1 Crore rupeess")


def play_game():
    qes_count = 0
    counter = 0
    instructions = '''\n.......Welcome to KBC.......\n\n1.You have four options for each question.\n2.You have Life Line also to use it type (life line) simply.\n3.To Quit the game simply type (quit).\n'''
    print(instructions)
    with open('questions.json') as content:
        questions = json.load(content)
        while counter <  len(questions['data']):
            print(questions['data'][counter]['question'])
            print(questions['data'][counter]['answer'],"\n")
            player_choice = user_choice().upper()
            
            if 'QUIT' in player_choice:
                print("Thanks For Playing Nicely! You Won "+ str(money[counter])  + " Rupess")
                break
            if 'LIFE LINE' in player_choice:
                life_line(counter+1)
                time.sleep(5)
            if 'A' in player_choice or 'B' in player_choice or 'C' in player_choice or 'D' in player_choice:
                qes_count+=1
                ans = check_answer(qes_count,player_choice)
                if ans:
                    print(ans + "\n")
                else:
                    print("")
                    print("Sadly! Your answer is Wrong")
                    print("Thanks For Playing Nicely! You Won "+ str(money[qes_count-1])  + " Rupess")
                    break
                counter +=1
                if counter <=9:
                    print("Wait for next question....")
                    time.sleep(2)
                    os.system('clear')
            else:
                os.system('clear')
                print("Enter Valid options! You have options like A or B or C or D :)\n")
                counter = counter
play_game()

