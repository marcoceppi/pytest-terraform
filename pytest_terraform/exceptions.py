class PytestTerraformError(Exception):
    """Pytest Terraform Exception Base Class"""

    pass


class TerraformCommandFailed(PytestTerraformError):
    """Terraform Command failed during execution"""

    pass


class InvalidOption(PytestTerraformError):
    """Invalid Option Error"""

    pass


class InvalidTeardownMode(InvalidOption):
    """Invalid Teardown Option Error"""

    pass
