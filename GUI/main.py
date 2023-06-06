import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")


app = QApplication(sys.argv)

button = QPushButton("Click me")

button.clicked.connect(say_hello)

# Show the button
button.show()
# Run the main Qt loop
app.exec()
