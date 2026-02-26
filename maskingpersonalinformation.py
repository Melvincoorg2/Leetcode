def maskPII(self, s: str) -> str:

        # Email case
        if "@" in s:
            s = s.lower()
            name, domain = s.split("@")

            return name[0] + "*****" + name[-1] + "@" + domain

        # Phone case
        else:
            digits = ""

            # remove non-digit characters
            for ch in s:
                if ch.isdigit():
                    digits += ch

            local = digits[-4:]
            country_length = len(digits) - 10

            masked_local = "***-***-" + local

            if country_length == 0:
                return masked_local
            else:
                return "+" + "*" * country_length + "-" + masked_local