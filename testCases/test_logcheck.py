from utilities.customLogger import LogGen

# Get an instance of the logger object
class Test_002_Login:

    def test_logCheck(self):

        self.logger = LogGen.loggen()
        # Write logs to the file
        self.logger.info('This is an info message')
        self.logger.warning('This is a warning message')
        self.logger.error('This is an error message')
