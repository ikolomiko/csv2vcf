from dataclasses import dataclass


@dataclass
class Member:
    name: str
    telno: str

    @classmethod
    def parse_list(cls, l: list[str]):
        platform = l[8].lower()
        if "signal" in platform:
            platform = "-S "
        elif "whatsapp" in platform:
            platform = "-W "
        elif "telegram" in platform:
            platform = "-T "
        else:
            platform = "-N "

        name = "OYT" + platform + l[1].strip() + " " + l[2].strip()
        telno = l[7].strip().replace(" ", "")
        return cls(name, telno)

    def __repr__(self) -> str:
        return f'"{self.name}","{self.telno}"\n'

    def __str__(self) -> str:
        return self.__repr__()