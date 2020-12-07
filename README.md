# TP_CleanCode
Evaluated project - API
## How to run and test the api ? (Linux)
- Clone the repository
```sh
git clone https://github.com/agirar05/TP_CleanCode.git
```
- Create python virtual env in it
```sh
cd TP_CleanCode
python3 -m venv venv
```
- Launch the virtual env
```sh
source venv/bin/activate
```
- Install all the requirements
```sh
pip install -r requirements.txt
```
### Run the api
```sh
python manage.py run # Then go to localhost:5000
```

### Test the api
```sh
python manage.py test
```