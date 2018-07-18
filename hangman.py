# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


def hangman(word):
    wrong = 0
    input_list = []
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    #print(len(stages))
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        input_list.append(char)   # 入力した単語をリストに入れる
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(rletters)     #答え確認用
        print(("現在分かっている単語：" + " ".join(board)))
        print("\n")
        print("入力した単語：" + ",".join(input_list))   #　入力した単語のリストを記入
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))


        
        if "__" not in board:
            print("\n")
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n")
        #print("\n"
              #.join(stages[0: \
              #wrong+1]))
        print("あなたの負け！正解は{}."
              .format(word))



# page138_List.py
import page138_List as p138L
word =str(p138L.key_select())


hangman(word)



"""        
with open("page138_List.py", "r", encoding="utf-8") as f:
    a = f.read()

print(hangman(a)) 
"""

