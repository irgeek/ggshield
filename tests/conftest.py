from requests.utils import DEFAULT_CA_BUNDLE_PATH, extract_zipped_paths
# This long token is a test token, always reported as an uncheckable secret
GG_TEST_TOKEN = (
    "8a784aab7090f6a4ba3b9f7a6594e2e727007a26590b58ed314e4b9ed4536479sRZlRup3xvtMVfiHWA"
    "anbe712Jtc3nY8veZux5raL1bhpaxiv0rfyhFoAIMZUCh2Njyk7gRVsSQFPrEphSJnxa16SIdWKb03sRft"
    "770LUTTYTAy3IM18A7Su4HjiHlGA9ihLj9ou3luadfRAATlKH6kAZwTw289Kq9uip67zxyWkUJdh6PTeFp"
    "MgCh3AhHcZ21VeZHlu12345"
)

# This is another test token, this one is always report as a valid secret
GG_VALID_TOKEN = "ggtt-v-12345azert"  # ggignore
UNCHECKED_SECRET = (
    "+# gg token\n"
    f'+apikey = "{GG_TEST_TOKEN}";\n'
VALID_SECRET = (
    "diff --git a/test.txt b/test.txt\n"
    "new file mode 100644\n"
    "index 0000000..b80e3df\n"
    "--- /dev/null\n"
    "+++ b/test\n"
    "@@ -0,0 +2 @@\n"
    "+# gg token\n"
    f'+apikey = "{GG_VALID_TOKEN}";\n'
)

_SIMPLE_SECRET = UNCHECKED_SECRET

_PATCH_WITH_NONEWLINE_BEFORE_SECRET = """
diff --git a/artifactory b/artifactory
index 2ace9c7..4c7699d 100644
--- a/artifactory
+++ b/artifactory
@@ -1,3 +1,3 @@
 some line
 some other line
-deleted line
\\ No newline at end of file
+sg_key = "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"
\\ No newline at end of file
"""



@pytest.fixture(scope="function")
def isolated_fs(fs):
    # isolate fs but include CA bundle for https validation
    fs.add_real_directory(os.path.dirname(extract_zipped_paths(DEFAULT_CA_BUNDLE_PATH)))
    # add cassettes dir
    cassettes_dir = join(dirname(realpath(__file__)), "cassettes")
    fs.add_real_directory(cassettes_dir)