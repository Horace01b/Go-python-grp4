board_size = 9

# Initialize a Go board of size 9x9
board = []  

for _ in range(board_size):            
    row = []                           
    for _ in range(board_size):        
        row.append(".")                
    board.append(row)                  


columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:board_size]
print("   " + " ".join(columns))   

# Print each row with row numbers
for row_index, row in enumerate(board):
    print(f"{row_index:2} " + " ".join(row))