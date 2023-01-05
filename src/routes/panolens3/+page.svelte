<script>
    import {onMount} from "svelte";
    import * as THREE from 'three';
    import LayoutGrid, { Cell as GridCell} from '@smui/layout-grid';
    import Dialog, { Header, Title, Content, Actions } from '@smui/dialog';
    import IconButton from '@smui/icon-button';
    import Button, { Label } from '@smui/button';

    let current_panorama;
    let current_panorama_id;
    let viewer;
    function closePopup(){
        if(current_panorama!==undefined){
            viewer.remove(current_panorama);
            current_panorama = undefined;
        }
    }

    // https://r105.threejsfundamentals.org/threejs/lessons/threejs-cameras.html
    onMount( async () => {

        const PANOLENS  = await import('panolens');
        let bool = true;


        function displayPanorama(){
            if(bool) {
                viewer = new PANOLENS.Viewer({container: document.getElementById('viewer-360')});
                bool=false;
            }

            const new_panorama = new PANOLENS.ImagePanorama( `/public/images/${current_panorama_id}-pano.jpg` );
            if(current_panorama!==undefined){
                viewer.remove(current_panorama)
            }
            current_panorama = new_panorama
            viewer.add( current_panorama );
            viewer.setPanorama(current_panorama)
            // const control = viewer.getControl();
            // control.rotateLeft(Math.random()*Math.PI)
        }

        const {OrbitControls}  = await import('three/examples/jsm/controls/OrbitControls');

        const scene = new THREE.Scene();
        function width(){
            //return window.innerWidth/2
            return window.innerWidth
        }
        function height(){
            //return 800
            return window.innerHeight
        }
        const camera = new THREE.PerspectiveCamera( 75, width() / height(), 0.1, 1000 );
        camera.position.set(0, 10, 20);

        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(width(),height())
        document.getElementById("three-renderer").appendChild( renderer.domElement );

        let dictionary = {};

        let raycaster = new THREE.Raycaster();
        let INTERSECTED;
        const pointer = new THREE.Vector2();
        {
            const geometry = new THREE.BoxGeometry(5, 2, 3);
            const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
            const cube = new THREE.Mesh(geometry, material);
            cube.position.set(5, 0, 10);
            dictionary[cube.id] = "00000"
            scene.add(cube);
        }

        {
            const geometry = new THREE.BoxGeometry(5, 2, 3);
            const material = new THREE.MeshBasicMaterial({color: 0x0000ff});
            const cube = new THREE.Mesh(geometry, material);
            cube.position.set(-5, 0, -10);
            dictionary[cube.id] = "00002"
            scene.add(cube);
        }

        {
            const planeSize = 40;

            const loader = new THREE.TextureLoader();
            const texture = loader.load('https://r105.threejsfundamentals.org/threejs/resources/images/checker.png');
            texture.wrapS = THREE.RepeatWrapping;
            texture.wrapT = THREE.RepeatWrapping;
            texture.magFilter = THREE.NearestFilter;
            const repeats = planeSize / 2;
            texture.repeat.set(repeats, repeats);

            const planeGeo = new THREE.PlaneBufferGeometry(planeSize, planeSize);
            const planeMat = new THREE.MeshPhongMaterial({
                map: texture,
                side: THREE.DoubleSide,
            });
            const mesh = new THREE.Mesh(planeGeo, planeMat);
            mesh.rotation.x = Math.PI * -.5;
            scene.add(mesh);
        }
        {
            const cubeSize = 4;
            const cubeGeo = new THREE.BoxBufferGeometry(cubeSize, cubeSize, cubeSize);
            const cubeMat = new THREE.MeshPhongMaterial({color: '#8AC'});
            const mesh = new THREE.Mesh(cubeGeo, cubeMat);
            mesh.position.set(cubeSize + 1, cubeSize / 2, 0);
            scene.add(mesh);
        }
        {
            const sphereRadius = 3;
            const sphereWidthDivisions = 32;
            const sphereHeightDivisions = 16;
            const sphereGeo = new THREE.SphereBufferGeometry(sphereRadius, sphereWidthDivisions, sphereHeightDivisions);
            const sphereMat = new THREE.MeshPhongMaterial({color: '#CA8'});
            const mesh = new THREE.Mesh(sphereGeo, sphereMat);
            mesh.position.set(-sphereRadius - 1, sphereRadius + 2, 0);
            scene.add(mesh);
        }

        {
            const color = 0xFFFFFF;
            const intensity = 1;
            const light = new THREE.DirectionalLight(color, intensity);
            light.position.set(0, 10, 0);
            light.target.position.set(-5, 0, 0);
            scene.add(light);
            scene.add(light.target);
        }

        {
            const MAX_POINTS = 1000;
            const settings = {
                animation: '',
                points: 100,
                pointSize: 2,
            }
            const color = new THREE.Color();
            const positions = [];
            const colors = [];

            let i = 0;

            while (i < MAX_POINTS) {
                const x = 2 * Math.random() + 4;
                const y = 2 * Math.random()  + 6;
                const z = 2 * Math.random() - 1;
                positions.push( new THREE.Vector3(x, y, z ));
                colors.push( new THREE.Color( Math.random(),Math.random(), Math.random() ));
                i++;
            }

            const geometry = new THREE.Geometry();
            for (i = 0; i < settings.points; i++) {
                geometry.vertices.push(positions[i]);
                geometry.colors.push(colors[i]);
            }
            const material = new THREE.PointsMaterial( {
                size: 5,
                sizeAttenuation: false,
                vertexColors: true
            } );

            let pointCloud = new THREE.Points( geometry, material );
            scene.add( pointCloud)
        }

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.target.set(0, 5, 0);

        controls.update();

        function animate() {
            requestAnimationFrame( animate );
            controls.update();
            raycaster.setFromCamera( pointer, camera );
            const intersects = raycaster.intersectObjects( scene.children, false );
            if ( intersects.length > 0 ) {
                if ( INTERSECTED !== intersects[0].object ) {
                    INTERSECTED = intersects[0].object;
                }
            } else {
                INTERSECTED = null;
            }
            renderer.render( scene, camera );
        };

        window.addEventListener( 'click', onClick, false );
        function onClick(e){
            if(INTERSECTED !== null && dictionary[INTERSECTED.id]){
                console.log(INTERSECTED.id)
                current_panorama_id = dictionary[INTERSECTED.id]
                open_popup=true
                window.setTimeout( ()=> {
                    displayPanorama()
                }, 500)
            }
        }

        window.addEventListener( 'resize', onWindowResize, false );
        function onWindowResize() {
            camera.aspect = width() / height();
            renderer.setSize(width(),height())
            document.getElementById("three-renderer").style = `width: ${width()}px; height: ${height()}px;`
            camera.updateProjectionMatrix();
            controls.update();
        }

        document.addEventListener( 'keydown', keyboard );
        function keyboard( ev ) {
            switch (ev.keyCode){
                case 17: // CTRL
                    controls.screenSpacePanning = true;
                    break;
            }
        }
        document.addEventListener( 'keyup', keyboard2 );
        function keyboard2( ev ) {
            switch (ev.keyCode){
                case 17: // CTRL
                    controls.screenSpacePanning = false;
                    break;
            }
        }

        document.addEventListener( 'mousemove', onPointerMove );
        function onPointerMove( event ) {
            pointer.x = ( event.clientX / window.innerWidth ) * 2 - 1;
            pointer.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
        }


        animate();
    })

    let open_popup = false;
</script>

<div>
    <div id="three-renderer"></div>
    <div>
        <Dialog
                bind:open={open_popup}
                fullscreen
                aria-labelledby="fullscreen-title"
                aria-describedby="fullscreen-content"
        >
            <Header>
                <Title id="fullscreen-title">Terms and Conditions</Title>
                <IconButton action="close" class="material-icons" on:click={closePopup}>close</IconButton>
            </Header>
            <Content id="fullscreen-content">
                <div id="viewer-360"></div>
            </Content>
        </Dialog>
    </div>

</div>


<style>

    #three-renderer{
        width: 100%;
        height: 100%;
    }
    #viewer-360{
        width: 76vw;
        height: 80vh;

    }
</style>