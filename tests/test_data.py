valid_users = [
    ("standard_user", "secret_sauce"),
]

invalid_users = [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("invalid_user", "wrong_password", "do not match"),
]

empty_users = [
    ("", ""),
]