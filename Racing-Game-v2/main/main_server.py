import game
import communication as comm


def main():
    addr = "127.0.0.1", 5555
    my_comm = comm.Server(addr)
    server_game = game.Game(my_comm, "Racing-Game-Server-v2")
    server_game.start()


if __name__ == "__main__":
    main()
