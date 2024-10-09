import argparse
import click

def string_splitter(string_to_split: str, split_symbol: str) -> list:
    """
    :param string_to_split: String to separate
    :param split_symbol: Separator to separate by
    :return: List of separated substrings
    """
    # Add code here to split 'string_to_split' with 'split_symbol'
    return string_to_split.split(split_symbol)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Split "String" by "Separator"')

    # Add required info form task here
    parser.add_argument("-string", action="store", required=True)

    # Add required info form task here
    parser.add_argument("-separator", action="store", required=True)

    args = parser.parse_args()
    income_string = args.string
    separator_symbol = args.separator

    # Call function "string_splitter" with parameters to print result
    print(string_splitter(income_string, separator_symbol))
