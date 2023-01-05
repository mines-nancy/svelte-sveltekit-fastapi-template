import { sveltekit } from '@sveltejs/kit/vite';
import dotenv from "dotenv";

if (process.env && process.env['ENV_MODE'] === 'development') {
	dotenv.config({path: 'scripts/dev/.env'});
} else {
	dotenv.config({path: 'scripts/prod/.env'});
}

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [
		sveltekit()
	],
	server:{
		host: process.env["PUBLIC_SVELTEKIT_HOST"],
		port: process.env["PUBLIC_SVELTEKIT_PORT"],
		strictPort:false,
		cors:true
	},
	preview:{
		host: process.env["PUBLIC_SVELTEKIT_HOST"],
		port: process.env["PUBLIC_SVELTEKIT_PORT"],
		strictPort:false,
		cors:true
	},
	define: {
		'process.env': process.env
	}
};

export default config;
