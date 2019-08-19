from flask import jsonify


class HttpRequestError(Exception):
	def __init__(self, err_msg):
		self.err_msg = err_msg


	@property
	def response(self):
		return jsonify({'err': self.err_msg}), self.status_code


class BadRequest(HttpRequestError):
	status_code = 400


class NotFound(HttpRequestError):
	status_code = 404


class NotAcceptable(HttpRequestError):
	status_code = 406
		