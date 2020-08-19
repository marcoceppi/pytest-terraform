class PytestTerraformError(Exception):
    """Pytest Terraform Exception Base Class"""


class ModuleNotFound(ValueError):
    """module not found"""


class TerraformCommandFailed(PytestTerraformError):
    """Terraform Command failed during execution"""


class InvalidOption(PytestTerraformError):
    """Invalid Option Error"""


class InvalidTeardownMode(InvalidOption):
    """Invalid Teardown Option Error"""
