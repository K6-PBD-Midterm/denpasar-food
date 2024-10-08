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
Tailwindcss
```

To use Tailwind, first install `node` and then install tailwindcss with `npm install -D tailwindcss autoprefixer postcss`. Then, run `npm run build` to collect the tailwind classes, then run `python manage.py runserver` as usual.

## Souce of initial dataset
https://overpass-turbo.eu

## User roles
```
tba
```

## Application deployment link
```
tba
```

## Instruction for other user to start the code:
NOTE: The following instructions ASSUME that your current local repo is fresh out of 
```
git clone https://github.com/K6-PBD-Midterm/bali-food-guide.git
```

If you are in windows use `python`, if you're on linux/mac use `python3`

Make sure you are in the root folder when running startup code, for example:

```
for Windows
C:\Users\ferdi\OneDrive\Desktop\bali-food-guide>

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

Install node.js from the following site for your OS:
```
https://nodejs.org/en/download/prebuilt-installer
```

### Step 6:
```
npm install -D tailwindcss autoprefixer postcss
npm run build
python manage.py runserver
```

### Optional Step: Debugging potential bugs

Bug 1: after `npm run build`
```
PS C:\Users\ferdi\OneDrive\Desktop\bali-food-guide> npm run build

> bali-food-guide@1.0.0 build
> npx tailwindcss -i ./src/input.css -o ./static/css/output.css

node:internal/modules/cjs/loader:1251
  throw err;
  ^

Error: Cannot find module 'C:\Users\ferdi\OneDrive\Desktop\bali-food-guide\node_modules\tailwindcss\lib\cli.js'
    at Module._resolveFilename (node:internal/modules/cjs/loader:1248:15)
    at Module._load (node:internal/modules/cjs/loader:1074:27)
    at TracingChannel.traceSync (node:diagnostics_channel:315:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:217:24)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:166:5)
    at node:internal/main/run_main_module:30:49 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
}

Node.js v22.9.0
```

- Delete the `node_modules` folder
- Run on terminal: `npm install -D tailwindcss autoprefixer postcss`
- Now your `npm run build` should work
