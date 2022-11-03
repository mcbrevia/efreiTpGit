from lib import calcul_moyenne

def test_moyenne():
    data =[1,1,1]

    result = calcul_moyenne(data)


    assert result == 1