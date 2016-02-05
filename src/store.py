from collections import defaultdict
from transaction import TransactionBlock

class DataStore(object):
    """Key-value store with transaction support."""

    def __init__(self):
        self._blocks = []
        self._variables = {}
        self._num_equal_to = defaultdict(int)

    def set(self, name, value, log=True):
        """Set the value of a variable."""
        if name in self._variables:
            self.unset(name, log)

        # Add undo action to transaction block
        if self.in_transaction() and log:
            self._blocks[-1].add_undo(self.unset, name, False)

        self._variables[name] = value
        self._num_equal_to[value] += 1

    def get(self, name):
        """Get the value of a variable."""
        return self._variables.get(name, None)

    def unset(self, name, log=True):
        """Remove the variable if it exists."""
        if name in self._variables:
            value = self._variables[name]

            # Add undo action to transaction block
            if self.in_transaction() and log:
                self._blocks[-1].add_undo(self.set, name, value, False)

            del self._variables[name]
            self._num_equal_to[value] -= 1

    def numequalto(self, value):
        """Returns the number of variables set to a particular value."""
        return self._num_equal_to[value]

    def begin(self):
        """Start a new transaction block."""
        self._blocks.append(TransactionBlock())

    def rollback(self):
        """Rollback the last transaction block."""
        if self.in_transaction():
            self._blocks.pop().rollback()

    def commit(self):
        """Flush transaction logs."""
        self._blocks = []

    def in_transaction(self):
        """Checks if there is an active transaction."""
        return len(self._blocks) > 0
