**Activate the virtual environment**

```
blockchain-env\Scripts\activate
```

**Install all packages**

```
pip3 install -r requirements.txt
```


**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the application and API**

```
python -m backend.app
```