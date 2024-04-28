# this module has 2 classes: Scanner and Drive that the AntiVirus class use for better organized and clear code
import os


class Drive:

    """
    this class represent a drive in the computer with 3 fields:
    1. drive name
    2. drive type
    3. drive unique id

    it also has the ability to tell us if the drive is flash drive by checking its own type
    """

    # can be init with a complete shell line or with the actual fields
    def __init__(self, d_name=None, d_type=None, d_id=None, shell_line=None):
        if shell_line:
            self.name, self.type, self.id = parse_shell_line(shell_line)
        else:
            self.name, self.type, self.id = d_name, d_type, d_id

    def __eq__(self, other) -> bool:
        if isinstance(other, Drive):
            return self.name == other.name and self.type == other.type and self.id == other.id
        else:
            return False

    def __repr__(self) -> str:
        return f"drive name:{self.name} | drive type:{self.type} | drive ID:{self.id}"

    # type 2 is what signals a drive being removable (flash drive) in windows
    def is_flash_drive(self) -> bool:
        return self.type == "2" and self.id is not None


class Scanner:

    """
    this class interacts with the os and perform all the necessary operations with the flash drives
    """

    def __init__(self, config: dict):
        self.config = config  # contains all the "rules" that decides whether a file might be harmful - users choice

    # the logic of scanning the flash drive
    def scan(self, flash_drive: Drive) -> list[str]:
        pot_threats = []
        for root, dirs, files in os.walk(flash_drive.name):
            for file in files:
                file_path = str(os.path.join(root, file))
                if self.potential_threat(file, file_path):
                    pot_threats.append(file_path)
        return pot_threats

    # decides if a file is a potential threat
    def potential_threat(self, dir_name: str, dir_path: str) -> bool:
        return self.bad_ending(dir_name) or self.bad_name(dir_name) or self.check_exe(dir_path)

    # check if the file ends with an ending we think might be problematic
    def bad_ending(self, dir_name: str) -> bool:
        for ending in self.config["bad_endings"]:
            if dir_name.endswith(ending):
                return True
        return False

    # check if the file name indicate about it being problematic
    def bad_name(self, dir_name: str) -> bool:
        return dir_name.split('.')[0] in self.config["bad_names"]

    # checks if the user wanted to check exe permission and if he wanted to know return if the file has exe permission
    def check_exe(self, dir_path: str) -> bool:
        return os.access(dir_path, os.X_OK) if self.config["check_exe"] else False

    # uses the OS to remove a specific file
    @staticmethod  # can be removed
    def remove(file_to_remove):
        os.remove(file_to_remove)


# parsing a shell line into drive name, drive type and drive id
def parse_shell_line(shell_line: str) -> tuple[str, str, str]:
    attributes = list(filter(lambda attr: attr != "", shell_line.strip().split()))
    return attributes[0], attributes[1], attributes[2] if len(attributes) == 3 else None



