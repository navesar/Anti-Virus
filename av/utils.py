import os


class Scanner:
    def __init__(self):
        self._endings = [".py", ".exe", ".js"]  # add more

    def scan(self, flash_drive_name):
        listdir = os.listdir(flash_drive_name)
        return [dir_name for dir_name in listdir if self.potential_threat(dir_name)]

    def potential_threat(self, dir_name):
        return self.bad_ending(dir_name)  # or self.has_url(dir_name)

    def bad_ending(self, dir_name):
        for ending in self._endings:
            if dir_name.endswith(ending):
                return True
        return False

    def deal(self, dir_path):
        print(f"Dealing with bad file at {dir_path}")


def parse_shell_line(shell_line):
    attributes = list(filter(lambda attr: attr != "",shell_line.strip().split(" ")))
    return attributes[0], attributes[1], attributes[2] if len(attributes) == 3 else None


class Drive:
    def __init__(self, shell_line):
        self.name, self.type, self.id = parse_shell_line(shell_line)

    def __eq__(self, other):
        if isinstance(other, Drive):
            return self.name == other.name and self.type == other.type and self.id == other.id
        else:
            return False

    def __str__(self):
        return f"drive name:{self.name} | drive type:{self.type} | drive ID:{self.id}"

    def is_flash_drive(self):
        return self.type == "2"
