# This contains the driver fixture and the base test class

import pytest

@pytest.mark.usefixtures("driver_init")
class BaseTest():
    pass
