import argparse
import getMonth


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--login", action="store_true", help="Log into the system"
    )
    parser.add_argument(
        "-o", "--logout", action="store_true", help="Log out of the system"
    )

    args = parser.parse_args()

    getMonth.mkFolder()

    if args.login:
        getMonth.logIn()
        print(
            f"You clocked in:{getMonth.get_date}, {getMonth.get_time}")

    if args.logout:
        getMonth.logOut()
        print(
            f"You clocked out:{getMonth.get_date}, {getMonth.get_time}")


if __name__ == "__main__":
    main()
