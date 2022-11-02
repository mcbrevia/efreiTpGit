from lib import calcul_moyenne

def test_moyenne():
    data = [1,1,1]
    expected_result = 1

    result = calcul_moyenne(data)

    if result != expected_result:
        print("Error : calcul_moyenne")
        exit(1)

test_moyenne()
exit(0)
