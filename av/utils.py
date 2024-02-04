import os


class Scanner:
    def __init__(self):
        self._endings = [".py", ".exe", ".js", ".java", ".ts", ".inf"]  # add more

    def scan(self, flash_drive):
        pot_threats = []
        for root, dirs, files in os.walk(flash_drive.name):
            for file in files:
                file_path = os.path.join(root, file)
                if self.potential_threat(file, file_path):
                    pot_threats.append(file_path)
        return pot_threats

    def potential_threat(self, dir_name, dir_path):
        return self.bad_ending(dir_name) or dir_name.startswith("autorun") or dir_name.startswith("autoplay")
        # or self.has_url(dir_path=dir_path)

    def bad_ending(self, dir_name):
        for ending in self._endings:
            if dir_name.endswith(ending):
                return True
        return False

    @staticmethod  # can be removed
    def remove(file_to_remove):
        print(f"os.remove({file_to_remove})")


def parse_shell_line(shell_line):
    attributes = list(filter(lambda attr: attr != "", shell_line.strip().split()))
    return attributes[0], attributes[1], attributes[2] if len(attributes) == 3 else None


class Drive:
    def __init__(self, name=None, type=None, id=None, shell_line=None):
        if shell_line:
            self.name, self.type, self.id = parse_shell_line(shell_line)
        else:
            self.name, self.type, self.id = name, type, id

    def __eq__(self, other):
        if isinstance(other, Drive):
            return self.name == other.name and self.type == other.type and self.id == other.id
        else:
            return False

    def __str__(self):
        return f"drive name:{self.name} | drive type:{self.type} | drive ID:{self.id}"

    def is_flash_drive(self):
        return self.type == "2" and self.id is not None
