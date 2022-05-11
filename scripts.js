function sendSuggestion() {
    var suggestion = document.getElementById("idea-box").value;

    const sendURL = `http://127.0.0.1:8080/suggestion/?suggestion=${suggestion}`;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", sendURL, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
}

function opengithubrepo() {
    window.open("https://github.com/iUseYahoo/Idea-Suggester");
}