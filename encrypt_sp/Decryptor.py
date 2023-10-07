from encrypt_sp.helper.rot_13 import rot_13

class Decryptor:
    def __init__(self, target_file, output=None):
        with open(target_file, "r") as file:
            info = file.read()

        encrypted_info = rot_13(info, idx = -13)

        if not output:
            with open(target_file, "w") as file:
                file.write(encrypted_info)
