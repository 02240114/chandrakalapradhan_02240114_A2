
from chandrakala_02240114_A2_PA import PokemonBinderManager

class PokemonCardBinder(PokemonBinderManager):
    """
    Enhanced Pokemon card binder that extends the manager class.
    Adds position tracking and pokedex number validation.
    """
    
    CARDS_PER_PAGE = 20
    ROWS = 4
    COLUMNS = 5
    MAX_POKEDEX = 1025

    def __init__(self):
        """Initialize with parent class and add position tracking."""
        super().__init__()  # Initialize the parent class
        
    def get_position(self, index):
        """
        Calculate the page, row, and column position of a card in the binder.
        Returns tuple: (page, row, column)
        """
        page = (index // self.CARDS_PER_PAGE) + 1
        position = index % self.CARDS_PER_PAGE
        row = (position // self.COLUMNS) + 1
        column = (position % self.COLUMNS) + 1
        return page, row, column

    def add_card(self):
        """Enhanced version that handles pokedex numbers and positions."""
        print("\nSelect option: 1")
        try:
            pokedex = int(input("Enter Pokedex number: "))
            if not 1 <= pokedex <= self.MAX_POKEDEX:
                print(f"Invalid input. Please enter between 1 and {self.MAX_POKEDEX}.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        card_name = f"Pokedex #{pokedex}"
        
        if card_name in self.binder:
            index = self.binder.index(card_name)
            page, row, col = self.get_position(index)
            print("\nOutput:")
            print(f"Page: {page}")
            print(f"Position: Row {row}, Column {col}")
            print("Status: already exists in binder")
        else:
            self.binder.append(card_name)
            index = len(self.binder) - 1
            page, row, col = self.get_position(index)
            print("\nOutput:")
            print(f"Page: {page}")
            print(f"Position: Row {row}, Column {col}")
            print(f"Status: Added {card_name} to binder")

    def view_binder(self):
        """Enhanced view that shows positions."""
        print("\nSelect option: 3")
        print("Current Binder Contents:")
        print("--------------------------")
        if not self.binder:
            print("The binder is empty.")
        else:
            for index, card in enumerate(self.binder):
                page, row, col = self.get_position(index)
                print(f"{card}:")
                print(f"  Page: {page}")
                print(f"  Position: Row {row}, Column {col}")
        print("--------------------------")
        print(f"Total cards in binder: {len(self.binder)}")
        percent = (len(self.binder) / self.MAX_POKEDEX) * 100
        print(f"% completion: {round(percent, 1)}%")

    def reset_binder(self):
        """Enhanced reset with confirmation."""
        print("\nSelect option: 2")
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        response = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").strip().upper()
        if response == "CONFIRM":
            super().reset_binder()  # Call parent's reset method
            print("The binder reset was successful!")
        elif response != "EXIT":
            print("Invalid input. Reset cancelled.")

if __name__ == "__main__":
    binder = PokemonCardBinder()
    binder.main_menu()  # Inherited from PokemonBinderManager
    