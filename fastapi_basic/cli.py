"""Console script for fastapi_basic."""

import fire


def help():
    print("fastapi_basic")
    print("=" * len("fastapi_basic"))
    print("Basic FastAPI template")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
