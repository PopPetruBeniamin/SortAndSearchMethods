from application.tests.test_all import test_all
from application.repository.repository import MasinaRepository
from application.service.service import MasinaService
from application.ui.console import MasinaConsole

if __name__ == '__main__':
    test_all()

    repo = MasinaRepository(file_name="data/data")
    service = MasinaService(repo)
    console = MasinaConsole(service)

    console.run_console()
