#!/usr/bin/env python3

import click # type: ignore
from oalib.solutions import code_generator


@click.group()
def cli():

    """Generate code examples from comments in m ultiple languages"""


@cli.command("generate")
@click.option(
    "--language", "-l", default="python", help="The language to generate code in"
)
@click.argument("text")
def mkcode(text, language):
    """
    This is the main function that you ask the Open AI API a question to get an answer
    example: ./mkcode.py generate -l python "Calculate the mean distance between an array of points"
    """

    response = code_generator(text, language)
    print(response)

if __name__ == "__main__":
    cli()
