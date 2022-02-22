# University Voting System

A system created for university students to vote for candidates running for different Student Union positions such as President, Vice President and many other. 
The program has an python based GUI which allows students to enter their ID and Passwords, for access to the voting screen.

As this is SQL-based, there is a database created which includes;
- the login IDs of the Users (Students) 
- The Candidates and the position in which they are running for
- the Election date : for functionality that users are to vote on the election date.
- Counting : voting data for counting the results of the elections.

FUNCTIONALITIES WITHIN THE LOGIN GUI:
- If students are not registered as users, they will not have access to the voting screen, with a warning pop up entailing that they ae not eligible to vote.
- If students login post the election date, they will not have access to the voting.

FUNCTIONALITIES WITHIN THE ELECTION_RESULTS:
- A GUI which allows the user to access the results of each candidate, separated by faculty.
- Therefore allows users to view all candidates and how many votes each has by preference.
