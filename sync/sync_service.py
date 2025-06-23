import threading
import time
from db.database import get_all_products
from db.cloud_database import init_cloud_db, upsert_product

class SyncService:
    def __init__(self, interval=30):
        self.interval = interval
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True)

    def start(self):
        init_cloud_db()
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def run(self):
        print("🛰️ Servicio de sincronización iniciado...")
        while self.running:
            try:
                products = get_all_products()
                for product in products:
                    upsert_product(*product)
                print("✅ Sincronización completada.")
            except Exception as e:
                print(f"❌ Error al sincronizar: {e}")
            time.sleep(self.interval)
