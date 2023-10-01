#!/usr/local/bin/python3
import argparse
import logging
import re

logging.basicConfig(filename="ligma.log",
                    encoding="utf-8", level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()
    if not args.file:
        logging.error("No file provided")

    logging.info("Parsing file")
    logging.info(f"file arg: {args.file}")
    logging.info(f"other args: {args}")

    with open(args.file, 'r') as f:
        line_number = 0
        for line in f:
            line_number += 1
            pattern = "[a-zA-Z_]+igma"

            match = re.search(pattern, line)
            if not match:
                continue

            start, end = match.span()
            message = match.group()
            logging.info(f"Message: {message}")

            message = f"{line_number}:{start}:{end + 1}:info:{message} balls"
            print(message)
            logging.info(message)


if __name__ == "__main__":
    main()
