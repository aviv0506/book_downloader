import logic


def activate():
    user_preferences = logic.get_data()
    activate = logic.download_content(user_preferences)


if __name__ == '__main__':
    activate()

uwh37ejsi2838
