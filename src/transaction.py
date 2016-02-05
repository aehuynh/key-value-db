class TransactionBlock(object):
    """Represents a transaction and contains all the actions to rollback
    the transaction.
    """

    def __init__(self):
        self._undo_actions = []

    def add_undo(self, command, *args):
        self._undo_actions.append(UndoAction(command, args))

    def rollback(self):
        """Run all the undo actions."""
        for action in reversed(self._undo_actions):
            action.run()

        self._undo_actions = []


class UndoAction(object):
    """Represents an action to be taken on rollback.

    Attributes
    ----------
    command: a function
        A function to call on rollback
    args: list
        A list of arguments for the command
    """

    def __init__(self, command, args):
        self._command = command
        self._args = args

    def run(self):
        self._command(*self._args)
