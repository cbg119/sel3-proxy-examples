# Setup
1. Clone the repository
2. Install dependencies (`requirements.txt`)
3. Set your environment variable (`$HTTP_PROXY`)
4. Run the test
   - To run the basic (default behavior) test, `python test_title.py`
   - To run the solution-implemented test, `python wrapper.py`

# Additional Information
- `runpy` (https://docs.python.org/3/library/runpy.html)
   - Ensures the same namespace/process is used to execute the wrapped Python script
   - `run_name` is explicitly set to `__main__` to emulate running the wrapped script directly from CLI (i.e. `python test_title.py`)