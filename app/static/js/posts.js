function HideSessionContent() {
    var content = document.getElementById("sessionForm");
    if (content.style.display == 'none') {
        content.style.display = 'block';
        document.getElementById("sessionToggle").innerHTML = "Create New Session";    
    } else {
        content.style.display = 'none';
        document.getElementById("sessionToggle").innerHTML = "Hide Session Form";
    }

}

function HideEventContent() {
    var content = document.getElementById("eventForm");
    if (content.style.display == 'none') {
        content.style.display = 'block';
        document.getElementById("eventToggle").innerHTML = "Create New Event";    
    } else {
        content.style.display = 'none';
        document.getElementById("eventToggle").innerHTML = "Hide Event Form";
    }

}