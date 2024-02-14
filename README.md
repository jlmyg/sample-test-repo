# sample-test-repo

### This is my repository to showcase what I know when it comes to test automation. This repo focuses on using tools such as Selenium, Python, and Pytest.


### First steps to run this test repository: install python
1. Install python through https://www.python.org/


### Additionally, you can also install python through pyenv which helps manage your python version in the long run. You can check it through https://github.com/pyenv/pyenv?tab=readme-ov-file

### How to run the tests
1. After installation of python and setting up a virtual env, you can then proceed to install the dependencies by running:
    `pip install -r requirements.txt`

    **NOTE: The recommended python version is 3.10+**
3. Change your directory to the tests/ folder
4. Run `pytest`

### Other neat and useful commands
1. Markers
    - This allows you to categorize your tests as smoke, slow, fast, etc. which allows you to specify which tests you'd want to run
    - To run smoke tests, just append `-m *marker*` from the pytest command. e.g. `pytest -m smoke`
2. Parallel testing
    - This allows you to run tests in parallel with each other
    - To run in parallel, just append `-n *workers*` from the pytest command. e.g. `pytest -n auto` note that you can also specify the number of workers.
3. Headless testing
    - This allows you to run the tests in headless mode (without opening an actual browser instance)
    - To run headless, just append `--headless=true` from the pytest command. e.g. `pytest --headless=true` note that the default value is false when ommited.
4. WIP: Different browsers

The good thing is that you can append a combination of these commands e.g. `pytest -m smoke -n 4 --headless=true`

### TODO: Add docker capabilities for running the tests
