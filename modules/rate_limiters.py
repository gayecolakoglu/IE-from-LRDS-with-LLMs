# rate_limiters.py

import time
import logging
import multiprocessing

class RateLimiter:
    def __init__(self, max_tokens_per_minute):
        self.max_tokens_per_minute = max_tokens_per_minute
        self.tokens_used = 0
        self.start_time = time.time()

    def request_tokens(self, tokens):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time > 60:
            self.tokens_used = 0
            self.start_time = current_time

        if self.tokens_used + tokens > self.max_tokens_per_minute:
            wait_time = 60 - elapsed_time
            wait_time = max(wait_time, 0)  # Ensure wait time is non-negative
            logging.info(f"Rate limit reached. Waiting for {wait_time:.2f} seconds.")
            time.sleep(wait_time)
            self.tokens_used = 0
            self.start_time = time.time()

        self.tokens_used += tokens

class GlobalRateLimiter:
    def __init__(self, max_tokens_per_minute):
        self.max_tokens_per_minute = max_tokens_per_minute
        self.tokens_used = 0
        self.start_time = time.time()
        self.lock = multiprocessing.Lock()

    def request_tokens(self, tokens):
        with self.lock:
            current_time = time.time()
            elapsed_time = current_time - self.start_time

            if elapsed_time > 60:
                self.tokens_used = 0
                self.start_time = current_time

            if self.tokens_used + tokens > self.max_tokens_per_minute:
                wait_time = 60 - elapsed_time
                wait_time = max(wait_time, 0)  # Ensure wait time is non-negative
                logging.info(f"Global rate limit reached. Waiting for {wait_time:.2f} seconds.")
                time.sleep(wait_time)
                self.tokens_used = 0
                self.start_time = time.time()

            self.tokens_used += tokens
