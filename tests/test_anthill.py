#!/usr/bin/env python

"""Tests for `anthill` package."""


import unittest
from click.testing import CliRunner

from anthill import src
from anthill.src import cli


class TestAnthill(unittest.TestCase):
    """Tests for `anthill` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        # runner = CliRunner()
        # result = runner.invoke(cli)
        # assert result.exit_code == 0
        # assert 'src.cli' in result.output
        # help_result = runner.invoke(cli, ['--help'])
        # assert help_result.exit_code == 0
        # assert '--help  Show this message and exit.' in help_result.output
        pass
