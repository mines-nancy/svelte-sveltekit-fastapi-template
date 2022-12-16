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

## Install FastAPI on Ubuntu 20.04

Information needed to install NodeJS 18 on Ubuntu 20.04 are available here:
> https://github.com/tiangolo/fastapi

To summarize:
```
sudo apt install -y uvicorn
pip3 install fastapi
pip3 install "uvicorn[standard]"
```

## Clone, Install and start the svelte-sveltekit-fastapi-template project

```commandline
git clone git@github.com:mines-nancy/svelte-sveltekit-fastapi-template.git
cd svelte-sveltekit-fastapi-template
npm install
```

Then, to run in dev mode the sveltekit web app:

```commandline
cd svelte-sveltekit-fastapi-template
npm run dev
```

To finish, in a second terminal, start the fastapi backend:
```commandline
cd svelte-sveltekit-fastapi-template/fastapi
uvicorn main:app --reload
```

## Creating a new Svelte project 

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm create svelte@latest

# create a new project in my-app
npm create svelte@latest my-app
cd myapp
npm install
npm run dev
```


