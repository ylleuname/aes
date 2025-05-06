import random
import math

def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def gerar_primo(valor_minimo, valor_maximo):
    """Gera um número primo aleatório dentro de um intervalo."""
    while True:
        num = random.randint(valor_minimo, valor_maximo)
        if eh_primo(num):
            return num

def calcular_mdc(a, b):
    """Calcula o Máximo Divisor Comum de dois números."""
    while b:
        a, b = b, a % b
    return a

def calcular_mdc_estendido(a, b):
    """Calcula o MDC e os coeficientes da identidade de Bézout."""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = calcular_mdc_estendido(b % a, a)
        return g, x - (b // a) * y, y

def calcular_inverso_modular(a, m):
    """Calcula o inverso multiplicativo modular de 'a' módulo 'm'."""
    g, x, y = calcular_mdc_estendido(a % m, m)
    if g != 1:
        raise Exception('Inverso modular não existe')
    else:
        return x % m

def gerar_chaves_simples():
    """Gera chaves RSA simplificadas (inseguro para uso real)."""
    p = gerar_primo(50, 100)
    q = gerar_primo(101, 150)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Escolhe um 'e' pequeno e relativamente primo com phi_n
    expoente_publico = 65537  # Um valor comum, mas a escolha aqui é simplificada

    # Calcula 'd' (inverso modular de 'e' mod phi_n)
    expoente_privado = calcular_inverso_modular(expoente_publico, phi_n)

    chave_publica = (n, expoente_publico)
    chave_privada = (n, expoente_privado)
    return chave_publica, chave_privada

def criptografar_numero_simples(chave_publica, numero):
    """Criptografa um número usando a chave pública RSA (simplificado e inseguro)."""
    n, e = chave_publica
    texto_cifrado = pow(numero, e, n)
    return texto_cifrado

def descriptografar_numero_simples(chave_privada, texto_cifrado):
    """Descriptografa um número usando a chave privada RSA (simplificado e inseguro)."""
    n, d = chave_privada
    texto_original = pow(texto_cifrado, d, n)
    return texto_original

if __name__ == "__main__":
    # Gera um par de chaves RSA simplificado
    chave_publica, chave_privada = gerar_chaves_simples()
    print(f"Chave Pública (n, e): {chave_publica}")
    print(f"Chave Privada (n, d): {chave_privada}")

    # Número a ser criptografado (deve ser menor que n)
    mensagem = 42
    print(f"\nMensagem original (número): {mensagem}")

    # Criptografa o número
    mensagem_cifrada = criptografar_numero_simples(chave_publica, mensagem)
    print(f"Mensagem criptografada: {mensagem_cifrada}")

    # Decriptografa o número
    mensagem_original = descriptografar_numero_simples(chave_privada, mensagem_cifrada)
    print(f"Mensagem decriptografada: {mensagem_original}")