"""Export selected item wrappers through the installed, unmodified PyHTML CLI."""

import argparse
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory

from ggpaths import atomic_write_string_to_file


def item_id(value: str) -> str:
    """Validate a canonical item identity for a wrapper and output directory.

    Args:
        value: Positive ASCII decimal identity without leading zeroes.
    """
    if re.fullmatch(r"[1-9][0-9]*", value) is None:
        raise argparse.ArgumentTypeError("Use a positive item ID without leading zeroes.")
    return value


def main() -> None:
    """Build every requested wrapper successfully before replacing its export."""
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("items", nargs="+", type=item_id, help="Existing N.muweave wrappers to export")
    parser.add_argument(
        "--library", type=Path,
        default=project.parent.parent.parent / "Python/ggpackages/muweave_library",
        help="Canonical MuWeave library (default: the sibling ggpackages workspace)",
    )
    parser.add_argument(
        "--output-root", type=Path, default=project,
        help="Destination containing N/index.html (default: this repository)",
    )
    arguments = parser.parse_args()
    identities = tuple(dict.fromkeys(arguments.items))
    library = arguments.library.resolve()
    for name in ("items", "images", "interactive"):
        if not (library / name).is_dir():
            parser.error(f"Missing library directory: {library / name}")
    for identity in identities:
        if not (project / f"{identity}.muweave").is_file():
            parser.error(f"Missing wrapper: {identity}.muweave")
        if not (library / "items" / f"{identity}.muweave").is_file():
            parser.error(f"Missing canonical item: {identity}.muweave")

    # The temporary source has no course-specific ancestor .mu settings.
    # Explicit canonical roots keep included items and their assets unambiguous.
    with TemporaryDirectory(prefix="muweave-items-", dir="/tmp") as temporary:
        staging = Path(temporary)
        for identity in identities:
            source = staging / f"{identity}.muweave"
            (staging / identity).mkdir()
            atomic_write_string_to_file(
                (project / source.name).read_text(encoding="utf-8"), source,
            )
            subprocess.run(
                [
                    sys.executable, "-m", "pyhtml", str(source), "--publish",
                    "--items-dir", str(library / "items"),
                    "--images-dir", str(library / "images"),
                    "--interactive-dir", str(library / "interactive"),
                    "--output", str(staging / identity / "index.html"),
                ],
                check=True, cwd=staging,
            )
        for identity in identities:
            destination = arguments.output_root.resolve() / identity / "index.html"
            destination.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_string_to_file(
                (staging / identity / "index.html").read_text(encoding="utf-8"), destination,
            )
            print(f"Exported {identity}: {destination}")


if __name__ == "__main__":
    main()
