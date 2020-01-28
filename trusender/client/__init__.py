# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from ..transport import Transport


logger = logging.getLogger("elasticsearch")


class Trusender:

    def __init__(self):
        print('loading')

    def send_email(template_name, to_address, data_mapping):
        endpoint = "https://api.trusender.com/v1/sendEmail"
		request_data = array(
			'auth_token' => auth_token,
			'email' => to_address,
			'name' => event_name,
			"properties" => properties
		);
        return endpoint

    def send()
    	print('coming soon...')