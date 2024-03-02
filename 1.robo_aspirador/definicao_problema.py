# Robo aspirador (Vacuum Cleanner)

# Ambientes {A,B}
# Estados {Limpo, Não Limpo}
# Ações {Limpar, Não fazer nada}

# Casos
#   1. O robô pode começar em ambos os ambientes, A e B
#   2. Caso o ambiente esteja sujo o robô limpa
#   3. O robô precisa lembrar por onde ele passou, para não haver looping infinito
#   4. O robô anda apenas para os lados direito e esquerdo

# Classes
#   Ambiente
#   Robô
#   Local: Conjunto de ambiente