<script>
    import {onMount} from "svelte";

    onMount(async ()=>{
        const PANOLENS  = await import('panolens');
        const panorama = new PANOLENS.ImagePanorama( '/public/images/00000-pano.jpg' );
        const panorama2 = new PANOLENS.ImagePanorama( '/public/images/00002-pano.jpg' );

        const viewer = new PANOLENS.Viewer({container: document.getElementById('viewer-360')});

        let current_panorama;


        function displayPanorama(new_panorama){
            if(current_panorama!==undefined){
                viewer.remove(current_panorama)
            }
            current_panorama = new_panorama
            viewer.add( current_panorama );
            viewer.setPanorama(current_panorama)
            // const control = viewer.getControl();
            // control.rotateLeft(Math.random()*Math.PI)
        }
        window.setTimeout( ()=>{
            displayPanorama(panorama)
            window.setTimeout( ()=>{
                displayPanorama(panorama2)
            }, 3000)
        }, 3000)
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

