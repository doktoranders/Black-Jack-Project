import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 is Ace, 10s are face cards

def deal_initial_cards():
    """Deal one card each to player and computer at the start."""
    player_cards = [random.choice(CARDS)]
    comp_cards = [random.choice(CARDS)]
    print(f"Your first card: {player_cards[0]}")
    print(f"Computer's first card: {comp_cards[0]}")
    return player_cards, comp_cards

def compare(player_cards, comp_cards):
    """Compares scores and prints the result."""
    player_score = sum(player_cards)
    comp_score = sum(comp_cards)

    # Crucial: Player wins if under 21 and beats computer or computer busts
    if player_score <= 21 and (player_score > comp_score or comp_score > 21):
        print(f'You win! {player_cards} vs {comp_cards}')
    elif player_score <= 21 and player_score == comp_score:
        print(f"It's a draw! {player_cards} vs {comp_cards}")
    else:
        print(f'Computer wins! {player_cards} vs {comp_cards}')

def adjust_for_ace(cards):
    """Adjust Ace value from 11 to 1 if total is over 21."""
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

def play_game():
    """Main game loop."""
    while True:
        player_cards, comp_cards = deal_initial_cards()

        # Player's turn
        while True:
            adjust_for_ace(player_cards)
            print(f'Your cards: {player_cards}, total: {sum(player_cards)}')
            print(f"Computer's visible card: {comp_cards[0]}")

            if sum(player_cards) == 21:
                print(f'You win with 21! {player_cards}, {comp_cards}')
                break
            if sum(player_cards) > 21:
                print(f'Bust! Your cards: {player_cards}, total: {sum(player_cards)}')
                print(f'Computer wins with cards: {comp_cards}')
                break

            answer = input('Draw another card? (y/n): ').strip().lower()
            if answer == 'y':
                player_cards.append(random.choice(CARDS))
            elif answer == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Computer's turn (only if player hasn't busted or won with 21)
        if sum(player_cards) <= 21:
            # Crucial: Computer draws until at least 17
            while sum(comp_cards) < 17:
                comp_cards.append(random.choice(CARDS))
                adjust_for_ace(comp_cards)
            print(f"Computer's final cards: {comp_cards}, total: {sum(comp_cards)}")
            compare(player_cards, comp_cards)

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()
