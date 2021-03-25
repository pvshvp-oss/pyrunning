import unittest

from fenix_library.running import LoggingHandler
from tests.initializing import InitializeLogging

import logging
 
class Test_log_message(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        InitializeLogging.setup_logger()
        cls.logger = logging.getLogger("fenix_library-running_test." + "Test_log_message")
        cls.logging_handler = LoggingHandler(cls.logger)

    def test_debug_message(self):
        self.logging_handler.log_message(10, "Test message")