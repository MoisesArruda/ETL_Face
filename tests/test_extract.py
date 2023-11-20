from app.pipeline.extract import definir_caminhos

def test_definir_caminhos():
    caminhos = definir_caminhos()
    origem, staging, destino = caminhos

    assert origem is not None
    assert staging is not None
    assert destino is not None