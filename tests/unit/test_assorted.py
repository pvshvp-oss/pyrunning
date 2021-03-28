import unittest

from fenix_library.running import LoggingHandler, LogMessage, Function, Command
from tests.initializing import InitializeLogging

import logging
 
class UnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        InitializeLogging.setup_logger()
        cls.logger = logging.getLogger("fenix_library-running_test." + "Test_log_message")
        cls.logging_handler = LoggingHandler(cls.logger)

    def test_debug_message(self):
        self.logging_handler.log_message(10, "Test message 1")

    def test_debug_message_indirect(self):
        LogMessage.Debug("Test message 2").write(self.logging_handler)

    def test_function_run(self):
        Function(len, [1,2,3,4,5]).run_and_log(self.logging_handler)

    def test_command_run(self):
        Command(["ping", "-c", "5", "www.google.com"]).run_log_and_wait(self.logging_handler)

    def test_silent_command_run(self):
        Command(["ping", "-c", "5", "www.facebook.com"], is_silent= True).run_log_and_wait(self.logging_handler)

    def test_special(self):
        LogMessage.Debug("Before ping...").write(self.logging_handler)
        print("Before ping print...")
        command = Command(["ping", "-c", "5", "www.instagram.com"])
        command.run_and_log(self.logging_handler)
        print("After ping print...")
        LogMessage.Debug("After ping...").write(self.logging_handler)

        command = Command(["ping", "-c", "5", "www.discourse.com"])
        LogMessage.Debug("Before ping 2...").write(self.logging_handler)
        print("Before ping 2 print...")
        command.run_and_log(self.logging_handler)
        print("After ping 2 print...")
        LogMessage.Debug("After ping 2...").write(self.logging_handler)

    def test_run_log_and_wait(self):
        print("Starting a command that waits...")
        Command(["ping", "-c", "5", "www.twitter.com"]).run_log_and_wait(self.logging_handler)
        print("After the command that waits...")
        Command(["echo", "Hello"]).run_log_and_wait(self.logging_handler)

    def test_run_and_log(self):
        print("Starting a command that does not wait...")
        Command(["ping", "-c", "5", "www.amazon.com"]).run_and_log(self.logging_handler)
        print("After the command that does not wait...")
        Command(["echo", "Hello"]).run_log_and_wait(self.logging_handler)


