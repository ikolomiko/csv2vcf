from dataclasses import dataclass


@dataclass
class Member:
    name: str
    telno: str
    email: str
    note: str

    @classmethod
    def parse_list(cls, l: list[str]):
        [firstName,lastName,mobileNumber,platform,email,studentID,department,degree] = l

        platform = platform.lower().strip()
        if "signal" in platform:
            platform = "S "
        elif "whatsapp" in platform:
            platform = "W "
        elif "telegram" in platform:
            platform = "T "
        else:
            platform = "N "

        note = f"{studentID} {department} {degree}"

        name = "OYT23" + platform + firstName.strip() + " " + lastName.strip()

        telno = mobileNumber.replace(" ", "")
        if telno.startswith('5'):
            telno = '+90' + telno
        elif telno.startswith('0'):
            telno = '+9' + telno

        return cls(name, telno, email, note)

    def __repr__(self) -> str:
        return f'"{self.name}","{self.telno}","{self.email}","{self.note}"\n'

    def __str__(self) -> str:
        return self.__repr__()