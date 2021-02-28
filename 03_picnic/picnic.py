#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-01-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Stores and formats what you bring to a picnic",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "items", metavar="items", nargs="+", help="Item(s) to bring with you"
    )

    parser.add_argument(
        "-s", "--sorted", help="Sorts items by character", action="store_true"
    )

    # Sets the oxford comma
    # @see https://stackoverflow.com/questions/52403065/argparse-optional-boolean
    parser.add_argument(
        "--oxford",
        help="Include the oxford comma",
        default=True,
        action="store_true",
    )

    parser.add_argument(
        "--no-oxford",
        help="Removes the oxford comma",
        dest="oxford",
        action="store_false",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Prints the final list of items"""

    args = get_args()
    needs_sorting = args.sorted
    item_list = args.items
    include_oxford_comma = args.oxford

    if needs_sorting:
        item_list.sort()

    message = "You are bringing "

    if len(item_list) == 1:
        message += f"{item_list[0]}."
    elif len(item_list) == 2:
        message += f"{item_list[0]} and {item_list[1]}."
    else:
        message += (
            f"{', '.join(item_list[0:-1])}, and {item_list[-1]}."
            if include_oxford_comma
            else f"{', '.join(item_list[0:-1])} and {item_list[-1]}."
        )

    print(message)


# --------------------------------------------------
if __name__ == "__main__":
    main()
