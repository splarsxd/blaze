from os import system
import requests
import time

# made by splars#1252

prefix = "blaze by splars#1252"
system("title %s" %prefix)
system("color c")


def main():
    global fetch, d

    system("cls")
    print(prefix)

    search = input("\n\n>> ")
    if not search:
        main()

    requests.session().cookies.clear()

    if "." in search:
        server = requests.session().get(f"https://api.mcsrvstat.us/2/{search}").json()

        try:
            if server['online']:
                print(f"\nServer: {search}")
                print(f"IPv4: {server['ip']}:{server['port']}")
                print(f"Status: {server['online']}")
                print(f"Players: {server['players']['online']} / {server['players']['max']}\n")

                print(f"Version: {server['version']}")
                print(f"Protocol: {server['protocol']}")

                system("pause >nul")
                main()

            else:
                print(f"\nServer: {search}")
                print(f"IPv4: {server['ip']}:{server['port']}")
                print(f"Status: {server['online']}")

                system("pause >nul")
                main()

        except:
            print("\n\nPlease, specify an existing username or an online server.")
            time.sleep(2.2)
            main()

    try:
        fetch = requests.session().get(f"https://api.mojang.com/users/profiles/minecraft/{search}").json()

    except:
        print("\n\nPlease, specify an existing username or an online server.")
        time.sleep(2.2)
        main()

    friends = requests.session().get(f"https://api.namemc.com/profile/{fetch['id']}/friends").json()

    try:
        skin = requests.session().get(f"https://crafatar.com/skins/{fetch['id']}").url

    except:
        skin = "You're requesting skins too fast."

    print(f"\nUUID: {fetch['id']}")
    print(f"Current username: {fetch['name']}")
    print("\nProperties:")
    print(f"{skin}")

    try:
        d = 0
        print("\nFriends:")
        while True:
            print(f"{d + 1}: {friends[d]['name']}")
            d += 1

    except:
        if d == 0:
            print(f"{fetch['name']} has no friends.")

        system("pause >nul")
        main()

main()
