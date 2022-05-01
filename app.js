var sendButton = document.querySelector("#sendButton");

sendButton.onclick = function() {
	var emailBodyInput = document.querySelector(".emailBody");
	var emailText = emailBodyInput.value;

	console.log(emailText);

	fetch("http://localhost:8080/email", {
		method: "POST",
		body: emailText,
		credentials: "include",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}
	}).then(function (response) {
		alert("Thank you! Email will be compiled and sent!")
	});
}