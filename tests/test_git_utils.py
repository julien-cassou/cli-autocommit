from unittest.mock import patch
from autocommit.git_utils import get_git_diff
import subprocess

def test_get_git_diff_success() :
    with patch('subprocess.run') as mock_run:
        mock_run.return_value.stdout = "diff --git a/file.txt b/file.txt\n..."
        mock_run.return_value.stderr = ""
        mock_run.return_value.returncode = 0

        result = get_git_diff()

        assert result == "diff --git a/file.txt b/file.txt\n..."

def test_get_git_diff_error():
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, 'git', stderr="Erreur git")

        result = get_git_diff()
        assert result is None