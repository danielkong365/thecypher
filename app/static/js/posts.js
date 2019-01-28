function HideContent() {
    var content = document.getElementById("sessionForm");
    if (content.style.display == 'none') {
        content.style.display = 'block';
        document.getElementById("sessionToggle").innerHTML = "Create New Session";    
    } else {
        content.style.display = 'none';
        document.getElementById("sessionToggle").innerHTML = "Hide Session Form";
    }

}