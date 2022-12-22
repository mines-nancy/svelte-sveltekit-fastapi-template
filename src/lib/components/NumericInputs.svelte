<!-- https://svelte.dev/examples/numeric-inputs -->

<script>

	import axios from "axios";
	import { onMount } from "svelte";
	import { PUBLIC_FASTAPI_URL } from '$env/static/public';

	let a = 1;
	let b = 2;
	$: c = a + b;
	let posts = {};

	async function sendData(){
		try {
			// const response = await axios.get("http://localhost:8000/helloworld");
			// const response = await axios.get("http://localhost:8000/helloworld?name=kiki&name2=kiko");
			// const response = await axios.get("http://localhost:8000/helloworld/défdé/abc");
			const response = await axios.post(
					PUBLIC_FASTAPI_URL+"/helloworld",
					{"name":"nina", "age": c}
			);
			posts = response.data;
			console.log(posts);
		} catch (error) {
			console.error(error);
		}
	}
	onMount( () => sendData() );
</script>

<label>
	<input type=number bind:value={a} min=0 max=10>
	<input type=range bind:value={a} min=0 max=10>
</label>

<label>
	<input type=number bind:value={b} min=0 max=10>
	<input type=range bind:value={b} min=0 max=10>
</label>

<p>{a} + {b} = {a + b}</p>
<p>{a} + {b} = {c}</p>
<button on:click={sendData}> Click </button>
<h2>FROM AJAX: {JSON.stringify(posts)}</h2>
