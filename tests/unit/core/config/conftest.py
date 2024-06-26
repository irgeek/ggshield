import pytest

from ggshield.core.config.utils import get_global_path


TEST_AUTH_CONFIG = {
    "default_token_lifetime": 2,
    "instances": [
        {
            "name": "default",
            "url": "https://dashboard.gitguardian.com",
            "default_token_lifetime": 1,
            "accounts": [
                {
                    "workspace_id": 23,
                    "token": "62890f237c703c92fbda8236ec2a055ac21332a46115005c976d68b900535fb5",  # ggignore
                    "type": "pat",
                    "token_name": "my_token",
                    "expire_at": "2022-02-23T12:34:56+00:00",
                }
            ],
        },
        {
            "name": None,
            "url": "https://dashboard.onprem.example.com",
            "default_token_lifetime": 0,  # no expiry
            "accounts": [
                {
                    "workspace_id": 1,
                    "token": "8ecffbaeedcd2f090546efeed3bc48a5f4a04a1196637aef6b3f6bbcfd58a96b",  # ggignore
                    "type": "sat",
                    "token_name": "my_other_token",
                    "expire_at": "2022-02-24T12:34:56+00:00",
                }
            ],
        },
    ],
}


@pytest.fixture
def local_config_path():
    yield ".gitguardian"


@pytest.fixture()
def global_config_path():
    yield get_global_path(".gitguardian")
