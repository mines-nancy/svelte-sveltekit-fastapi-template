<script>
  import { onMount, onDestroy } from 'svelte';
  import SegmentedButton, { Segment } from '@smui/segmented-button';
  import Button, { Icon } from '@smui/button';
  import Select, { Option } from '@smui/select';
  import { Label } from '@smui/common';
  import {PUBLIC_FASTAPI_URL} from "$env/static/public";

  let intervalId;
  let milliseconds = 0;
  let seconds = 0;
  let minutes = 0;
  let hours = 0;
  let isRunning = false;
  let selectedTask = "";
  const tasks = ["Tache 1", "Tache 2", "Tache 3"];


  function startTimer() {
    if (isRunning) {
      clearInterval(intervalId);
      isRunning = false;
    } else {
      intervalId = setInterval(() => {
        milliseconds++;
        if (milliseconds === 100) {
          seconds++;
          milliseconds = 0;
        }
        if (seconds === 60) {
          minutes++;
          seconds = 0;
        }
        if (minutes === 60) {
          hours++;
          minutes = 0;
        }
        localStorage.setItem('timer', `${hours},${minutes},${seconds},${milliseconds}`);
      }, 10);
      isRunning = true;
    }
  }

    async function resetTimer() {
    clearInterval(intervalId);
    let currentTime = {hours, minutes, seconds, milliseconds};
    milliseconds = 0;
    seconds = 0;
    minutes = 0;
    hours = 0;
    isRunning = false;
    localStorage.removeItem('timer');
    await saveToCSV(currentTime);
    }

  async function saveToCSV(time) {
    try {
      const response = await fetch(PUBLIC_FASTAPI_URL+'/save_timer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({...time,task: selectedTask})
      });

      if (!response.ok) {
        throw new Error('Erreur lors de la sauvegarde des données du timer');
      }

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error('Erreur:', error);
    }
  }

  onMount(() => {
    const timerValue = localStorage.getItem('timer');
    if (timerValue) {
      const [storedHours, storedMinutes, storedSeconds, storedMilliseconds] = timerValue.split(',');
      hours = Number(storedHours);
      minutes = Number(storedMinutes);
      seconds = Number(storedSeconds);
      milliseconds = Number(storedMilliseconds);
    }
    startTimer();
  });

  onDestroy(() => {
    clearInterval(intervalId);
  });
</script>

<body>
<div>
    <h1>{hours < 10 ? `0${hours}` : hours}:{minutes < 10 ? `0${minutes}` : minutes}:{seconds < 10 ? `0${seconds}` : seconds}.{milliseconds < 10 ? `0${milliseconds}` : milliseconds}</h1>
    <div class="buttons">

        <Select variant="filled" bind:value={selectedTask} label="Choisir une tâche">
            {#each tasks as task}
                <Option value={task}>{task}</Option>
            {/each}
        </Select>

        <Button variant="raised" on:click={startTimer} style="margin-left: 10px">
            <Icon class="material-icons">{isRunning ? 'pause' : 'play_arrow'}</Icon>
            <Label>{isRunning ? 'Pause' : 'Reprendre'}</Label>
        </Button>

        <Button variant="raised" on:click={resetTimer} style="margin-left: 10px">
            <Icon class="material-icons">check</Icon>
            <Label>Fin</Label>
        </Button>

    </div>
</div>
</body>

<style>
  h1 {
    font-size: 8rem;
    text-align: center;
    margin-top: 4rem;
    margin-bottom: 2rem;
  }

  .buttons {
    display: flex;
    justify-content: center;
    margin-top: 2rem;
  }
</style>






