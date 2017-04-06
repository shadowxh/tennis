def comp101_tiebreaker2(points,server):
    # each point respersented by the integer 0 or 1 indicating that Player0 or Player1 won the given point,server takes value 0 or 1 ,indicating that Player 0 or Player 1
    player0=0
    player1=0
    remainder=points.copy()
    # test the points and check the point of each player the gain and list of the remainder
    while remainder:
        if remainder[0]==server:
            player0=player0+1
        elif remainder[0]==1-server:
            player1=player1+1
        remainder=remainder[1:]
        if (player0>=7 or player1>=7) and abs(player0-player1)>=2:
            break
   # when player0>=7 or player1>=7 and abs(player0-player1)>2,game over
    if player0>=7 and (player0-player1)>=2:
        winner=server
    elif player1>=7 and (player1-player0)>=2:
        winner=1-server
    else:
        winner=None
    return (str(player0)+"-"+str(player1),winner,remainder)


def comp101_game2(points, server):
    player0=0
    player1=0
    has_winner=False
    remainder=points
    for elem in points:
        if elem==0:
            player0+=1
        elif elem==1:
            player1+=1
        remainder=remainder[1:]
        if player0==4 and player1==4:
            player0=player0-1
            player1=player1-1
       
        if (player0>3 or player1>3) and abs(player0-player1)>=2:
            has_winner=True
            break
    player0_score, player1_score = convert_score(player0, player1, has_winner)
    if server==0:
        score=player0_score+'-'+player1_score
    elif server==1:
        score=player1_score+'-'+player0_score

    if has_winner:
        if player0>player1:
            winner=0
        elif player1>player0:
            winner=1
    else:
        winner=None
    return (score, winner, remainder)
        
    

def convert_score(player0, player1, has_winner):
    if player0>=3 and player1>=3:
        return convert_without_40(player0, has_winner), convert_without_40(player1, has_winner)
    else:
        return convert_with_40(player0, has_winner), convert_with_40(player1, has_winner)


## 40 !=> w
def convert_without_40(player, has_winner):
    if player == 0:
        return "0"
    elif player == 1:
        return "15"
    elif player == 2:
        return "30"
    elif player == 3:
        return "40"
    elif player >= 4:
        if has_winner:
            return "W"
        else:
            return "Ad"

## 40 => w
def convert_with_40(player, has_winner):
    if player == 0:
        return "0"
    elif player == 1:
        return "15"
    elif player == 2:
        return "30"
    elif player == 3:
        if has_winner:
            return "W"
        else:
            return "40"
    elif player >= 4:
        if has_winner:
            return "W"
        else:
            return "Ad"


# (score, winner, remainder)
def my_comp101_tiebreaker(points, server, wins=7):
    player0 = player1 = 0
    remainder = points[:]
    index = 0
    while index < len(points):
        if points[index] == server:
            player0 += 1
        else:
            player1 += 1
        index += 1
        diff = abs(player0 - player1)
        if max(player0, player1) >= wins and diff >= 2:
            break
    winner = None
    if player0 >= wins and diff >= 2:
        winner = server
    elif player1 >= wins and diff >= 2:
        winner = 1 - server
    return "{0}-{1}".format(player0, player1), winner, remainder[index:]


def my_comp101_game(points, server):
    score, winner, remainder = my_comp101_tiebreaker(points, server, 4)
    table = {
        0: "0",
        1: "15",
        2: "30",
        3: "40"
    }
    p0, p1 = map(int, score.split("-"))
    if winner is None:
        if min(p0, p1) >= 4:
            delta = min(p0, p1) - 3
            p0 -= delta
            p1 -= delta
        s0 = table.get(p0, "Ad")
        s1 = table.get(p1, "Ad")
        score = s0 + "-" + s1
    else:
        if p0 > p1:
            score = "W-" + table.get(p1, "40")
        else:
            score = table.get(p0, "40") + "-W"
    return score, winner, remainder


def comp101_set2(points,server,tiebreaker=my_comp101_tiebreaker,game=my_comp101_game):
        p1=0;p2=0;
        ret=[];
        while ((not ((p1==6) and (p2==7))) and (not ((p1==7) and (p2==6)))):
                if p1==6 and p2<=4:break;
                if (p1<=4) and (p2==6):break;
                if (p1==6 and p2==6):
                        ret=tiebreaker(points,server);
                        print("tiebreaker "+str(ret[1]));
                else:
                        ret=game(points,server);
                        # print ("normal game "+str(ret[1]));
                if ret[1]==None:
                        break;
                if ret[1]==0:p1+=1;
                else: p2+=1;
                points=tuple(ret[2]);

        win=0;
        if (p1==6) and (p2<=4):win=0;
        elif (p1<=4) and (p2==6):win=1;
        elif p1==7:win=0;
        elif p2==7:win=1;
        else: win=None;
        if server==1:
                score=str(p2)+"-"+str(p1);
        else:
                score=str(p1)+"-"+str(p2);
        return (score,win,ret[2]);


def comp101_set1(points, server, tiebreaker=my_comp101_tiebreaker, game=my_comp101_game):
    # return (score, winner, remainder)
    score, winner, remainder
    pass


def my_comp101_set(points,server,tiebreaker=my_comp101_tiebreaker,game=my_comp101_game):
        p1=0;p2=0;
        ret=[];
        while ((not ((p1==6) and (p2==7))) and (not ((p1==7) and (p2==6)))):
                if (p1==6) and (p2<=4):break;
                if (p1<=4) and (p2==6):break;
                if (p1==6 and p2==6):
                        ret=tiebreaker(points,server);
                        ret=list(ret);
                        print("tiebreaker "+str(ret[1]));
                else:
                        ret=game(points,server);
                        ret=list(ret);
                        # print ("normal game "+str(ret[1]));
                if ret[1]==None:
                        ret[2]=points;
                        break;
                if ret[1]==0:p1+=1;
                else: p2+=1;
                points=list(ret[2]);
        win=0;
        if (p1==6) and (p2<=4):win=0;
        elif (p1<=4) and (p2==6):win=1;
        elif p1==7:win=0;
        elif p2==7:win=1;
        else: win=None;
        if server==1:
                score=str(p2)+"-"+str(p1);
        else:
                score=str(p1)+"-"+str(p2);
        return [score,win,ret[2]];


def comp101_match(points, server, maxlen, tiebreaker=comp101_tiebreaker, game=comp101_game, set_score=comp101_set):
    num_to_win = (maxlen + 1) // 2
    p0_wins = p1_wins = 0
    result = list()
    while max(p0_wins, p1_wins) < num_to_win and points:
        score, winner, remainder = my_comp101_set(points, server, my_comp101_tiebreaker, my_comp101_game)
        if score != "0-0":
            result.append(score)
        if winner is None:
            score, winner, remainder = my_comp101_game(remainder, server)
            result.append(score)
            break
        elif winner == 0:
            p0_wins += 1
        elif winner == 1:
            p1_wins += 1
        points = remainder
    if max(p0_wins, p1_wins) == num_to_win and points:
        return "False"
    else:
        return ' '.join(result)


#if __name__ == '__main__':
    # print(comp101_tiebreaker([1, 0, 1, 0, 0, 0], 0))  # ('4-2', None, [])
    # print(comp101_tiebreaker([], 1))  # ('0-0', None, [])
    # print(comp101_tiebreaker([1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], 0))  # ('7-4', 0, [0])

    # print(comp101_game([1, 0, 0, 1, 0, 1, 1, 0, 1, 1], 1))  # ('W-40', 1, [])
    # print(comp101_game([0, 1, 0, 1, 0, 1, 0], 0))  # ('Ad-40', None, [])
    # print(comp101_game([], 1))  # ('0-0', None, [])
    # print(comp101_game([0, 0, 0, 0, 1, 0, 0], 1))  # ('0-W', 0, [1, 0, 0])
    # print(comp101_game([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 0))

    # print(comp101_set([0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], 1))

    # print(comp101_set([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 0));

     # print(comp101_match([], 0, 5))  # ''
     # print(comp101_match([0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], 1, 3))  # 1-2 40-Ad
     # print(comp101_match([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 0, 3))
     # print(comp101_match([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 0, 1))
     #print(comp101_match([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 0, 5))
