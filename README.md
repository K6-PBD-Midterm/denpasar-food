# denpasar-food
## Group members
- Derensh Pandian		
- Isaac Jesse Boentoro		
- Donia Sakji		
- Ferdinand Bonfilio Simamora		
- Adiena Nimeesha Adiwinastwan		
- Bryant Warrick Cai		

## Application description
Restaurant Locator based on Bali, Denpasar

## List of modules to be implemented
```
restaurants
authentication
reviews
map 
admin_dashboard
filter
```



## Souce of initial dataset
https://overpass-turbo.eu

## User roles
Roles in the site:
- Admin:
    This user is allowed to modify the web or restaurant in anyway it fits

- Client:
    This user is only allowed to view restaurants and not allowed to add restaurants.

- Restaurant Owner:
    This user is only allowed to view restaurants and add new restaurants.

## Application deployment link
```
tba
```

## Instruction for other user to start the code:
NOTE: The following instructions ASSUME that your current local repo is fresh out of 
```
git clone https://github.com/K6-PBD-Midterm/denpasar-food.git
```

If you are in windows use `python`, if you're on linux/mac use `python3`

Make sure you are in the root folder when running startup code, for example:

```
for Windows
C:\Users\ferdi\OneDrive\Desktop\denpasar-food>

for Mac

```

Make sure you do the following startup code in order (except if told otherwise)

### Step 1:
Inside the root directory of this repository, run:
```
python -m venv env
```

### Step 2:
Activate the virtual environment by running:

Windows:
```
env\Scripts\activate
```

Unix (Mac/Linux):
```
source env/bin/activate
```

Note: On Windows, if you get an error that running scripts is disabled on your system, follow these steps:
1. Open Windows PowerShell as an administrator. (Search "PowerShell" on start menu, then right-click -> Run as administrator)
2. Run the following command: `Set-ExecutionPolicy Unrestricted -Force`

### Step 3:
Inside the virtual environment (with `(env)` indicated in the terminal input line), run:
```
pip install -r requirements.txt
```

### Step 4:
Run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py import_restaurants
```

### Step 5:
```
python manage.py runserver
```

