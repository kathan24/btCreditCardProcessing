# btCreditCardProcessing
Assumptions:
- One user can only have one card since the charge and credit transaction does not have card number. Another card under 
 same user is ignored
- Input file has complete path

Overview of the design decisions.
- Card class has properties like number, limit, balance and whether the card number is valid or not
- User class has properties like name and Card object 

Why you picked the programming language you used.
- I choose Python as the programming language because I am familiar with it.

How to run your code and tests, including how to compile it if applicable and how to install any dependencies your code may have.
- To install Dependencies please run "pip install -r requirements.txt". 
- To run the code make sure the your_intput_file.txt is in project directory. Run below command to execute
python transactions.py < your_intput_file.txt
OR
python transactions.py your_intput_file.txt
