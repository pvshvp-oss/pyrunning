import logging
from os import stat
import pathlib
import subprocess
import datetime
from typing import Optional

class InitializeLogging:
    
    @staticmethod
    def setup_logger() -> logging.Logger:
        """
        Configure the logger

        The following tasks are accomplished:
        - Create a named logger
        - Setup logging to be done onto a file and the console
        - Define the format of log entries
        - Delete old log files

        Parameters
        ----------
        None

        Returns
        -------
        logger: logging.Logger
            The logger which has been set up
        """

        InitializeLogging.delete_old_log_files(no_of_files_to_keep =5) # delete old log files

        logger = logging.getLogger('pyrunning_test') # create a new logger and name it
        logger.setLevel(logging.DEBUG) # set it to log anything of debugging and higher alert levels
        logger.propagate = False
        
        # Set up file-based logging
        log_file_path = pathlib.Path("tests/log/" + "pyrunning_test-" + get_time_stamp() + ".log")
        print("Logging to " + str(log_file_path.resolve()) + "...\n")
        log_file_handler = logging.FileHandler(log_file_path) # for logging onto files
        log_file_handler.setLevel(logging.DEBUG) # log debug messages and higher
        # log_file_formatter = logging.Formatter('[%(asctime)s, %(levelname)-8s, %(name)s] %(message)s', '%Y-%m-%d, %H:%M:%S %Z') # old format of each log file entry
        log_file_formatter = logging.Formatter('%(asctime)s [%(levelname)8s] %(message)s (%(pathname)s > %(funcName)s; Line %(lineno)d)', '%Y-%m-%d %H:%M:%S %Z') # format of each log file entry
        log_file_handler.setFormatter(log_file_formatter)
        logger.addHandler(log_file_handler)

        # Set up standard console logging
        log_error_handler = logging.StreamHandler() # for logging onto the console
        log_error_handler.setLevel(logging.INFO) # log info messages and higher alert levels   
        log_error_formatter = logging.Formatter('%(levelname)8s: %(message)s') # format of each console log entry    
        log_error_handler.setFormatter(log_error_formatter)    
        logger.addHandler(log_error_handler)

        return logger

    @staticmethod
    def delete_old_log_files(no_of_files_to_keep: int) -> None:
        """
        Delete old log files while keeping the newest ones whose count is specified by "no_of_files_to_keep"
        
        Parameters
        ----------
        no_of_files_to_keep: int
            The number of newest log files to keep

        Returns
        -------
        Nothing        
        """

        subprocess.Popen(
            "ls -tp pyrunning_test-* | grep -v '/$' | tail -n +" 
                + str(no_of_files_to_keep) 
                + " | xargs -I {} rm -- {}",
            shell=True,
            cwd=pathlib.Path("./tests/log/")
        )

def get_time_stamp() -> str:
    """
    Returns the timestamp in a particular format
    Example: 2020-01-31_23_58_59_GMT

    Parameters
    ----------
    None

    Returns 
    -------
    timestamp: str
        The timestamp in a particular format. Example: 2020-01-31_23_58_59_GMT
    """

    time_stamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_")
    time_zone: Optional[str] = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    
    if time_zone is None:
        time_zone = ""

    return (
        time_stamp + time_zone
    )