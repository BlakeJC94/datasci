import fire

from . import (
    process,
)


def main():
    fire.Fire(dict(
        process=process,
    ))


if __name__ == '__main__':
    main()

