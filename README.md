# Key Value Database
A simple in-memory, key-value database that supports transactions

### How to Run
The Key Value Database requires Python 3.4.3. It is a command line program. To start the database command line: `python src/database.py`

### Command Syntax
Commands and arguments are split by spaces. Commands will not run without the correct number of arguments. 

Commands do not support quotes. The command `SET tomato "fruit"` sets `tomato` to the value `"fruit"` which incudes the quotes. The command `SET "jones "` sets `"jones` to the value `"`. 


### Regular Commands

* `SET key value` - Set the variable *key* to *value*. Overwrites *key* if it already exists.
* `GET key` - Print the value of the variable *key*. Prints NULL if *key* is not in the database.
* `NUMEQUALTO value` - Print the number of variables that are set to the specified value.
* `UNSET key` - Delete the variable *key* if it exists.
* `END` - End the program.

### Transaction Commands

* `BEGIN` - Create a new transaction. Transactions can be nested.
* `ROLLBACK` - Undo the changes of the most recently created transaction and close the transaction. Prints NO TRANSACTION if there are no open tranactions.
* `COMMIT` - Commits all open transactions and closes them. Prints NO TRANSACTION if there are no open tranactions.
