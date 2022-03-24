import platform
skipwindows = pytest.mark.skipif(
    platform.system() == "Windows" and not os.environ.get("DISABLE_SKIPWINDOWS"),
    reason="Skipped on Windows for now, define DISABLE_SKIPWINDOWS environment variable to unskip",
)


_SIMPLE_SECRET_TOKEN = "368ac3edf9e850d1c0ff9d6c526496f8237ddf91"
_SIMPLE_SECRET_PATCH = f"""@@ -0,0 +1 @@
+github_token: {_SIMPLE_SECRET_TOKEN}
                        "match": _SIMPLE_SECRET_TOKEN,
                        "match": _SIMPLE_SECRET_TOKEN,  # noqa