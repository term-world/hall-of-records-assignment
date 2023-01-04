import json
import narrator

from rich.table import Table
from rich.console import Console
from inventory import FixtureSpec

# Do not alter -----------------------------------------------
DATA = None

class Processor(FixtureSpec):

    def __init__(self):
        super().__init__()
        self.filename = "records/data.json"
        self.data = self.__load()

    def __load(self) -> dict:
        fh = open(self.filename, "r")
        data = json.load(fh)
        for item in data:
            idx = data.index(item)
            id = {"#": idx + 1}
            id.update(data[idx])
            data[idx] = id
        return data

    def display_menu(self) -> any:
        n = narrator.Narrator()
        q = narrator.Question({
            "question": "\nOperation to perform:\n",
            # You might alter this to add a feature ------------
            "responses": [
                {"choice": "1 search rows ", "outcome": 1},
                {"choice": "2 total a column ", "outcome": 2},
                {"choice": "3 average a column ", "outcome": 3},
                {"choice": "4 print table ", "outcome": 4},
                {"choice": "5 quit", "outcome": False},
                {"choice": "6 SECRET AUTO-AVERAGER", "outcome": "SECRET"}
            ]
            # You might alter this to add a feature ------------
        })
        return q.ask()
    
    def display_table(self) -> None:
        cols = list(self.data[0].keys())
        table = Table(title="term-world CITIZEN DATA")
        for col in cols:
            table.add_column(col)
        for row in self.data:
            entry = [str(item) for item in list(row.values())]
            table.add_row(*entry)
        console = Console()
        console.print(table)
# Do not alter -----------------------------------------------


# TODO: Implement search_rows function according to README, a function
#       which searches a column for a minimum value or _greater_ and 
#       returns all rows which match.

# TODO: Implmement total_column function according to README, a function
#       which adds all numeric values for a column


def main():

    # Do not alter -------------------------------------------
    global DATA
    obj = Processor()
    DATA = obj.data
    response = obj.display_menu()
    # Do not alter -------------------------------------------

    while True:
        
        # TODO: Implement if statements to handle menu options
        #
        # If response is false, break
        # If response is 1, run search_rows
        # If response is 2, run total_column
        # If response is 3, return the average of a given column
        #
        # HINT: Use the pass keyword to put a "placeholder" for all
        #       functionality not yet implement

        if response == 4:
            obj.display_table()
        response = obj.display_menu()

if __name__ == "__main__":
    main()