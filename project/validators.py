class Validators:
    @staticmethod
    def check_name_and_kind(name, message):
        if name.strip() == "":
            raise ValueError(message)

    @staticmethod
    def check_price(price, message):
        if price <= 0.0:
            raise ValueError(message)
