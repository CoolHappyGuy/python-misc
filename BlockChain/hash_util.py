import hashlib as hl  # Hashing (sha256, 64 bit method)
import json  # To convert dictionary to string


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

        Arguments:
            :block: The block that should be hashed.

        See lecture 102 for full explanation of the below method chain
        """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
