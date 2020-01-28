class Client:

    def __init__(self):
        print('loading')

    def send_email(template_name, to_address, data_mapping):
        endpoint = "https://api.trusender.com/v1/sendEmail"
        print(endpoint)
        return endpoint