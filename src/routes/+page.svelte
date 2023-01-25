<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    import { PUBLIC_FASTAPI_URL } from '$env/static/public';

    let recognition;
    let transcript = "";
    let responseText = "";
    let text = "";


    onMount(() => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        recognition.interimResults = true
        recognition.onresult = (event) => {
            transcript = event.results[0][0].transcript
            console.log("prompt : " + transcript)
            sendData()
        }
        recognition.start()

        const sendData = async () => {
            try {
                const response = await axios.post(PUBLIC_FASTAPI_URL+'/predict', {text: transcript})
                console.log("GPT : " + response.data)
                text = response.data
                text = text.replace(/\\n/g, '\n')
                text = text.replace(/\\u([a-fA-F0-9]{4})/g, (match, grp) => String.fromCharCode(parseInt(grp, 16)))
                responseText = text
            } catch (error) {
                console.error(error)
            }
        }

    });
</script>
<br>
<p class="GPT">Your prompt :</p>
<div class="GPT">
    <p class = "response">
        {transcript}
    </p>
</div>
<br>
<p class="GPT">GPT Answer :</p>
<div class="GPT">
    <p class = "response">
        {responseText}
    </p>
</div>

<style>
    .response {
        white-space: pre-wrap;
    }
    .GPT {
        margin: auto;
        width: 50%;
    }
    div {

        border: 1px solid gray;
        border-radius: 10px;
        padding: 3px;
        height: auto;
    }
</style>


