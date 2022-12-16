(function (window, document) {

    // we fetch the elements each time because docusaurus removes the previous
    // element references on page navigation
    function getElementsLeft() {
        return {
            layout: document.getElementById('layout'),
            menuLeft: document.getElementById('menu-left'),
            menuLeftLink: document.getElementById('menu-left-link')
        };
    }

    function toggleClassLeft(element, className) {
        var classes = element.className.split(/\s+/);
        var length = classes.length;
        var i = 0;

        for (; i < length; i++) {
            if (classes[i] === className) {
                classes.splice(i, 1);
                break;
            }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        }  else {
            classes.push("no-"+className)
        }

        element.className = classes.join(' ');
    }

    function toggleAllLeft() {
        var active = 'active-left';
        var elements = getElementsLeft();

        toggleClassLeft(elements.layout, active);
        toggleClassLeft(elements.menuLeft, active);
        toggleClassLeft(elements.menuLeftLink, active);
    }
    
    function handleEventLeft(e) {
        console.log("here")
        var elements = getElementsLeft();
        toggleAllLeft();
        e.preventDefault();     
    }
    
    document.getElementById('menu-left-link').addEventListener('click', handleEventLeft);
    
    
    function getElementsRight() {
        return {
            layout: document.getElementById('layout'),
            menuRight: document.getElementById('menu-right'),
            menuRightLink: document.getElementById('menu-right-link')
        };
    }

    function toggleClassRight(element, className) {
        var classes = element.className.split(/\s+/);
        var length = classes.length;
        var i = 0;

        for (; i < length; i++) {
            if (classes[i] === className) {
                classes.splice(i, 1);
                break;
            }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        } else {
            classes.push("no-"+className)
        }

        element.className = classes.join(' ');
    }

    function toggleAllRight() {
        var active = 'active-right';
        var elements = getElementsRight();

        toggleClassRight(elements.layout, active);
        toggleClassRight(elements.menuRight, active);
        toggleClassRight(elements.menuRightLink, active);
    }
    
    function handleEventRight(e) {
        var elements = getElementsRight();
        toggleAllRight();
        e.preventDefault();
    }
    
    document.getElementById('menu-right-link').addEventListener('click', handleEventRight);
    
    
    
    var menu = document.getElementById('menu'),
    rollback,
    WINDOW_CHANGE_EVENT = ('onorientationchange' in window) ? 'orientationchange':'resize';

function toggleHorizontal() {
    menu.classList.remove('closing');
    [].forEach.call(
        document.getElementById('menu').querySelectorAll('.custom-can-transform'),
        function(el){
            el.classList.toggle('pure-menu-horizontal');
        }
    );
};

function toggleMenu() {
    // set timeout so that the panel has a chance to roll up
    // before the menu switches states
    if (menu.classList.contains('open')) {
        menu.classList.add('closing');
        rollBack = setTimeout(toggleHorizontal, 500);
    }
    else {
        if (menu.classList.contains('closing')) {
            clearTimeout(rollBack);
        } else {
            toggleHorizontal();
        }
    }
    menu.classList.toggle('open');
    document.getElementById('toggle').classList.toggle('x');
};

function closeMenu() {
    if (menu.classList.contains('open')) {
        toggleMenu();
    }
}

document.getElementById('toggle').addEventListener('click', function (e) {
    toggleMenu();
    e.preventDefault();
});

window.addEventListener(WINDOW_CHANGE_EVENT, closeMenu);


    
}(this, this.document));
