function arrow_key_press(keyCodeNumber) {

    var key_arrow = document.getElementById('arrow_keys'),
        LEFT = 37,
        UP = 38,
        RIGHT = 39,
        DOWN = 40;

    switch(keyCodeNumber) {
        case LEFT:
            key_arrow.innerHTML = 'Left';
            break;
        case UP:
            key_arrow.innerHTML = 'Up';
            break;
        case RIGHT:
            key_arrow.innerHTML = 'Right';
            break;
        case DOWN:
            key_arrow.innerHTML = 'Down';
            break;
        default:
            key_arrow.innerHTML = 'Other Character (not an arrow key)';
    }    
    key_arrow.innerHTML += ' (keyCode: ' + keyCodeNumber + ')';
}

function checkKeycode(event) {
    var keyDownEvent = event || window.event, keycode = (keyDownEvent.which) ? keyDownEvent.which : keyDownEvent.keyCode;

    arrow_key_press(keycode);

    return false;
}

document.onkeydown = checkKeycode;


//********************************************************
//********************************************************
//********************************************************
//********************************************************