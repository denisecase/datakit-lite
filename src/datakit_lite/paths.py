"""Project path management utilities.

This module provides:
- ProjectPaths: dataclass for organizing standard project directories
- project_paths: function to create and return project directory structure
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectPaths:
    """Standard project directory paths.

    Attributes:
    ----------
    root : Path
        The root directory of the project.
    data_raw : Path
        Directory for raw data files.
    data_clean : Path
        Directory for cleaned/processed data files.
    reports : Path
        Directory for reports and output files.
    models : Path
        Directory for model files and artifacts.
    """

    root: Path
    data_raw: Path
    data_clean: Path
    reports: Path
    models: Path


def project_paths(root: str | Path = ".") -> ProjectPaths:
    """Return a set of standard project directories, creating them if needed.

    Directories:
        data/raw
        data/clean
        reports
        models
    """
    root = Path(root).resolve()

    data_raw = root / "data" / "raw"
    data_clean = root / "data" / "clean"
    reports = root / "reports"
    models = root / "models"

    for p in [data_raw, data_clean, reports, models]:
        p.mkdir(parents=True, exist_ok=True)

    return ProjectPaths(
        root=root,
        data_raw=data_raw,
        data_clean=data_clean,
        reports=reports,
        models=models,
    )
