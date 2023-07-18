from pathlib import Path
from typing import Any, Optional, Sequence

import click
import os

from ggshield.core.text_utils import display_warning
from ggshield.cmd.iac.scan.all import display_iac_scan_all_result, iac_scan_all
from ggshield.cmd.iac.scan.diff import display_iac_scan_diff_result, iac_scan_diff
from ggshield.cmd.iac.scan.iac_scan_common_options import (
    add_iac_scan_common_options,
    all_option,
    directory_argument,
    update_context,
)


@click.command()
@add_iac_scan_common_options()
@all_option
@directory_argument
@click.pass_context
def scan_ci_cmd(
    ctx: click.Context,
    exit_zero: bool,
    minimum_severity: str,
    ignore_policies: Sequence[str],
    ignore_paths: Sequence[str],
    all: bool,
    directory: Optional[Path] = None,
    **kwargs: Any,
) -> int:
    """
    Scan in CI for IaC vulnerabilities. By default, it will return vulnerabilities added in the new commits.
    """
    display_warning(
        "This feature is still in beta, its behavior may change in future versions."
    )
    directory = os.getenv("GITGUARDIAN_IAC_SCAN_DIRECTORY", directory)
    reference = os.getenv("GITGUARDIAN_IAC_SCAN_TO_REF", "HEAD")
    current = os.getenv("GITGUARDIAN_IAC_SCAN_FROM_REF", None)
    if directory is None:
        directory = Path().resolve()
    update_context(ctx, exit_zero, minimum_severity, ignore_policies, ignore_paths)
    if all:
        result = iac_scan_all(ctx, directory)
        return display_iac_scan_all_result(ctx, directory, result)
    if current:
        result = iac_scan_diff(ctx, directory, reference, current=current)
    else:
        result = iac_scan_diff(ctx, directory, reference, include_staged=True)
    return display_iac_scan_diff_result(ctx, directory, result)
