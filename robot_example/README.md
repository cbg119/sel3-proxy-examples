# Setup

1. Clone the repository
2. Install dependencies (`requirements.txt`)
3. Set your environment variable (`$HTTP_PROXY`)
4. Run the test - `HTTP_PROXY=http://localhost:3128 robot -V setup_proxy.py visit_login.robot`

# Notes
- When using the above command to start tests, `HTTP_PROXY=http://localhost:3128` is only required if `$HTTP_PROXY` has not already been set
- The `-V` flag instructs Robot to load `setup_proxy.py` as a variable file