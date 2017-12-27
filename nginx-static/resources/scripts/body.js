function myFunction(elmnt,clr) {
    elmnt.style.color = clr;
}

function getPeople() {
fetch("http://128.199.176.124/flask").then(function(response) {
	if (response.ok) {response.json()
	.then(function(data) {
		document.getElementById('main-body').innerHTML = JSON.stringify(data); });
	} else { alert('no luck!');
	}
}, function(e) { alert('error!', e);
});
}

function getNews() {
fetch("http://128.199.176.124/news").then(function(response) {
