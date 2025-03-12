from application.entities.entities import Masina
from application.repository.repository import MasinaRepository
from application.service.service import MasinaService


# ========== Test Masina class entity =================================================================================
def test_masina():
    masina = Masina("Chevrolet", "Express2500", "etxita8lic", 3976, 11103)

    assert (masina.marca == "Chevrolet"), "Incorrect marca"
    assert (masina.model == "Express2500"), "Incorrect model"
    assert (masina.token_masina == "etxita8lic"), "Incorrect token"
    assert (masina.pret_achizitie == 3976), "Incorrect pret_achizitie"
    assert (masina.pret_vanzare == 11103), "Incorrect pret_vanzare"


# ========== Test Repository class ====================================================================================
def test_repository():
    repo = MasinaRepository(file_name="data/data")

    # Chevrolet Express2500 etxita8lic 3976 11103
    assert (len(repo.load_data()) != 0), "File not read"
    assert (len(repo.find_all()) != 0), "Cars not found"
    assert (repo.find("etxita8lic").marca == "Chevrolet"), "Car not found"
    assert (repo.find("etxita8lic").token_masina == "etxita8lic"), "Car not found"
    assert (repo.find("etxita8lic").model == "Express2500"), "Car not found"
    assert (repo.find("etxita8lic").pret_achizitie == 3976), "Car not found"
    assert (repo.find("etxita8lic").pret_vanzare == 11103), "Car not found"


# ========== Test Service class =======================================================================================
def test_service():
    repo = MasinaRepository(file_name="data/data")
    service = MasinaService(repo)

    # ====== Test .find() method ===================================================

    # Toyota Avalon x8fu5lo3m9 8920 3916
    assert (service.find("x8fu5lo3m9").marca == "Toyota"), "Car not found"
    assert (service.find("x8fu5lo3m9").token_masina == "x8fu5lo3m9"), "Car not found"
    assert (service.find("x8fu5lo3m9").model == "Avalon"), "Car not found"
    assert (service.find("x8fu5lo3m9").pret_achizitie == 8920), "Car not found"
    assert (service.find("x8fu5lo3m9").pret_vanzare == 3916), "Car not found"

    # ====== Test .sort_by_token() method =======================================================================

    # 1 Masina: Marca: Subaru, Model: BRZ, Token masina: 0ibdu3n47t, Pret achizitie: 2987, Pret vanzare: 3046
    # -1 Masina: Marca: Toyota, Model: Mirai, Token masina: zn7jpf4dgp, Pret achizitie: 5806, Pret vanzare: 8925
    by_token = service.sort_by_token()
    assert (by_token[0].token_masina == "0ibdu3n47t"), "Incorrect sort by token"
    assert (by_token[-1].token_masina == "zn7jpf4dgp"), "Incorrect sort by token"

    # ====== Test .sort_by_marca_model() method =======================================================================

    # 1 Masina: Marca: Audi, Model: A3, Token masina: wt98fnpsku, Pret achizitie: 3816, Pret vanzare: 8993
    # -1 Masina: Marca: Volvo, Model: V40, Token masina: foi01znl24, Pret achizitie: 6604, Pret vanzare: 12283
    by_marca_model = service.sort_by_marca_model()
    assert (by_marca_model[0].marca == "Audi" and by_marca_model[0].model == "A3"), "Incorrect sort by marca-model"
    assert (by_marca_model[-1].marca == "Volvo" and by_marca_model[-1].model == "V40"), "Incorrect sort by marca-model"

    # ====== Test .sort_by_marca_model_token() method ========================================================

    # 1 Masina: Marca: Audi, Model: A3, Token masina: wt98fnpsku, Pret achizitie: 3816, Pret vanzare: 8993
    # -1 Masina: Marca: Volvo, Model: V40, Token masina: foi01znl24, Pret achizitie: 6604, Pret vanzare: 12283
    by_marca_model_token = service.sort_by_marca_model_token()
    assert (by_marca_model_token[0].marca == "Audi" and by_marca_model_token[0].model == "A3"
            and by_marca_model_token[0].token_masina == "wt98fnpsku"), "Incorrect sort by marca-model-token"
    assert (by_marca_model_token[-1].marca == "Volvo" and by_marca_model_token[-1].model == "V40"
            and by_marca_model_token[-1].token_masina == "foi01znl24"), "Incorrect sort by marca-model-token"

    # ====== Test .sort_by_profit() method ==========================================================================

    # 1 Masina: Marca: Toyota, Model: Avalon, Token masina: x8fu5lo3m9, Pret achizitie: 8920, Pret vanzare: 3916
    # -1 Masina: Marca: BMW, Model: X5, Token masina: ndizj7lng2, Pret achizitie: 2168, Pret vanzare: 14999
    by_profit = service.sort_by_profit()
    assert (by_profit[0].pret_achizitie == 8920 and by_profit[0].pret_vanzare == 3916), "Incorrect sort by profit"
    assert (by_profit[-1].pret_achizitie == 2168 and by_profit[-1].pret_vanzare == 14999), "Incorrect sort by profit"


# ========== Test all =================================================================================================
def test_all():
    test_masina()
    test_repository()
    test_service()
