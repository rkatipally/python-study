class TransactionException(Exception):

    def __init__(self, message):
        Exception.__init__(self, 'Invalid Transaction: {0}',message)
