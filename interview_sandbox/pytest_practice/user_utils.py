def filter_active_users(users: list[dict]) -> list[str]:
    filter_list = [user["name"] for user in users if user["is_active"]]
    return filter_list

