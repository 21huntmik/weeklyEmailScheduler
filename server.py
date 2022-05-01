from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
from socketserver import ThreadingMixIn
import smtplib
from datetime import date
import calendar

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

	emailTextFinal = ""

	def handleNotFound(self):
		self.send_response(404)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		self.wfile.write(bytes("Not Found", "utf-8"))

	def handlePostEmailBody(self):
		length = self.headers["Content-Length"]
		body = self.rfile.read(int(length)).decode("utf-8")
		body += "\n"
		print("printing body: ", body)
		MyHTTPRequestHandler.emailTextFinal += body
		print("Printing global variable += body:", MyHTTPRequestHandler.emailTextFinal)
		MyHTTPRequestHandler.scheduledEmail()

	def do_POST(self):
		if self.path == "/email":
			self.handlePostEmailBody()
		else:
			self.handleNotFound()

	def scheduledEmail():
		gmail_user = "missionarymailwebapp@gmail.com"
		gmail_password = "mobat&them"
		to = "mhunt@missionary.org"
		
		try:
			smtp = smtplib.SMTP("smtp.gmail.com", 587)
			smtp.starttls()
			smtp.login(gmail_user, gmail_password)
			smtp.sendmail(gmail_user, to, MyHTTPRequestHandler.emailTextFinal)
			smtp.quit()
			print("Email sent!")
		except Exception as ex:
			print("Something went wrong ", ex)

def run():
	listen = ("127.0.0.1", 8080)
	server = HTTPServer(listen, MyHTTPRequestHandler)
	print("Server ready!")
	server.serve_forever()

run()
