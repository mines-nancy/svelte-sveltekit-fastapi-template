<script>
    import {onMount} from "svelte";

    onMount(async ()=>{
        const PANOLENS  = await import('panolens');
        const panorama = new PANOLENS.ImagePanorama( '/public/images/00000-pano.jpg' );
        const viewer = new PANOLENS.Viewer({container: document.getElementById('viewer-360')});
        viewer.add( panorama );
    })
</script>

<div>
    <div id="viewer-360"></div>
</div>

<style>
    #viewer-360{
        width: 800px;
        height: 800px;
    }
</style>