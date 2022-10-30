import re


class Middleware(object):

    @staticmethod
    def bin_is_invalid(bin):
        pattern = re.compile("[A-Za-z0-9]{8}")
        return not bool(re.match(pattern, bin))
