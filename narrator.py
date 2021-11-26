import random
i = "i"
e_list = [
    "",
    "e1",
    "e2",
    "e3",
]
rus_b_list = [
    "",
    "б1",
    "б2",
]
eng_b_list = [
    "",
    "b1",
    "b2"
]
rus_v_list = [
    "",
    "в1",
    "в2",
    "в3",
]
w_list = [
    "",
    "w1",
    "w2",
    "w3",
]
rus_g = [
    "",
    "г1",
    "г2",
    "г3",
]
en_g = [
    "",
    "g1",
    "g2",
    "g3",
]
A_list = [
    "",
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10",
    "A11",
    "A12",
    "A13",
    "A14",
    "A15",
    "A16",
    "A16+",
    "A17",
    "A17+",
    "A18",
    "A19",
]
a_list = [
    "",
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
]
rus_V_list = [
    "",
    "В1",
    "В2",
    "В3",
    "В4",
    "В5",
    "В6",
    "В7",
]
C = [
    "",
    "С",
    "С*",
    "С**",
]
arrow_up = "{"
rus_D_list = [
    "",
    "Д1",
    "Д2",
    "Д3",
    "Д4",
    "Д5",
    "Д6",
    "Д7",
    "Д7*",
    "д7",
    "Д8",
    "Д9",
    "Д10",
]

rus_G_list = [
    "",
    "Г1",
    "Г2",
    "Г3",
    "Г4",
    "Г5",
    "Г6+",
    "Г7",
    "Г10",
]
Z_list = [
    "",
    "Z1",
    "Z2",
    "Z3",
    "Z4",
    "Z5",
    "Z6",
    "Z7",
    "Z8",
    "Z9",
]
R_list = [
    "",
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
]
rus_B_list = [
    "",
    "Б1",
    "Б2",
]
rus_P_list = [
    "",
    "П1",
    "П2",
    "П3",
    "П4",
    "П5",
    "П6",
]
K_list = [
    "",
    "K1",
    "K2",
    "K3",
]
rus_L_list = [
    "",
    "Л1",
    "Л2",
    "Л3",
    "Л4",
    "Л5",
    "Л6",
    "Л7",
    "Л8",
    "Л9",
    "Л10",
]
arrow_down = "}"

pr_list = [
    "",
    "Пр1",
    "Пр2",
    "Пр3",
    "Пр4",
    "Пр5",
    "Пр6",
    "Пр7",
]
Sp_list = [
    "",
    "Сп1",
    "Сп2",
    "Сп3",
    "Сп4",
    "Сп5",
    "Сп6",
    "Сп7",
    "Сп8",
    "Сп9",
    "Сп10",
]
ruz_H = "H"
rus_F = "Ф"
rus_Z = "З"
rus_R = "Р"
T_list = [
    "",
    "T1",
    "T2",
    "T3",
    "T4",
]
left_arrow = "<--"
s = "s"
mot = "mot"
con = "con"
Pos = "Pos"
neg = "neg"
contr = "contr"

def start_list():
    start_list = []
    start_list.append(random.choice(rus_D_list))
    start_list.append(random.choice(rus_G_list))
    start_list.append(random.choice(Z_list))
    return start_list

print(start_list())


def generate_plot():
    start_list = []
