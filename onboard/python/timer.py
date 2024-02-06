import time
from dataclasses import dataclass, field
from typing import Optional
import logging

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

@dataclass
class Timer:
    logger: logging.Logger
    name: Optional[str] = None
    text: str = "{} took {:0.4f} seconds"
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        # Calculate elapsed time
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        # Report elapsed time
        self.logger.info(self.text.format(self.name, elapsed_time))

        return elapsed_time
