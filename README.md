## Install NodeJS 18 on Ubuntu 20.04

Information needed to install NodeJS 18 on Ubuntu 20.04 are available here:
> https://joshtronic.com/2022/04/24/how-to-install-nodejs-18-on-ubuntu-2004-lts/

To summarize:
```
sudo apt update
sudo apt upgrade
sudo apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
node --version
```

## Install FastAPI and Uvicorn on Ubuntu 20.04

Information needed to install NodeJS 18 on Ubuntu 20.04 are available here:
> https://github.com/tiangolo/fastapi

To summarize:
```
sudo apt install python3-pip
sudo apt install -y uvicorn
pip3 install fastapi
pip3 install "uvicorn[standard]"
pip3 install python-dotenv
```

More information about Uvicorn configuration here: https://www.uvicorn.org/deployment/

## Install Honcho on Ubuntu 20.04

Information needed to install Honcho on Ubuntu 20.04 are available here:
> https://honcho.readthedocs.io/en/latest/

To summarize:
```
pip3 install honcho
```

## Install what needed by HERawS analysis program

To summarize:
```
pip3 install numpy
pip3 install pandas
pip3 install openpyxl
```

## Install OpenAI package

To summarize:
```
pip3 install openai
```

## Clone and install the svelte-sveltekit-fastapi-template project

```commandline
git clone git@github.com:mines-nancy/svelte-sveltekit-fastapi-template.git
cd svelte-sveltekit-fastapi-template
npm install
```

Copy scripts/dev/.env.example to scripts/dev/.env and modify the expected values.
Copy scripts/prod/.env.example to scripts/prod/.env and modify the expected values.

## Developing mode

Once you've created a project and installed dependencies, then,
to run in dev mode the sveltekit web app with auto reloading:

```commandline
honcho -f scripts/dev/Procfile start
```

To configure the web app config, modify what you expect in the part 'config.server'
in the file 'vite.config.js'. 

More information available here : https://vitejs.dev/config/

## Production mode

Once you've created a project and installed dependencies then,
to run in prod mode the sveltekit web app:

```commandline
honcho -f scripts/prod/Procfile start
```

To configure the web app config, modify what you expect in the part 'config.preview'
in the file 'vite.config.js'. 

More information available here : https://vitejs.dev/config/

## Docker

https://www.cloudbees.com/blog/using-honcho-create-multi-process-docker-container
