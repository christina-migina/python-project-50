from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
