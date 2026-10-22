# %%

def dobro(n):
    return n * 2

print(dobro(5))

def test_dobro():
    assert dobro(3) == 6
    assert dobro(0) == 0
    assert dobro(-4) == -8

test_dobro()
print("Todos os testes passaram!")



# %%
n=5
print("Dobro: ",n*2)

