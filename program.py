from TCP_Server import algorithm_TCP
from threading import Thread

choice = ""

name = input ("Hello, what is your name? ").capitalize()
print (f"Hi there {name} :)")

while (choice != "TCP" or choice != "UDP"):

    choice = input ("Which protocol do you want to monitor? [TCP/UDP] ").upper()
   
    if (choice == "TCP"):

        if __name__ == "__main__":

            client_1 = Thread (target = algorithm_TCP)
            client_2 = Thread (target = algorithm_TCP)
            client_3 = Thread (target = algorithm_TCP)
            client_4 = Thread (target = algorithm_TCP)

            client_1.start()
            client_1.join()

            client_2.start()
            client_2.join()

            client_3.start()
            client_3.join()

            client_4.start()
            client_4.join()

            break

    # elif (choice == "UDP"):

    #         if __name__ == "__main__":

    #             client_1 = Thread (target = algorithm_UDP)
    #             client_2 = Thread (target = algorithm_UDP)
    #             client_3 = Thread (target = algorithm_UDP)
    #             client_4 = Thread (target = algorithm_UDP)

    #             client_1.start()
    #             client_1.join()

    #             client_2.start()
    #             client_2.join()

    #             client_3.start()
    #             client_3.join()

    #             client_4.start()
    #             client_4.join()

    #             break

    else:

        print ("Enter either TCP or UDP")
        print ("Try again")

