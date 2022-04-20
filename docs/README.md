# datasci

Template for quick data science projects.

Quickstart checklist:
- [ ] Rename `datasci` throughout project (`README.md`, `./datasci` directory, `setup.py`)
- [ ] Link data directories in `./data`
- [ ] Add data links folders to `.gitignore`
- [ ] Update `__main__.main()` function
- [ ] Remove this checklist and write proper `README.md`


## Directory structure
```
.
├── data
│   ├── artifacts   <- Data needed for running/configuring modelling
│   ├── interim     <- Preprocessed data
│   ├── output      <- Output data
│   ├── processed   <- Input data
│   └── raw         <- Link to raw immutable data
├── datasci         <- `src` level directory (    *)
│   ├── data
│   │   └── load_data.py
│   ├── features
│   │   └── build.py
│   ├── globals.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── model
│   ├── process.py  <- High-level scripts (*)
│   ├── utils.py    <- Project-wide utility functions
│   └── vis
│       └── plot_feature.py
├── docs
│   └── README.md
├── LICENSE
├── pytest.ini
├── requirements.txt
├── results
│   └── report
├── setup.py
└── tests
    ├── conftest.py
    └── __init__.py

```
