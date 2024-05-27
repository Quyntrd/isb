import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout, 
    QWidget,
    QFileDialog)

from additional_funcs import find_card_data, luhn_algorithm, time_measurement


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Initializes the main application window with buttons and layouts."""
        super(MainWindow, self).__init__()

        self.setGeometry(100, 100, 300, 400)
        self.setMaximumSize(700, 500)

        self.setWindowTitle("Получение номера карты по хэшу")

        widget = QWidget()
        layout = QVBoxLayout()

        self.btn_bins = QLineEdit(placeholderText="Введите список BIN-ов через запятую без пробелов (например 220412)")
        self.btn_hash_card = QLineEdit(placeholderText="Введите хэш")
        self.btn_last_number = QLineEdit(placeholderText="Введите последние 4 цифры карты")

        self.btn_number_search = QPushButton("Найти номер карты по хэшу")
        self.btn_number_search.clicked.connect(self.find_number)
        self.btn_luhn = QPushButton("Проверить номер карты по алгоритму Луна")
        self.btn_luhn.setEnabled(False)
        self.btn_luhn.clicked.connect(self.luhn_algorithm)
        self.btn_graph = QPushButton("Построить график зависимости времени от процессов")
        self.btn_graph.clicked.connect(self.graph_draw)
        self.btn_exit = QPushButton("Выйти из программы")
        self.btn_exit.clicked.connect(lambda: self.shutprocess())
        
        self.card_number_label = QLabel()
        self.card_number_label.setText("Номер карты: ")
        self.card_number_label.setFixedSize(500,15)
        self.card_number_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.card_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.card_number = ""

        layout.addWidget(self.btn_bins)
        layout.addWidget(self.btn_hash_card)
        layout.addWidget(self.btn_last_number)
        layout.addWidget(self.btn_number_search)
        layout.addWidget(self.card_number_label)
        layout.addWidget(self.btn_luhn)
        layout.addWidget(self.btn_graph)
        layout.addWidget(self.btn_exit)
        
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

        self.show()

    def find_number(self) -> None:
        """
        Checks the data entered by the user and calls the function to search for the card number by hash.
        """
        file_path = QFileDialog.getSaveFileName(
                self,
                "Выберите файл для сохранения найденного номера:",
                "",
                "JSON File(*.json)",
            )[0]
        bins = self.btn_bins.text().split(",")
        hash_card = self.btn_hash_card.text()
        last_number = self.btn_last_number.text()
        if (
            (bins == [])
            or (hash_card == "")
            or (last_number == "")
        ):
            QMessageBox.warning(
                self,
                "Внимание!",
                "Были указаны не все данные карты для поиска номера",
            )
        else:
            result = find_card_data(
                bins,
                hash_card,
                last_number,
                file_path
            )
            if result:
                self.card_number_label.setText("Номер карты: " + result)
                self.card_number = result
                QMessageBox.information(None, "Успешно", f"Номер карты найден и успешно сохранен в {file_path}")
                self.btn_luhn.setEnabled(True)
            else:
                QMessageBox.information(None, "Ошибка", "Номер карты не найден")

    def luhn_algorithm(self) -> None:
        """
        Calls a function to verify the validity of the card number using the Luhn algorithm.
        """
        if self.card_number == "":
            QMessageBox.warning(
                None, "Сначала нужно получить номер карты", "Номер карты не был получен."
            )
        else:
            result = luhn_algorithm(self.card_number)
            if result is not False:
                QMessageBox.information(
                    None, "Результат проверки", "Номер карты действителен."
                )
            else:
                QMessageBox.information(
                    None, "Результат проверки", "Номер карты недействителен."
                )

    def graph_draw(self) -> None:
        """
        Calls a function to plot the execution time depending on the number of processes.
        """
        bins = self.btn_bins.text().split(",")
        if (bins == "") or (self.btn_hash_card == "") or (self.btn_last_number == ""):
            QMessageBox.information(
                None,
                "Были указаны не все данные карты",
                "Пожалуйста, заполните все данные карты.",
            )
        else:
            time_measurement(bins, self.btn_hash_card.text(), self.btn_last_number.text())
            QMessageBox.information(None, "Успешно", "График построен")
            
    def shutprocess(self):
        """
        Closes the application window with a confirmation request from the user.
        """
        reply = QMessageBox.question(self, 'Закрытие', 'Вы уверены что хотите закрыть окно?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())