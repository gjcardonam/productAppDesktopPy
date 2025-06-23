import sys
from PySide6.QtWidgets import QApplication
from db.database import init_db
from sync.sync_service import SyncService
from ui.main_window import MainWindow

if __name__ == "__main__":
    init_db()
    sync_service = SyncService(interval=30)  # cada 30 segundos
    sync_service.start()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
