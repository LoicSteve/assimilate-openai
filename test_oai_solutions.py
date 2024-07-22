# write a test for the submit_question function in oalib.solutions module.

import pytest
import os
from oalib.solutions import submit_question

def test_submit_question():
    """test teh submit question function"""
    assert submit_question("What is the capital of Nigeria?") == "The capital of Nigeria is Abuja."