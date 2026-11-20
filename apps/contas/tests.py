import pytest

from apps.contas.models import Usuario


@pytest.mark.django_db
def test_criar_usuario_com_perfil_padrao_vendedor():
    usuario = Usuario.objects.create_user(
        username="vendedor1",
        email="vendedor@email.com",
        password="senha-segura-123",
    )
    assert usuario.perfil == Usuario.Perfil.VENDEDOR
    assert usuario.eh_vendedor
    assert not usuario.eh_gerente
    assert not usuario.eh_estoquista
    assert str(usuario) == "vendedor1"


@pytest.mark.django_db
def test_criar_usuario_gerente():
    gerente = Usuario.objects.create_user(
        username="gerente1",
        email="gerente@email.com",
        password="senha-segura-123",
        perfil=Usuario.Perfil.GERENTE,
    )
    assert gerente.perfil == Usuario.Perfil.GERENTE
    assert gerente.eh_gerente
    assert not gerente.eh_vendedor


@pytest.mark.django_db
def test_criar_usuario_estoquista():
    estoquista = Usuario.objects.create_user(
        username="estoquista1",
        email="estoquista@email.com",
        password="senha-segura-123",
        perfil=Usuario.Perfil.ESTOQUISTA,
    )
    assert estoquista.perfil == Usuario.Perfil.ESTOQUISTA
    assert estoquista.eh_estoquista
    assert not estoquista.eh_gerente
