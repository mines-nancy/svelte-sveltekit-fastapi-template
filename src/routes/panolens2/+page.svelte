<script>
    import {onMount} from "svelte";
    import * as THREE from 'three';

    // https://r105.threejsfundamentals.org/threejs/lessons/threejs-cameras.html
    onMount( async () => {
        //const {TrackballControls}  = await import('three/examples/jsm/controls/TrackballControls');
        const {OrbitControls}  = await import('three/examples/jsm/controls/OrbitControls');
        var panOffset = new THREE.Vector3();



        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
        camera.position.set(0, 10, 20);

        const renderer = new THREE.WebGLRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        document.body.appendChild( renderer.domElement );

        {
            const geometry = new THREE.BoxGeometry(1, 2, 3);
            const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
            const cube = new THREE.Mesh(geometry, material);
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
            var MAX_POINTS = 1000;
            var settings = {
                animation: '',
                points: 100,
                pointSize: 2,
            }
            let points = new Array(MAX_POINTS);
            var i = 0;

            while (i < MAX_POINTS) {
                console.log(i)
                var x = 2 * Math.random() - 1;
                var y = 2 * Math.random() - 1;
                var z = 2 * Math.random() - 1;
                points[i] = new THREE.Vector3(x, y, z);
                i++;
            }

            var geometry = new THREE.Geometry();
            for (i = 0; i < settings.points; i++) {
                geometry.vertices.push(points[i]);
            }
            var material = new THREE.PointsMaterial({
                color: "yellow",
                size: settings.pointSize,
                sizeAttenuation: false
            });
            var pointCloud = new THREE.Points(geometry,material);
            scene.add(pointCloud);

        }

        {
            var MAX_POINTS = 1000;
            var settings = {
                animation: '',
                points: 100,
                pointSize: 2,
            }
            let points = new Array(MAX_POINTS);
            var i = 0;

            while (i < MAX_POINTS) {
                console.log(i)
                var x = 2 * Math.random() - 1;
                var y = 2 * Math.random() - 1;
                var z = 2 * Math.random() - 1;
                points[i] = new THREE.Vector3(x, y, z);
                i++;
            }

            var geometry = new THREE.Geometry();
            for (i = 0; i < settings.points; i++) {
                geometry.vertices.push(points[i]);
            }
            var material = new THREE.PointsMaterial({
                color: "green",
                size: settings.pointSize,
                sizeAttenuation: false
            });
            var pointCloud = new THREE.Points(geometry,material);
            scene.add(pointCloud);

        }


        // const controls = new TrackballControls(camera, renderer.domElement);

        // controls.minDistance = 0;
        // controls.maxDistance = Infinity;

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.target.set(0, 5, 0);


        controls.update();

        function animate() {
            requestAnimationFrame( animate );
            controls.update();
            renderer.render( scene, camera );
        };

        window.addEventListener( 'resize', onWindowResize, false );
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize( window.innerWidth, window.innerHeight );
            controls.target.add( panOffset );
            controls.update();
            //controls.handleResize();
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
        document.addEventListener('wheel', function(e) {
            // pos += e.deltaY * .001;
            // if ( pos < 0 ) pos = 0;
            // if ( pos > 1 ) pos = 1;
        });

        animate();
    })
</script>

<div>

</div>

