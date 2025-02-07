# Contributing to jReadability

## Reporting issues

If you encounter an issue with jReadability and would like to report it, you'll first want to make sure you're using the latest version of jReadability.

The latest version of jReadability can be found under [releases](https://github.com/joshdavham/jreadability/releases) and you can verify the version of your current installation with the following command:
```
pip show jreadability
```

Once you've confirmed your version, please report your issue in the [issues tab](https://github.com/joshdavham/jreadability/issues).

## Contributing code

### Set up local environment

After cloning this repo, install `jreadability` locally in editable mode along with the dev dependencies
```
pip install -e ".[dev]"
```

Now you're ready to make changes to files in the `src/jreadability` directory and see your changes reflected immediately.

### Pass the checks

In order for your contribution to be accepted, your code must pass the linting checks and unit tests.

Lint your code with:
```
ruff check --fix
```

Run the tests with:
```
pytest
```

Also, don't forget to format your code with:
```
ruff format
```

Additionally, you are strongly encouraged to contribute your own tests to [tests/test_jreadability.py](tests/test_jreadability.py) to help make jReadability more reliable.