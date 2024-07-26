import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip):
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return False
            return True

        def isIPv6(ip):
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) == 0 or len(part) > 4 or not re.match("^[0-9a-fA-F]+$", part):
                    return False
            return True

        if queryIP.count(".") == 3 and isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(":") == 7 and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

        