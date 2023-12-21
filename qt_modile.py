from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, Slot
import sys
from get_images import GetImages

class MyWidget(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image

        self.hello = {
            "1": "Previous word",
            "2": "Next word",
            "3": "Hei maailma",
            "4": "Hola Mundo",
        }

        self.prev_button = QPushButton("Previous word")
        self.next_button = QPushButton("Next word")

        self.message = QLabel("Hello World")
        

        # Add the image_label attribute
        self.image_label = QLabel(self)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.prev_button)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.image_label)  # Add image_label to the layout
        self.layout.addWidget(self.prev_button)
        self.layout.addWidget(self.next_button)
      
        # Example: Resize the image to 200x200 pixels
        self.display_photo(image, width=800, height=600)       
       

        # Connecting the signals to the slots
        self.prev_button.clicked.connect(self.show_previous_word)
        self.next_button.clicked.connect(self.show_next_word)
        
        # Adjust location (optional, as the layout will handle this)
        self.prev_button.move(200, 20)
        self.next_button.move(120, 20)
        
        # Adjust size and location of buttons
        self.prev_button.setFixedSize(120, 30)  # Set fixed size
        self.next_button.setFixedSize(120, 30)  # Set fixed size
        
        

    def display_photo(self, image_data, width=None, height=None):
        image = QImage.fromData(image_data)
        pixmap = QPixmap.fromImage(image)
        if width and height:
            pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)

        self.image_label.setPixmap(pixmap)

    @Slot()
    def show_previous_word(self):
        self.message.setText(self.hello['1'])

    @Slot()
    def show_next_word(self):
        self.message.setText(self.hello['2'])

if __name__ == "__main__":

    gi = GetImages('anna')   
    content = gi.get_image_from_unsplash()    
    image = gi.download_image(content)
    

    app = QApplication(sys.argv)
    widget = MyWidget(image)
    widget.show()
    sys.exit(app.exec())
    