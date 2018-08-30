def to_bs(self,timestamp):
    short_code = "601490"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

    the_date = str(timestamp)
    result = base64.b64encode(passkey,passkey,the_date)
    return result