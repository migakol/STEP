import argparse


class BaseOptions:
    """
    This class defines the basic options used in all cases - in trainging, testing, saving data, etc.
    """

    def __init__(self):
        """Reset the class; indicates the class hasn't been initailized"""
        self.parser = argparse.ArgumentParser()
        self.initialized = False
        self.opt = None

    def initialize(self):
        # --mode nlp_benchmark, clip_benchmark
        self.parser.add_argument('--input_folder', type=str, default='', help='where /frames reside')

    def parse(self):
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()

        return self.opt