"""Entrypoint for pipelines"""


def main() -> None:
    """Entrypoint for pipelines"""
    print('hello world!')


def healthy() -> None:
    """Placeholder health check"""
    return True


if __name__ == '__main__':
    main()
