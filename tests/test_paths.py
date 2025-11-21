from datakit_lite import project_paths


def test_project_paths_creates_directories(tmp_path):
    paths = project_paths(tmp_path)

    # All directories should exist
    assert paths.data_raw.exists()
    assert paths.data_clean.exists()
    assert paths.reports.exists()
    assert paths.models.exists()
