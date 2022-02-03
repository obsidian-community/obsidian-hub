#!/usr/bin/env python3

import sys
import argparse
from typing import Sequence

from make_mocs import VaultMoc


def main(argv: Sequence[str] = sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    # parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    vault_moc = VaultMoc()
    vault_moc.update_all_mocs(args)


if __name__ == "__main__":
    main()
