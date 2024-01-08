import random
MAX_LINES=3
MIN_BET=10
MAX_BET=100
ROWS=3
COLS=3
symbol_count={"A":2,
              "B":3,
              "C":7,
              "D":8}
symbol_value={"A":10,"B":8,"C":6,"D":4}
def check_winners(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            current_symbol=column[line]
            if current_symbol!=symbol:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        # print (row)100

        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amount=input("Enter amount to deposit?$")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than zero")
        else:
            print("Please Enter a number")
    return amount
def get_number_of_lines():
    while True:
        lines=input("Enter the lines within (1-"+str(MAX_LINES)+")?")
        if lines.isdigit():
            lines=int(lines)
            if lines>=1 and lines<=MAX_LINES:
                break
            else:
                print("Amount should be within range")
        else:
            print("Please Enter a number")
    return lines
def get_bet():
    while True:
        amount=input("Enter amount to bet?$")
        if amount.isdigit():
            amount=int(amount)
            if amount>MIN_BET and amount<MAX_BET:
                break
            else:
                print(f"Amount should be within range ${MIN_BET}-${MAX_BET}")
        else:
            print("Please Enter a number")
    return amount
def spin(balance):
    while True:

        lines=get_number_of_lines()
    # print(f"Lines: {lines}")  # Debug statement
        bet=get_bet()
    # print(f"Bet: {bet}")  # Debug statement
        total_bet=lines*bet
        if total_bet>balance:
            print(f"You dont have enough balance  for ${total_bet}. The current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is on ${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines=check_winners(slots,lines,bet,symbol_value)
    print(f"Your winning amount is${winnings}")
    print(f"Your winning line is",  *winning_lines)
    return winnings-total_bet

    # print(slots)
    # print_slot_machine(slots)



def main():
    balance=deposit()
    # print(f"Balance: {balance}")  # Debug statement
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance+=spin(balance)
    print(f"You left with ${balance}")
    

main()

