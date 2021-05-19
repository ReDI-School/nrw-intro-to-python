# Install dependencies:
``` bash
python -m venv .venv
```
For Windows:  

``` Powershell
.venv\Scripts\activate
```
For Linux/iOS:  

``` Bash
.venv/bin/activate

or 

.venv/Scripts/activate (git bash)
```
Then run:  

``` Bash
pip install -r requirements.txt

python -m uvicorn test_api:app --reload --port 54321
```

Now you can visit: http://127.0.0.1:54321/docs