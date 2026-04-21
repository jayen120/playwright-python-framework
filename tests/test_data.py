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

security_test_data = [
    ("' OR 1=1 --", "anything", "error"),
    ("admin' --", "anything", "error"), 
    ("standard_user", "' OR '1'='1", "error"),
]