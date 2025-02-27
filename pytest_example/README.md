# Setup
1. Clone the repository
2. Install dependencies (`requirements.txt`)
3. Set your environment variable (`$HTTP_PROXY`)
4. Run the test - `HTTP_PROXY=http://localhost:3128 pytest -p setup_proxy test_title.py`

# Notes
- Depending on your environment, you may see an error similar to `Error importing plugin "setup_proxy": No module named 'setup_proxy'`. In this case, you may need to configure your `$PYTHONPATH` to include the current project directory, like so: `PYTHONPATH=./ HTTP_PROXY=http://localhost:3128 pytest -p setup_proxy test_title.py`