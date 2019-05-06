import game
import communication as comm


def main():
    addr = "127.0.0.1", 5555
    my_comm = comm.Client(addr)
    client_game = game.Game(my_comm, "Racing-Game-Client-v2")
    client_game.start()


if __name__ == "__main__":
    main()
