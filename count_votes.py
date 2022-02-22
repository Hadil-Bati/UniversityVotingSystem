import sqlite3
def count_votes():
    counts = {}
    c = sqlite3.connect("login.db")
    ids = c.execute("SELECT NAME FROM Candidates WHERE POSITION='GSU_Officer'").fetchall()
    for x in ids:
        name = (x[0])
        votes = c.execute("SELECT COUNT(*) FROM COUNTING WHERE CANDIDATE = ?;",(name,)).fetchone()[0]
        counts[name] = votes
    #Single Transferable vote
    print(counts) 
    seats = 1
    total_votes = c.execute("SELECT COUNT(*) FROM COUNTING WHERE POSITION = 'GSU_Officer';").fetchone()[0]
    quota = (total_votes/(seats+1))+1
    highest = max(counts, key=counts.get)
    value = counts[highest]
    if value > quota:
        print("winner is",highest)

count_votes()
