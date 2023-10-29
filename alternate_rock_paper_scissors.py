from getpass import getpass as input

print("Play rock, paper, scissors!")
print()

player1 = input(
    "Player 1, make your choice: Rock  🪨(r), Paper 📄(p), or Scissors ✂️(s)? ")
player2 = input(
    "Player 2, make your choice: Rock  🪨(r), Paper 📄(p), or Scissors ✂️(s)? ")

# winning combinations: r > s; p > r; s > p
if player1.lower() == "r" and player2.lower() == "s":
    print("Player 1's rock 🪨 smashes Player 2's scissors ✂️, Player 1 wins!")
elif player1.lower() == "s" and player2.lower() == "p":
    print(
        "Player 1's scissors ✂️ cut up Player 2's paper 📄 into bits and pieces, Player 1 wins!"
    )
elif player1.lower() == "p" and player2.lower() == "r":
    print("Player 1's paper 📄 smothers Player 2's rock 🪨, Player 1 wins!")
elif player2.lower() == "r" and player1.lower() == "s":
    print(
        "Player 2's rock 🪨 makes metal-dust out of Player 1's scissors ✂️, Player 2 wins!"
    )
elif player2.lower() == "s" and player1.lower() == "p":
    print(
        "Player 2's scissors ✂️ make confetti out of Player 1's paper 📄, Player 2 wins!"
    )
elif player2.lower() == "p" and player1.lower() == "r":
    print("Player 2's paper 📄 smother's Player 1's rock 🪨, Player 2 wins!")
elif player1.lower() == "p" and player2.lower() == "p":
    print("Two bits of paper 📄📄 flap at each other. Disappointing. Draw.")
elif player1.lower() == "s" and player2.lower() == "s":
    print(
        "Ka-Shing! Scissors ✂️✂️ bounce off each other like a dodgy sword fight! Draw."
    )
elif player1.lower() == "r" and player2.lower() == "r":
    print("Two rocks 🪨🪨 clink together. It's a tie.")
else:
    print("This is awkward...")